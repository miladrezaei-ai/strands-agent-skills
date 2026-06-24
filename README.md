# Strands AgentSkills — Skills Demo

A minimal, article-ready project demonstrating the **Skills plugin** in the [Strands Agents](https://strandsagents.com) framework.

Skills solve a real problem: as agents handle more tasks, their system prompts balloon with competing instructions. The `AgentSkills` plugin implements *progressive disclosure* — only skill names and descriptions load upfront, and full instructions are fetched on demand when the agent decides it needs them.

---

## Project Structure

```
strands-skills-demo/
├── main.py                        # Entry point — demonstrates both skill approaches
├── skills/
│   ├── good-morning/
│   │   └── SKILL.md               # Filesystem-based skill
│   └── tech-explainer/
│       └── SKILL.md               # Filesystem-based skill
├── pyproject.toml
├── .python-version
└── uv.lock
```

---

## How Skills Work

```
Agent startup
     │
     ▼
AgentSkills plugin injects skill metadata into system prompt
     │
     ▼
Agent receives user message
     │
     ▼
Agent calls `skills` tool with skill name  ◄── only when needed
     │
     ▼
Full instructions loaded into context
     │
     ▼
Agent executes with skill instructions
```

---

## Quickstart

**Prerequisites:** Python 3.12+, [uv](https://docs.astral.sh/uv/), and an `ANTHROPIC_API_KEY`.

```bash
# Clone and install
git clone https://github.com/your-username/strands-skills-demo.git
cd strands-skills-demo
uv sync

# Set your API key
export ANTHROPIC_API_KEY=sk-...

# Run
uv run python main.py
```

---

## Two Ways to Define Skills

### 1. Filesystem-based (SKILL.md)

Create a directory with a `SKILL.md` file using YAML frontmatter:

```
skills/good-morning/
└── SKILL.md
```

```markdown
---
name: good-morning
description: Responds to good-morning greetings with a warm reply and a joke.
---

# Good Morning Skill

You are a cheerful morning companion ...
```

Load it with:

```python
from strands import Agent, AgentSkills

plugin = AgentSkills(skills="./skills/")   # loads all subdirectories
agent = Agent(plugins=[plugin])
```

### 2. Programmatic (inline `Skill` object)

Define skills directly in code — useful for dynamic or environment-specific instructions:

```python
from strands import Agent, AgentSkills, Skill

skill = Skill(
    name="summarizer",
    description="Condenses any text into a crisp bullet-point summary.",
    instructions="Extract the 3-5 most important points as bullet points ...",
)

plugin = AgentSkills(skills=[skill])
agent = Agent(plugins=[plugin])
```

You can also mix both approaches:

```python
plugin = AgentSkills(skills=["./skills/", skill])
```

---

## SKILL.md Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier — lowercase alphanumeric and hyphens, 1–64 chars |
| `description` | Yes | Shown in the system prompt; helps the agent decide when to activate the skill |
| `allowed-tools` | No | Space-delimited list of tools the skill may use |

---

## Resources

- [Strands Agents Docs](https://strandsagents.com/docs)
- [Skills Concept Guide](https://strandsagents.com/docs/user-guide/concepts/plugins/skills/)
- [strands-agents on PyPI](https://pypi.org/project/strands-agents/)
