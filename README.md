# LangGraph Test

A test project using LangGraph and LangChain for building multi-agent systems.

## Quick Start

1. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill in your API keys:
```bash
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
```

4. Run the project:
```bash
langgraph dev
```

## Project Structure
- `multi_agent/` - Multi-agent system code
- `files/` - Project files
- `.env` - Environment variables (create from .env.example)
- `requirements.txt` - Python dependencies
