# Personal Assistant Agent - Development Progress

## Project Overview
Building a personal assistant agent using LangGraph that runs on Raspberry Pi 5, accessible via Telegram bot.

**Key Features:**
- RAG capabilities (web page knowledge)
- Task management
- Calendar integration (Google + iOS/iCloud)
- Persistent memory storage
- Multi-LLM provider support (Chinese models: DeepSeek, Qwen, Zhipu AI)

**Full Implementation Plan:** See `/Users/bsp/.claude/plans/purrfect-strolling-balloon.md`

---

## Current Status: Phase 1 - Project Setup & Foundation

### ✅ Completed
- [x] Updated `.gitignore` with comprehensive Python project ignores

### 🏗️ In Progress
- [ ] Setting up project directory structure

### 📋 Next Steps
1. Create directory structure (`src/`, `data/`, `tests/`)
2. Create `requirements.txt` with core dependencies
3. Create `.env.example` template
4. Create `src/config.py` for configuration management
5. Create basic `src/main.py` entry point

---

## Key Decisions Made

### LLM Provider
- **TBD**: Need to decide between DeepSeek V3, Qwen 2.5-Max, or starting with OpenAI/Anthropic
- Will support multiple providers for experimentation

### Python Version
- Using Python 3.10 (current venv)

### Project Structure
```
personal-assistant-agent/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── telegram_bot/
│   ├── agent/
│   ├── services/
│   └── utils/
├── data/
│   ├── vector_store/
│   ├── checkpoints/
│   └── tasks.db
├── tests/
└── requirements.txt
```

### Configuration Approach
- **TBD**: Using `.env` file with `python-dotenv` (decision pending)

---

## Dependencies to Install

### Core
- langgraph>=0.2.0
- langchain>=0.3.0
- langchain-core
- python-telegram-bot>=21.0
- python-dotenv

### Storage & RAG
- chromadb
- sentence-transformers
- sqlalchemy
- aiosqlite

### Calendar Integration (Later)
- google-auth
- google-auth-oauthlib
- google-api-python-client
- pyicloud

### Additional (TBD)
- httpx / requests (web scraping)
- beautifulsoup4 (HTML parsing)
- fastapi + uvicorn (optional API server)
- pytest (testing)

---

## API Keys Needed

- [ ] Telegram Bot Token (from @BotFather)
- [ ] LLM API Key (DeepSeek/Qwen/OpenAI/etc.)
- [ ] Google Calendar API credentials (Phase 6)

---

## Notes & Gotchas

- **User wants to code themselves**: Guide and suggest, don't implement unless asked
- **Start simple**: Begin with basic conversational agent, add complexity incrementally
- **Learning focus**: This is a learning project for LangGraph concepts

---

## Phase Breakdown (8 weeks)

1. **Phase 1 (Week 1)**: Project Setup & Foundation ⬅️ YOU ARE HERE
2. **Phase 2 (Week 1-2)**: Simple LangGraph Agent
3. **Phase 3 (Week 2)**: Telegram Bot Integration
4. **Phase 4 (Week 3)**: Memory & Persistence
5. **Phase 5 (Week 3-4)**: RAG Implementation
6. **Phase 6 (Week 4-5)**: Calendar Integration
7. **Phase 7 (Week 5)**: Task Management
8. **Phase 8 (Week 6)**: Advanced LangGraph Features
9. **Phase 9 (Week 6-7)**: Raspberry Pi Deployment
10. **Phase 10 (Week 7-8)**: Testing & Refinement

---

**Last Updated:** 2025-12-28
