# Building Modular AI Agents with Strands Skills

A companion project for the article **"Building Modular AI Agents with Strands Skills"**.

Demonstrates the `AgentSkills` plugin from the [Strands Agents](https://strandsagents.com) framework — three independent skills loaded by a single agent, each activated on demand.

---

## Project Structure

```
strands-skills-demo/
├── app.py                          # Streamlit UI (recommended)
├── main.py                         # CLI demo
├── skills/
│   ├── email-drafter/
│   │   └── SKILL.md
│   ├── bug-investigator/
│   │   └── SKILL.md
│   └── git-commit-writer/
│       └── SKILL.md
├── .streamlit/
│   └── secrets.toml.example        # API key template for Streamlit Cloud
├── pyproject.toml
├── .python-version
└── uv.lock
```

---

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- An `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com)

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/your-username/strands-skills-demo.git
cd strands-skills-demo

# 2. Install dependencies
uv sync

# 3. Set your API key
export ANTHROPIC_API_KEY=sk-...

# 4. Run the Streamlit UI
uv run streamlit run app.py

# or run the CLI demo
uv run python main.py
```

Open `http://localhost:8501` in your browser.

---

## How It Works

The agent is loaded with three skills. At startup only their names and descriptions enter the system prompt. Full instructions load on demand when the agent decides it needs them.

```
User message
     │
     ▼
Agent reads available skill names + descriptions
     │
     ▼
Agent calls `skills` tool with the relevant skill name
     │
     ▼
Full instructions load into context
     │
     ▼
Agent responds using skill instructions
```

### The Three Skills

| Skill | Trigger | Output format |
|-------|---------|---------------|
| `email-drafter` | Email request | Subject / Dear / Body / Regards |
| `bug-investigator` | Error or stack trace | 🔍 Root Cause / 🛠 Fix / ✅ Example |
| `git-commit-writer` | Description of a code change | Conventional commit message |

---

## Defining a Skill

Each skill is a directory with a `SKILL.md` file:

```markdown
---
name: bug-investigator
description: Analyzes an error message or stack trace and returns a structured diagnosis.
---

# Bug Investigator Skill

You are a senior software debugger. When given an error, respond in this format:

🔍 Root Cause: ...
🛠 Fix: ...
✅ Example: ...
```

Load all skills in one line:

```python
from strands import Agent, AgentSkills

plugin = AgentSkills(skills="./skills/")
agent = Agent(plugins=[plugin])
```

---

## Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Under **App Settings → Secrets**, add:

```toml
ANTHROPIC_API_KEY = "sk-..."
```

---

## Resources

- [Strands Agents Docs](https://strandsagents.com/docs)
- [Skills Concept Guide](https://strandsagents.com/docs/user-guide/concepts/plugins/skills/)
- [strands-agents on PyPI](https://pypi.org/project/strands-agents/)
