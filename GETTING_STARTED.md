# Getting Started with TMC

Welcome to TMC - your intelligent multi-layer memory system!

## Prerequisites

- **Valid License Key** - Contact kent.stone@gmail.com
- **Python 3.8+** (for benchmarks and integration)
- **Network Access** - Port 8000 for the server

## Installation Steps

### 1. Download TMC Server

Choose your platform:

- **Windows**: [tmc-server.exe](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server.exe)
- **macOS (Intel)**: [tmc-server-macos-intel](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-macos-intel)
- **macOS (Apple Silicon)**: [tmc-server-macos-arm](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-macos-arm)
- **Linux**: [tmc-server-linux](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-linux)

### 2. Get Your License

Contact us for a license key:
- **Email**: kent.stone@gmail.com
- **Phone**: +51 945 012 953

We offer:
- **Enterprise licenses** - Full featured, unlimited usage
- **Pro licenses** - Perfect for production applications
- **Starter licenses** - Great for development and testing
- **Academic discounts** - Available for research institutions

### 3. Run the Server

#### Option A: Windows (Easy)

1. Download `run-tmc-server.bat` from this repository
2. Edit the file and replace `your-license-key-here` with your actual license
3. Double-click the file to start the server

#### Option B: Command Line

**Windows (Command Prompt)**:
```cmd
set TMC_LICENSE_KEY=your-license-key-here
tmc-server.exe
```

**Windows (PowerShell)**:
```powershell
$env:TMC_LICENSE_KEY="your-license-key-here"
.\tmc-server.exe
```

**macOS / Linux**:
```bash
chmod +x tmc-server-*
TMC_LICENSE_KEY="your-license-key-here" ./tmc-server-*
```

### 4. Verify It's Running

Open a new terminal/command prompt and run:

```bash
curl http://localhost:8000/health
```

You should see: `OK`

## First Steps

### Store Your First Memory

```bash
curl -X POST http://localhost:8000/crystallize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "TMC is an intelligent memory system with emotional awareness",
    "importance": 0.9
  }'
```

Response:
```json
{
  "node_id": "550e8400-e29b-41d4-a716-446655440000",
  "success": true
}
```

### Retrieve Memories

```bash
curl -X POST http://localhost:8000/retrieve \
  -H "Content-Type: application/json" \
  -d '{
    "query": "memory system with emotions",
    "k": 5
  }'
```

Response:
```json
{
  "results": [
    {
      "node_id": "550e8400-e29b-41d4-a716-446655440000",
      "content": "TMC is an intelligent memory system with emotional awareness",
      "score": 0.95,
      "importance": 0.9
    }
  ],
  "count": 1
}
```

### Check Statistics

```bash
curl http://localhost:8000/stats
```

## Next Steps

1. **Read the Documentation**
   - [README.md](README.md) - Full feature overview
   - [BENCHMARK_GUIDE.md](BENCHMARK_GUIDE.md) - Performance testing

2. **Try Advanced Features**
   - Multi-layer crystallization with emotional vectors
   - Adaptive retrieval modes
   - Custom weight configurations

3. **Integrate with Your App**
   - Python client examples in README
   - LangChain integration
   - REST API documentation

4. **Run Benchmarks**
   ```bash
   python run-benchmark.py
   ```

## Troubleshooting

### Server Won't Start

**Error**: "TMC_LICENSE_KEY not set"
- **Solution**: Make sure you've set the environment variable with your license key

**Error**: "Invalid license"
- **Solution**: Check that your license key is correct and hasn't expired
- **Contact**: kent.stone@gmail.com if you need a new license

**Error**: "Address already in use"
- **Solution**: Another service is using port 8000. Either stop it or run TMC on a different port

### Can't Connect to Server

1. Check if the server is running:
   ```bash
   curl http://localhost:8000/health
   ```

2. Check firewall settings - port 8000 must be accessible

3. On Windows, you may need to allow the application through Windows Firewall

### Performance Issues

- TMC stores 5 layers of data (hash, semantic, emotional, temporal, metadata)
- This uses more memory than simple vector databases
- Expect ~9ms average query latency with 100k memories
- For millions of vectors, consider hardware upgrades

## Support

Need help?
- **Email**: kent.stone@gmail.com
- **Phone**: +51 945 012 953
- **GitHub Issues**: https://github.com/kentstone84/Ai_Memory/issues

---

**Happy crystallizing! 🧠**
