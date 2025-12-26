# TMC - Temporal Memory Crystallization

**Choose Your Speed: Lightning-Fast Basic Search OR Intelligent Multi-Layer Memory**

[![Free Version](https://img.shields.io/badge/TMC_Free-v1.0_Blazing_Fast-brightgreen)](https://github.com/kentstone84/Ai_Memory)
[![Pro Version](https://img.shields.io/badge/TMC_Pro-v1.1+_Intelligent-blue)](https://github.com/kentstone84/Ai_Memory)
[![License](https://img.shields.io/badge/Free_Tier-Open_Source-green)](https://github.com/kentstone84/Ai_Memory)

---

## 🚀 TMC Free - Lightning Fast Vector Search

**255× faster than Pinecone. No strings attached.**

### Performance (100k vectors):
- ⚡ **Sub-3ms retrieval** latency
- 📊 **92% precision** in similarity search
- 🚄 **255× faster** than Pinecone
- 💰 **100% FREE** - No license required

### Perfect For:
- Basic RAG (Retrieval Augmented Generation)
- High-speed similarity search
- Simple vector storage and retrieval
- Learning and experimentation

### Download TMC Free:
- [Windows v1.0](https://github.com/kentstone84/AiMemory/releases/v1.0-free)
- [macOS v1.0](https://github.com/kentstone84/AiMemory/releases/v1.0-free)
- [Linux v1.0](https://github.com/kentstone84/AiMemory/releases/v1.0-free)

**No license. No limits. Just speed.** ⚡

---

## 🧠 TMC Pro - Intelligent AI Memory

**When you need memory that thinks, not just searches.**

### What Makes It Different:

TMC Pro isn't just vector search - it's a **multi-dimensional memory system**:

- **📝 Content Layer** - Hash-based exact matching
- **🧩 Semantic Layer** - Meaning and concept similarity
- **💭 Emotional Layer** - Sentiment and tone analysis
- **⏰ Temporal Layer** - Time-aware relevance
- **🎯 Importance** - Priority-based filtering

### The Trade-Off:

| Metric | TMC Free | TMC Pro | What You Get |
|--------|----------|---------|--------------|
| **Query Speed** | 3ms | ~20-100ms | Emotional + temporal context |
| **Layers** | 1 (semantic) | 5 (multi-dimensional) | Intelligence vs raw speed |
| **Use Case** | Fast search | Smart memory | Simple vs sophisticated |
| **License** | FREE | Paid | Open source vs proprietary |

### Perfect For:

✅ **AI Agents** - Agents that remember context, emotions, and timing
✅ **Emotional AI** - Chatbots with sentiment awareness
✅ **Personal Knowledge** - Systems that track what matters and when
✅ **Intelligent Assistants** - Not just similar, but contextually relevant
✅ **Research Platforms** - Multi-dimensional analysis

### Retrieval Modes:

TMC Pro adapts its strategy based on your query:

```
Query: "I'm feeling overwhelmed with deadlines"

┌─────────────────────────────────────┐
│     TMC Pro Adaptive Retrieval      │
├─────────────────────────────────────┤
│ Hash:     "overwhelmed" "deadlines" │ 35%
│ Semantic: stress/anxiety concepts   │ 30%
│ Emotional: negative sentiment       │ 25%
│ Temporal: recent memories           │ 10%
└─────────────────────────────────────┘
```

- **Adaptive** - AI decides the best strategy
- **SemanticOnly** - Pure meaning search
- **HashOnly** - Exact keywords
- **Hybrid** - Custom weight control
- **Temporal** - Time-based relevance
- **Emotional** - Sentiment matching

### Get TMC Pro:

**Contact for licensing:**
- Email: kent.stone@gmail.com
- Phone: +51 945 012 953

**Pricing:**
- **Starter**: Development & testing
- **Pro**: Production applications
- **Enterprise**: Unlimited usage
- **Academic**: Research discounts available

---

## 📥 Quick Start

### TMC Free (v1.0)

1. **Download** the free version for your platform
2. **Run** it - no license needed
3. **Store** memories:
   ```bash
   curl -X POST http://localhost:8000/crystallize \
     -H "Content-Type: application/json" \
     -d '{"text": "Your memory here", "importance": 0.8}'
   ```
4. **Retrieve** with lightning speed:
   ```bash
   curl -X POST http://localhost:8000/retrieve \
     -H "Content-Type: application/json" \
     -d '{"query": "search term", "k": 5}'
   ```

### TMC Pro (v1.1+)

1. **Get a license** from kent.stone@gmail.com
2. **Download** TMC Pro for your platform:
   - [Windows Pro](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server.exe)
   - [macOS Intel Pro](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-macos-intel)
   - [macOS ARM Pro](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-macos-arm)
   - [Linux Pro](https://github.com/kentstone84/AiMemory/releases/latest/download/tmc-server-linux)

3. **Run with license**:
   ```bash
   TMC_LICENSE_KEY="your-key" ./tmc-server
   ```

4. **Use intelligent memory**:
   ```bash
   curl -X POST http://localhost:8000/v1.1/crystallize \
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
   curl -X POST http://localhost:8000/v1.1/retrieve \
     -H "Content-Type: application/json" \
     -d '{
       "query": "positive work experiences",
       "k": 10,
       "mode": "Adaptive"
     }'
   ```

---

## 🎯 Which Version Should You Choose?

### Choose TMC Free if:
- ✅ You need blazing-fast vector search
- ✅ Simple similarity search is enough
- ✅ You're building basic RAG systems
- ✅ You want to experiment first
- ✅ Budget is a concern

### Choose TMC Pro if:
- ✅ You're building AI agents with memory
- ✅ Emotional context matters
- ✅ You need temporal awareness
- ✅ Multi-dimensional search is valuable
- ✅ You want "smart" not just "fast"

### Or Start Free, Upgrade Later!

Many customers start with TMC Free and upgrade to Pro when they need:
- Emotional intelligence
- Temporal context
- Adaptive retrieval
- Multi-layer analysis

---

## 📊 API Endpoints

### TMC Free (v1.0) Endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/crystallize` | POST | Store memory |
| `/retrieve` | POST | Search memories |
| `/stats` | GET | System statistics |

### TMC Pro (v1.1+) Additional Endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1.1/crystallize` | POST | Multi-layer storage |
| `/v1.1/retrieve` | POST | Adaptive retrieval |

---

## 🛠️ Integration Examples

### Python Integration (Works with both versions)

```python
import requests

class TMCClient:
    def __init__(self, base_url="http://localhost:8000", pro=False):
        self.base_url = base_url
        self.pro = pro

    def remember(self, text, importance=0.5, emotion=None):
        """Store a memory"""
        endpoint = "/v1.1/crystallize" if self.pro else "/crystallize"
        payload = {"text": text, "importance": importance}

        if self.pro and emotion:
            payload["emotion_vector"] = emotion

        return requests.post(f"{self.base_url}{endpoint}", json=payload).json()

    def recall(self, query, k=5, mode="Adaptive"):
        """Retrieve memories"""
        endpoint = "/v1.1/retrieve" if self.pro else "/retrieve"
        payload = {"query": query, "k": k}

        if self.pro:
            payload["mode"] = mode

        return requests.post(f"{self.base_url}{endpoint}", json=payload).json()

# Use TMC Free
tmc_free = TMCClient(pro=False)
tmc_free.remember("Fast memory storage", importance=0.8)
results = tmc_free.recall("fast storage")

# Use TMC Pro
tmc_pro = TMCClient(pro=True)
tmc_pro.remember(
    "Exciting breakthrough!",
    importance=0.9,
    emotion=[0.9, 0.1, 0.0]  # Positive emotion
)
results = tmc_pro.recall("exciting news", mode="Emotional")
```

### LangChain Integration

```python
from langchain_tmc import TMCVectorStore

# TMC Free - fast and simple
vectorstore_free = TMCVectorStore(
    url="http://localhost:8000",
    version="free"
)

# TMC Pro - intelligent and adaptive
vectorstore_pro = TMCVectorStore(
    url="http://localhost:8000",
    version="pro",
    mode="Adaptive",
    include_emotions=True
)
```

---

## 📈 Benchmarking

Want to verify the performance claims?

**TMC Free benchmarks:**
```bash
python benchmark_tmc_free.py
```

**TMC Pro benchmarks:**
```bash
python benchmark_tmc_pro.py
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

- **TMC Free (v1.0):** Open Source - Use freely
- **TMC Pro (v1.1+):** Proprietary - Commercial license required

---

## 🎯 The Bottom Line

**Need speed?** → Use TMC Free (v1.0)

**Need intelligence?** → Upgrade to TMC Pro (v1.1+)

**Not sure?** → Start free, upgrade when you need more

---

**© 2025 TMC. All rights reserved.**

*TMC Free - Stupid fast. TMC Pro - Stupid smart.*
