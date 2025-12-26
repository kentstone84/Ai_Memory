#!/usr/bin/env python3
"""
COMPREHENSIVE VECTOR DATABASE BENCHMARK
TMC vs FAISS vs Qdrant vs Elasticsearch

Tests:
- Load performance (1k, 10k, 100k vectors)
- Query latency (mean, median, p95, p99)
- Throughput (queries per second)

Fair comparison using same embeddings across all systems.
"""

import time
import statistics
import json
import numpy as np
from typing import Dict, List, Tuple
import requests

# ============== CONFIG ==============

TMC_BASE_URL = "http://localhost:8000"
QDRANT_URL = "http://localhost:6333"
ES_URL = "http://localhost:9200"

EMBEDDING_DIM = 384
DATASET_SIZES = [1000, 10000, 100000]
QUERY_ITERATIONS = 100
K = 5

TEST_QUERIES = [
    "What is artificial intelligence?",
    "Tell me about memory systems",
    "How do AI systems retrieve information?",
    "Explain structured memory",
    "AI performance optimization",
]

# ============== EMBEDDING ==============

def simple_hash_embed(text: str, dim: int = EMBEDDING_DIM) -> np.ndarray:
    """Simple hash-based embedding (like TMC uses)"""
    embedding = np.zeros(dim, dtype=np.float32)
    words = text.lower().split()
    for word in words:
        hash_val = hash(word) % dim
        embedding[hash_val] += 1.0
    # Normalize
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    return embedding


def generate_dataset(n: int) -> List[Tuple[str, np.ndarray, float]]:
    """Generate test dataset: (text, embedding, importance)"""
    texts = [
        f"Artificial intelligence and machine learning system #{i} with structured memory architecture"
        for i in range(n)
    ]
    return [(text, simple_hash_embed(text), 0.5 + (i % 5) * 0.1) for i, text in enumerate(texts)]


# ============== TMC BENCHMARK ==============

class TMCBenchmark:
    def __init__(self):
        self.name = "TMC"
        self.session = requests.Session()

    def setup(self, dataset: List[Tuple[str, np.ndarray, float]]) -> float:
        """Load dataset and return load time in seconds"""
        print(f"\n📝 Loading {len(dataset)} vectors into TMC...")

        # Clear existing data
        try:
            self.session.post(f"{TMC_BASE_URL}/clear", timeout=5)
        except:
            pass

        start = time.time()
        for text, embedding, importance in dataset:
            self.session.post(
                f"{TMC_BASE_URL}/crystallize",
                json={"text": text, "importance": importance},
                timeout=5
            ).raise_for_status()

        load_time = time.time() - start
        print(f"✅ Loaded in {load_time:.2f}s ({len(dataset)/load_time:.0f} ops/s)")
        return load_time

    def benchmark_queries(self) -> Dict[str, float]:
        """Run queries and return latency statistics (in ms)"""
        latencies = []
        for i in range(QUERY_ITERATIONS):
            query = TEST_QUERIES[i % len(TEST_QUERIES)]
            t0 = time.time()
            r = self.session.post(
                f"{TMC_BASE_URL}/retrieve",
                json={"query": query, "k": K},
                timeout=5
            )
            r.raise_for_status()
            latencies.append((time.time() - t0) * 1000)

        return calculate_stats(latencies)


# ============== FAISS BENCHMARK ==============

class FAISSBenchmark:
    def __init__(self):
        self.name = "FAISS"
        try:
            import faiss
            self.faiss = faiss
            self.index = None
            self.texts = []
        except ImportError:
            raise ImportError("FAISS not installed. Run: pip install faiss-cpu")

    def setup(self, dataset: List[Tuple[str, np.ndarray, float]]) -> float:
        """Load dataset and return load time in seconds"""
        print(f"\n📝 Loading {len(dataset)} vectors into FAISS...")

        start = time.time()

        # Extract embeddings
        self.texts = [text for text, _, _ in dataset]
        embeddings = np.array([emb for _, emb, _ in dataset], dtype=np.float32)

        # Create flat index (most fair comparison to TMC's brute force)
        self.index = self.faiss.IndexFlatL2(EMBEDDING_DIM)
        self.index.add(embeddings)

        load_time = time.time() - start
        print(f"✅ Loaded in {load_time:.2f}s ({len(dataset)/load_time:.0f} ops/s)")
        return load_time

    def benchmark_queries(self) -> Dict[str, float]:
        """Run queries and return latency statistics (in ms)"""
        latencies = []
        for i in range(QUERY_ITERATIONS):
            query = TEST_QUERIES[i % len(TEST_QUERIES)]
            query_emb = simple_hash_embed(query).reshape(1, -1)

            t0 = time.time()
            distances, indices = self.index.search(query_emb, K)
            latencies.append((time.time() - t0) * 1000)

        return calculate_stats(latencies)


# ============== QDRANT BENCHMARK ==============

class QdrantBenchmark:
    def __init__(self):
        self.name = "Qdrant"
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.models import Distance, VectorParams, PointStruct
            self.QdrantClient = QdrantClient
            self.Distance = Distance
            self.VectorParams = VectorParams
            self.PointStruct = PointStruct
            self.client = None
            self.collection_name = "benchmark_test"
        except ImportError:
            raise ImportError("Qdrant client not installed. Run: pip install qdrant-client")

    def setup(self, dataset: List[Tuple[str, np.ndarray, float]]) -> float:
        """Load dataset and return load time in seconds"""
        print(f"\n📝 Loading {len(dataset)} vectors into Qdrant...")

        self.client = self.QdrantClient(url=QDRANT_URL)

        # Delete collection if exists
        try:
            self.client.delete_collection(self.collection_name)
        except:
            pass

        # Create collection
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=self.VectorParams(size=EMBEDDING_DIM, distance=self.Distance.COSINE)
        )

        start = time.time()

        # Upload in batches
        batch_size = 100
        for i in range(0, len(dataset), batch_size):
            batch = dataset[i:i + batch_size]
            points = [
                self.PointStruct(
                    id=i + j,
                    vector=emb.tolist(),
                    payload={"text": text, "importance": importance}
                )
                for j, (text, emb, importance) in enumerate(batch)
            ]
            self.client.upsert(collection_name=self.collection_name, points=points)

        load_time = time.time() - start
        print(f"✅ Loaded in {load_time:.2f}s ({len(dataset)/load_time:.0f} ops/s)")
        return load_time

    def benchmark_queries(self) -> Dict[str, float]:
        """Run queries and return latency statistics (in ms)"""
        latencies = []
        for i in range(QUERY_ITERATIONS):
            query = TEST_QUERIES[i % len(TEST_QUERIES)]
            query_emb = simple_hash_embed(query)

            t0 = time.time()
            # Use query() method (newer API) or search_points() (older API)
            try:
                results = self.client.query_points(
                    collection_name=self.collection_name,
                    query=query_emb.tolist(),
                    limit=K
                )
            except AttributeError:
                # Fall back to search_points for older versions
                results = self.client.search_points(
                    collection_name=self.collection_name,
                    query_vector=query_emb.tolist(),
                    limit=K
                )
            latencies.append((time.time() - t0) * 1000)

        return calculate_stats(latencies)


# ============== ELASTICSEARCH BENCHMARK ==============

class ElasticsearchBenchmark:
    def __init__(self):
        self.name = "Elasticsearch"
        try:
            from elasticsearch import Elasticsearch
            self.Elasticsearch = Elasticsearch
            self.client = None
            self.index_name = "benchmark_test"
        except ImportError:
            raise ImportError("Elasticsearch not installed. Run: pip install elasticsearch")

    def setup(self, dataset: List[Tuple[str, np.ndarray, float]]) -> float:
        """Load dataset and return load time in seconds"""
        print(f"\n📝 Loading {len(dataset)} vectors into Elasticsearch...")

        # Use compatibility mode for ES 8.x
        self.client = self.Elasticsearch(
            [ES_URL],
            headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=8"}
        )

        # Delete index if exists
        try:
            self.client.indices.delete(index=self.index_name)
        except:
            pass

        # Create index with dense vector mapping
        self.client.indices.create(
            index=self.index_name,
            body={
                "mappings": {
                    "properties": {
                        "text": {"type": "text"},
                        "embedding": {
                            "type": "dense_vector",
                            "dims": EMBEDDING_DIM,
                            "index": True,
                            "similarity": "cosine"
                        },
                        "importance": {"type": "float"}
                    }
                }
            }
        )

        start = time.time()

        # Bulk upload
        from elasticsearch.helpers import bulk

        actions = [
            {
                "_index": self.index_name,
                "_id": i,
                "_source": {
                    "text": text,
                    "embedding": emb.tolist(),
                    "importance": importance
                }
            }
            for i, (text, emb, importance) in enumerate(dataset)
        ]

        bulk(self.client, actions)
        self.client.indices.refresh(index=self.index_name)

        load_time = time.time() - start
        print(f"✅ Loaded in {load_time:.2f}s ({len(dataset)/load_time:.0f} ops/s)")
        return load_time

    def benchmark_queries(self) -> Dict[str, float]:
        """Run queries and return latency statistics (in ms)"""
        latencies = []
        for i in range(QUERY_ITERATIONS):
            query = TEST_QUERIES[i % len(TEST_QUERIES)]
            query_emb = simple_hash_embed(query)

            t0 = time.time()
            response = self.client.search(
                index=self.index_name,
                body={
                    "knn": {
                        "field": "embedding",
                        "query_vector": query_emb.tolist(),
                        "k": K,
                        "num_candidates": 100
                    }
                }
            )
            latencies.append((time.time() - t0) * 1000)

        return calculate_stats(latencies)


# ============== UTILITIES ==============

def calculate_stats(latencies: List[float]) -> Dict[str, float]:
    """Calculate latency statistics"""
    latencies_sorted = sorted(latencies)
    return {
        "mean": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "p95": latencies_sorted[int(0.95 * len(latencies_sorted))],
        "p99": latencies_sorted[int(0.99 * len(latencies_sorted))],
        "min": min(latencies),
        "max": max(latencies)
    }


def print_results(results: Dict):
    """Print formatted results"""
    print("\n" + "=" * 100)
    print("📊 COMPREHENSIVE BENCHMARK RESULTS")
    print("=" * 100)

    for size in DATASET_SIZES:
        if size not in results:
            continue

        print(f"\n🔹 Dataset Size: {size:,} vectors")
        print("-" * 100)

        # Load times
        print("\n📥 Load Performance:")
        print(f"{'System':<15} {'Load Time':<15} {'Ops/Second':<15}")
        print("-" * 50)
        for system, data in results[size].items():
            load_time = data['load_time']
            ops_per_sec = size / load_time if load_time > 0 else 0
            print(f"{system:<15} {load_time:<15.2f} {ops_per_sec:<15.0f}")

        # Query latencies
        print("\n🔍 Query Latency (ms):")
        print(f"{'System':<15} {'Mean':<12} {'Median':<12} {'P95':<12} {'P99':<12} {'Min':<12} {'Max':<12}")
        print("-" * 100)
        for system, data in results[size].items():
            stats = data['query_stats']
            print(f"{system:<15} {stats['mean']:<12.2f} {stats['median']:<12.2f} "
                  f"{stats['p95']:<12.2f} {stats['p99']:<12.2f} "
                  f"{stats['min']:<12.2f} {stats['max']:<12.2f}")

        # Speed comparisons
        print("\n⚡ Speed vs TMC:")
        print("-" * 50)
        if "TMC" in results[size]:
            tmc_mean = results[size]["TMC"]['query_stats']['mean']
            for system, data in results[size].items():
                if system == "TMC":
                    continue
                system_mean = data['query_stats']['mean']
                speedup = system_mean / tmc_mean
                if speedup >= 1:
                    print(f"TMC is {speedup:.1f}x faster than {system}")
                else:
                    print(f"{system} is {1/speedup:.1f}x faster than TMC")


# ============== MAIN ==============

def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║     COMPREHENSIVE VECTOR DATABASE BENCHMARK                                      ║
║     TMC vs FAISS vs Qdrant vs Elasticsearch                                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝
""")

    # Initialize benchmarks
    benchmarks = []

    # Always include TMC
    try:
        r = requests.get(f"{TMC_BASE_URL}/health", timeout=2)
        r.raise_for_status()
        benchmarks.append(TMCBenchmark())
        print("✅ TMC server is running")
    except:
        print("❌ TMC server is not running. Start it with:")
        print("   cd tmc-rust/tmc-api && TMC_LICENSE_KEY='test' cargo run --release")
        return

    # Try to add FAISS
    try:
        benchmarks.append(FAISSBenchmark())
        print("✅ FAISS is available")
    except ImportError as e:
        print(f"⚠️  FAISS not available: {e}")

    # Try to add Qdrant
    try:
        from qdrant_client import QdrantClient
        client = QdrantClient(url=QDRANT_URL)
        client.get_collections()
        benchmarks.append(QdrantBenchmark())
        print("✅ Qdrant is running")
    except Exception as e:
        print(f"⚠️  Qdrant not available: {e}")
        print("   Start it with: docker run -p 6333:6333 qdrant/qdrant")

    # Try to add Elasticsearch
    try:
        from elasticsearch import Elasticsearch
        client = Elasticsearch([ES_URL])
        client.info()
        benchmarks.append(ElasticsearchBenchmark())
        print("✅ Elasticsearch is running")
    except Exception as e:
        print(f"⚠️  Elasticsearch not available: {e}")
        print("   Start it with: docker run -p 9200:9200 -e 'discovery.type=single-node' -e 'xpack.security.enabled=false' elasticsearch:8.11.0")

    if len(benchmarks) == 1:
        print("\n⚠️  Only TMC is available. Install/start other systems for comparison.")
        return

    # Run benchmarks
    results = {}

    for size in DATASET_SIZES:
        print(f"\n{'='*100}")
        print(f"🔬 Testing with {size:,} vectors")
        print(f"{'='*100}")

        dataset = generate_dataset(size)
        results[size] = {}

        for benchmark in benchmarks:
            try:
                print(f"\n🧪 Testing {benchmark.name}...")
                load_time = benchmark.setup(dataset)
                query_stats = benchmark.benchmark_queries()

                results[size][benchmark.name] = {
                    'load_time': load_time,
                    'query_stats': query_stats
                }

            except Exception as e:
                print(f"❌ {benchmark.name} failed: {e}")
                import traceback
                traceback.print_exc()

    # Print results
    print_results(results)

    # Save to file
    output_file = "benchmark_comprehensive_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Results saved to: {output_file}")

    print("\n✅ BENCHMARK COMPLETE!")


if __name__ == "__main__":
    main()
