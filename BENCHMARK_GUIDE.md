# TMC Benchmarking Guide for Windows

## Prerequisites

1. **Python 3.8+** installed on Windows
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **TMC Server running** with valid license
   - Use `run-tmc-server.bat` or `run-tmc-server.ps1`
   - Server should be accessible at http://localhost:8000

## Quick Start

### Option 1: Simple Benchmark (Recommended)

1. Open **Command Prompt** or **PowerShell**

2. Install required packages:
```powershell
pip install requests numpy
```

3. Run the basic TMC benchmark:
```powershell
python benchmark_tmc.py
```

This will:
- Load 100,000 memories into TMC
- Run retrieval tests
- Show performance metrics (latency, throughput)

### Option 2: Comprehensive Benchmark

For detailed performance analysis:

```powershell
python benchmark_comprehensive.py
```

This includes:
- Multiple query types
- Precision/recall metrics
- Latency percentiles
- Comparison charts

### Option 3: Comparison with Competitors

To compare TMC vs Pinecone/Milvus:

```powershell
# Install additional dependencies
pip install pinecone-client pymilvus chromadb

# Run comparison
python benchmark_milvus_pinecone.py
```

## Available Benchmark Scripts

| Script | Purpose | Time to Run |
|--------|---------|-------------|
| `benchmark_tmc.py` | Basic performance test | ~2-3 min |
| `benchmark_comprehensive.py` | Full performance analysis | ~5-10 min |
| `benchmark_semantic_accuracy.py` | Precision/recall testing | ~3-5 min |
| `benchmark_recall_precision_fixed.py` | Detailed accuracy metrics | ~5 min |
| `benchmark_milvus_pinecone.py` | Compare vs competitors | ~15-20 min |

## Troubleshooting

### Server not responding
```powershell
# Check if server is running
curl http://localhost:8000/health
```

Expected response: `OK`

### Python packages missing
```powershell
pip install requests numpy matplotlib pandas
```

### Port already in use
If port 8000 is busy, modify the server startup or benchmark script to use a different port.

## Results Location

Benchmark results are saved as JSON files:
- `benchmark_results.json`
- `benchmark_comprehensive_results.json`
- etc.

Charts (if generated) are saved as PNG files in `benchmark_charts/`

## Quick Performance Check

To quickly verify TMC is working:

```powershell
curl -X POST http://localhost:8000/crystallize -H "Content-Type: application/json" -d "{\"text\":\"Test memory\",\"importance\":0.8}"
```

Expected: JSON response with `node_id` and `success: true`

## Contact

For issues or questions:
- Email: kent.stone@gmail.com
- Phone: +51 945 012 953
