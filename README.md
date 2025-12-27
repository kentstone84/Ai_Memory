# TMC - Temporal Memory Crystallization

**Choose Your Version: v1.0 (Free & Fast) OR v2.0 (Intelligent & Premium)**

[![Free Version](https://img.shields.io/badge/v1.0-Free_&_Blazing_Fast-brightgreen)](https://github.com/kentstone84/Ai_Memory)
[![Pro Version](https://img.shields.io/badge/v2.0-Intelligent_&_Premium-blue)](https://github.com/kentstone84/Ai_Memory)
[![License](https://img.shields.io/badge/v1.0-Open_Source-green)](https://github.com/kentstone84/Ai_Memory)

---

## 🚀 TMC v1.0 - FREE & BLAZING FAST

**255× faster than Pinecone. No license. No limits. No bullshit.**

### Performance (100k vectors):
- ⚡ **Sub-3ms retrieval** latency
- 📊 **92% precision** in similarity search
- 🚄 **255× faster** than Pinecone
- 💰 **100% FREE** - No license required
- 🔓 **Open Source** - Use anywhere, anytime

### Perfect For:
- Basic RAG (Retrieval Augmented Generation)
- High-speed similarity search
- Simple vector storage and retrieval
- Learning and experimentation
- Production apps that need pure speed

### Download TMC v1.0 (FREE):
- [Windows v1.0](https://github.com/kentstone84/AiMemory/releases/download/v1.0/tmc-server-windows.exe)
- [macOS Intel v1.0](https://github.com/kentstone84/AiMemory/releases/download/v1.0/tmc-server-macos-intel)
- [macOS ARM v1.0](https://github.com/kentstone84/AiMemory/releases/download/v1.0/tmc-server-macos-arm)
- [Linux v1.0](https://github.com/kentstone84/AiMemory/releases/download/v1.0/tmc-server-linux)

**No license. No limits. Just speed.** ⚡

---

## 🧠 TMC v2.0 - INTELLIGENT & PREMIUM

**When speed isn't enough - you need memory that actually thinks.**

### What's Different in v2.0?

TMC v2.0 trades pure speed for multi-dimensional intelligence:

| Feature | v1.0 (Free) | v2.0 (Premium) |
|---------|-------------|----------------|
| **Speed** | Sub-3ms ⚡ | ~20-100ms 🐢 |
| **Layers** | 1 (semantic only) | 5 (multi-dimensional) |
| **Emotional Context** | ❌ | ✅ Sentiment analysis |
| **Temporal Awareness** | ❌ | ✅ Time-based relevance |
| **Adaptive Retrieval** | ❌ | ✅ AI decides strategy |
| **License** | FREE | **PAID - Contact for pricing** |

### The 5 Layers in v2.0:

1. **📝 Content Layer** - Hash-based exact matching
2. **🧩 Semantic Layer** - Meaning and concept similarity
3. **💭 Emotional Layer** - Sentiment and tone analysis
4. **⏰ Temporal Layer** - Time-aware relevance
5. **🎯 Importance** - Priority-based filtering

### The Trade-Off:

**v2.0 costs you in TWO ways:**

💸 **Money** - Requires commercial license
🐌 **Speed** - 6-33x slower than v1.0

### Why Choose v2.0?

✅ **AI Agents** - Agents need context, emotions, and timing (not just speed)
✅ **Emotional AI** - Chatbots with sentiment awareness
✅ **Personal Knowledge** - Systems that remember what matters AND when
✅ **Intelligent Assistants** - Context-aware retrieval
✅ **Research Platforms** - Multi-dimensional search

### Adaptive Retrieval in Action:

```
Query: "I'm feeling overwhelmed with work deadlines"

┌─────────────────────────────────────┐
│     TMC v2.0 Adaptive Retrieval     │
├─────────────────────────────────────┤
│ Hash:     "overwhelmed" "deadlines" │ 35%
│ Semantic: stress/anxiety concepts   │ 30%
│ Emotional: negative sentiment       │ 25%
│ Temporal: recent memories           │ 10%
└─────────────────────────────────────┘
    ↓
Intelligently ranked results that understand:
- What you said (keywords)
- What you meant (concepts)
- How you feel (emotion)
- When it matters (time)
```

### Get TMC v2.0:

**📧 Contact for licensing:**
- **Email:** kent.stone@gmail.com
- **Phone:** +51 945 012 953

**Pricing Tiers:**
- **Starter** - Development & testing
- **Pro** - Production applications
- **Enterprise** - Unlimited usage
- **Academic** - Research discounts

### Download TMC v2.0 (Requires License):
- [Windows v2.0](https://github.com/kentstone84/AiMemory/releases/download/v2.0/tmc-server-windows.exe)
- [macOS Intel v2.0](https://github.com/kentstone84/AiMemory/releases/download/v2.0/tmc-server-macos-intel)
- [macOS ARM v2.0](https://github.com/kentstone84/AiMemory/releases/download/v2.0/tmc-server-macos-arm)
- [Linux v2.0](https://github.com/kentstone84/AiMemory/releases/download/v2.0/tmc-server-linux)

---

## 📥 Quick Start

### TMC v1.0 (Free & Fast)

1. **Download** v1.0 for your platform (see links above)
2. **Run** it - no license needed:
   ```bash
   ./tmc-server
   ```
3. **Store** memories:
   ```bash
   curl -X POST http://localhost:8000/crystallize \
     -H "Content-Type: application/json" \
     -d '{"text": "Your memory here", "importance": 0.8}'
   ```
4. **Retrieve** at lightning speed:
   ```bash
   curl -X POST http://localhost:8000/retrieve \
     -H "Content-Type: application/json" \
     -d '{"query": "search term", "k": 5}'
   ```

### TMC v2.0 (Premium & Intelligent)

1. **Get a license** from kent.stone@gmail.com
2. **Download** v2.0 for your platform (see links above)
3. **Run with license**:
   ```bash
   TMC_LICENSE_KEY="your-key-here" ./tmc-server
   ```

   Or on Windows use `run-tmc-server.bat`:
   ```cmd
   set TMC_LICENSE_KEY=your-key-here
   tmc-server.exe
   ```

4. **Use intelligent memory**:
   ```bash
   curl -X POST http://localhost:8000/v2/crystallize \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Feeling excited about the new AI project!",
       "importance": 0.9,
       "emotion_vector": [0.8, 0.1, 0.1],
       "metadata": {"category": "work", "mood": "positive"}
     }'
   ```

5. **Adaptive retrieval**:
   ```bash
   curl -X POST http://localhost:8000/v2/retrieve \
     -H "Content-Type: application/json" \
     -d '{
       "query": "positive work experiences",
       "k": 10,
       "mode": "Adaptive"
     }'
   ```

---

## 🎯 Which Version Should You Choose?

### Choose v1.0 (FREE) if:
- ✅ You need **blazing-fast** vector search
- ✅ Simple similarity search is enough
- ✅ You're building basic RAG systems
- ✅ **Speed is your top priority**
- ✅ Budget is a concern / trying things out

### Choose v2.0 (PAID) if:
- ✅ You're building **AI agents** with memory
- ✅ **Emotional context** matters
- ✅ You need **temporal awareness**
- ✅ Multi-dimensional search is valuable
- ✅ You want **intelligence over speed**

### The Honest Truth:

**v1.0** → Fast but simple (one-dimensional similarity)
**v2.0** → Smart but slower (five-dimensional intelligence)

**Most people should start with v1.0.** Upgrade to v2.0 when you hit the limits of simple similarity search.

---

## 📊 API Endpoints

### v1.0 Endpoints (FREE):

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/crystallize` | POST | Store memory |
| `/retrieve` | POST | Search memories |
| `/stats` | GET | System statistics |

### v2.0 Additional Endpoints (PAID):

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/crystallize` | POST | Multi-layer storage |
| `/v2/retrieve` | POST | Adaptive retrieval |

**Note:** v2.0 includes ALL v1.0 endpoints plus the advanced features.

---

## 🛠️ Integration Examples

### Python Client (Works with both versions)

```python
import requests

class TMCClient:
    def __init__(self, base_url="http://localhost:8000", version=1):
        self.base_url = base_url
        self.version = version

    def remember(self, text, importance=0.5, emotion=None):
        """Store a memory"""
        if self.version == 2:
            endpoint = "/v2/crystallize"
            payload = {
                "text": text,
                "importance": importance,
                "emotion_vector": emotion or [0.5, 0.5, 0.0]
            }
        else:
            endpoint = "/crystallize"
            payload = {"text": text, "importance": importance}

        return requests.post(f"{self.base_url}{endpoint}", json=payload).json()

    def recall(self, query, k=5, mode="Adaptive"):
        """Retrieve memories"""
        if self.version == 2:
            endpoint = "/v2/retrieve"
            payload = {"query": query, "k": k, "mode": mode}
        else:
            endpoint = "/retrieve"
            payload = {"query": query, "k": k}

        return requests.post(f"{self.base_url}{endpoint}", json=payload).json()

# Use v1.0 (Free & Fast)
tmc_v1 = TMCClient(version=1)
tmc_v1.remember("Fast memory storage", importance=0.8)
results = tmc_v1.recall("fast storage")

# Use v2.0 (Premium & Intelligent)
tmc_v2 = TMCClient(version=2)
tmc_v2.remember(
    "Exciting breakthrough!",
    importance=0.9,
    emotion=[0.9, 0.1, 0.0]  # Positive emotion
)
results = tmc_v2.recall("exciting news", mode="Emotional")
```

---

## 📈 Performance Comparison

| Metric | v1.0 (Free) | v2.0 (Paid) | Winner |
|--------|-------------|-------------|--------|
| **Query Speed** | 3ms | 20-100ms | v1.0 (33x faster) |
| **Write Speed** | Fast | Slower | v1.0 |
| **Precision** | 92% | 92%+ | Tie |
| **Emotional Context** | No | Yes | v2.0 |
| **Temporal Awareness** | No | Yes | v2.0 |
| **Adaptive Modes** | No | Yes | v2.0 |
| **Cost** | FREE | PAID | v1.0 |

**Bottom Line:**
- Need speed? → **v1.0**
- Need intelligence? → **v2.0**
- Not sure? → **Start with v1.0**

---

## 📈 Benchmarking

Want to verify the performance claims?

**v1.0 benchmarks:**
```bash
python benchmark_tmc.py
```

**v2.0 benchmarks:**
```bash
python benchmark_comprehensive.py
```

See [BENCHMARK_GUIDE.md](BENCHMARK_GUIDE.md) for details.

---

## 🎓 Documentation

- [Getting Started](GETTING_STARTED.md) - Installation and first steps
- [Benchmark Guide](BENCHMARK_GUIDE.md) - Performance testing
- [License Info](LICENSE) - Terms and conditions

---

## 💬 Support

- **Email:** kent.stone@gmail.com
- **Phone:** +51 945 012 953
- **GitHub Issues:** [Report a bug](https://github.com/kentstone84/Ai_Memory/issues)

---

## 📄 License

- **TMC v1.0:** Open Source - Use freely anywhere
- **TMC v2.0:** Proprietary - **Commercial license required**

**To get a v2.0 license:** Contact kent.stone@gmail.com

---

## 🎯 The Bottom Line

**Need speed?** → Use TMC v1.0 (FREE)

**Need intelligence?** → Get TMC v2.0 (Contact for license)

**Not sure?** → Start with v1.0, upgrade when you need the extra layers

---

## ⚠️ Version History

### v2.0 (Current - Premium)
- Multi-layer architecture (5 layers)
- Emotional context analysis
- Temporal awareness
- Adaptive retrieval modes
- **Requires commercial license**

### v1.0 (Current - Free)
- Lightning-fast vector search
- 255× faster than Pinecone
- Simple similarity search
- **Open source - no license required**

---

**© 2025 TMC. All rights reserved.**

*v1.0 - Stupid fast. v2.0 - Stupid smart.*
