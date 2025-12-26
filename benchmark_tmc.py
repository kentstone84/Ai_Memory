#!/usr/bin/env python3
"""
STRESS BENCHMARK
TMC vs ChromaDB (100k memories)
Real-world, connection-safe, batch-safe
"""

import time
import statistics
import json
import requests
from typing import Dict, List

# ---------------- CONFIG ----------------

TMC_BASE_URL = "http://localhost:8000"
TOTAL_MEMORIES = 100_000
CHROMA_MAX_BATCH = 5000     # < 5461 hard limit
TMC_BATCH = 100             # HTTP-safe chunk
RETRIEVAL_ITERS = 200
K = 5

TEST_TEXT = "Artificial intelligence systems benefit from structured memory."

# ---------------------------------------


def generate_memories(n: int):
    return [(f"{TEST_TEXT} #{i}", 0.8) for i in range(n)]


TEST_QUERIES = [
    "What is artificial intelligence?",
    "Tell me about memory systems",
    "How do AI systems retrieve information?",
    "Explain structured memory",
    "AI performance optimization",
]


# ================= TMC =================

class TMCBenchmark:
    def __init__(self):
        self.name = "TMC"
        self.session = requests.Session()

    def setup(self, memories):
        print(f"\n📝 Loading {len(memories)} memories into TMC...")
        start = time.time()

        for i in range(0, len(memories), TMC_BATCH):
            batch = memories[i:i + TMC_BATCH]
            for text, importance in batch:
                r = self.session.post(
                    f"{TMC_BASE_URL}/crystallize",
                    json={"text": text, "importance": importance},
                    timeout=5
                )
                r.raise_for_status()

        dt = time.time() - start
        print(f"✅ Loaded in {dt:.2f}s ({len(memories)/dt:.0f} ops/s)")
        return dt

    def benchmark(self):
        lat = []
        for i in range(RETRIEVAL_ITERS):
            q = TEST_QUERIES[i % len(TEST_QUERIES)]
            t0 = time.time()
            r = self.session.post(
                f"{TMC_BASE_URL}/retrieve",
                json={"query": q, "k": K},
                timeout=5
            )
            r.raise_for_status()
            lat.append((time.time() - t0) * 1000)

        return summarize(lat)


# ================= CHROMA =================

class ChromaBenchmark:
    def __init__(self):
        import chromadb
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("stress_benchmark")
        self.name = "ChromaDB"

    def setup(self, memories):
        print(f"\n📝 Loading {len(memories)} memories into ChromaDB...")
        start = time.time()

        for i in range(0, len(memories), CHROMA_MAX_BATCH):
            batch = memories[i:i + CHROMA_MAX_BATCH]
            docs = [t for t, _ in batch]
            metas = [{"importance": imp} for _, imp in batch]
            ids = [f"mem_{i+j}" for j in range(len(batch))]

            self.collection.add(
                documents=docs,
                metadatas=metas,
                ids=ids
            )

        dt = time.time() - start
        print(f"✅ Loaded in {dt:.2f}s ({len(memories)/dt:.0f} ops/s)")
        return dt

    def benchmark(self):
        lat = []
        for i in range(RETRIEVAL_ITERS):
            q = TEST_QUERIES[i % len(TEST_QUERIES)]
            t0 = time.time()
            self.collection.query(query_texts=[q], n_results=K)
            lat.append((time.time() - t0) * 1000)

        return summarize(lat)


# ================= UTILS =================

def summarize(latencies: List[float]) -> Dict:
    latencies.sort()
    return {
        "mean": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "p95": latencies[int(0.95 * len(latencies))],
        "p99": latencies[int(0.99 * len(latencies))],
    }


def print_results(results):
    print("\n" + "=" * 72)
    print("📊 STRESS BENCHMARK RESULTS (100k memories)")
    print("=" * 72)
    print(f"{'System':<12} {'Mean(ms)':<12} {'Median':<12} {'P95':<12} {'P99':<12}")
    print("-" * 72)

    for name, r in results.items():
        print(f"{name:<12} {r['mean']:<12.2f} {r['median']:<12.2f} {r['p95']:<12.2f} {r['p99']:<12.2f}")

    speedup = results["ChromaDB"]["mean"] / results["TMC"]["mean"]
    print(f"\n🚀 TMC is **{speedup:.1f}x faster** than ChromaDB (mean latency)")


# ================= MAIN =================

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║        TMC vs ChromaDB — STRESS BENCHMARK                    ║
╚══════════════════════════════════════════════════════════════╝
""")

    # Health check
    r = requests.get(f"{TMC_BASE_URL}/health", timeout=2)
    r.raise_for_status()

    memories = generate_memories(TOTAL_MEMORIES)

    tmc = TMCBenchmark()
    chroma = ChromaBenchmark()

    tmc.setup(memories)
    chroma.setup(memories)

    results = {
        "TMC": tmc.benchmark(),
        "ChromaDB": chroma.benchmark()
    }

    print_results(results)

    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ BENCHMARK COMPLETE")


if __name__ == "__main__":
    main()
