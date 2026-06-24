from strands import Agent, AgentSkills, Skill

# ---------------------------------------------------------------------------
# Approach 1: Filesystem-based skills
# Each subdirectory under ./skills/ that contains a SKILL.md is auto-loaded.
# ---------------------------------------------------------------------------
filesystem_plugin = AgentSkills(skills="./skills/")

agent = Agent(plugins=[filesystem_plugin])

print("=== Filesystem Skills Demo ===\n")

response = agent("Good morning! How are you today?")
print(response)
print()

response = agent("Can you explain what a plugin system is?")
print(response)
print()

# ---------------------------------------------------------------------------
# Approach 2: Programmatic skill defined inline in code
# Useful for dynamic or environment-specific instructions.
# ---------------------------------------------------------------------------
summarizer_skill = Skill(
    name="summarizer",
    description="Condenses any text into a crisp bullet-point summary, preserving all key facts.",
    instructions=(
        "You are a precise summarizer. When given a block of text:\n"
        "1. Extract the 3-5 most important points.\n"
        "2. Present them as concise bullet points (one line each).\n"
        "3. Add a one-sentence TL;DR at the top.\n"
        "Do not add opinions or information not present in the source text."
    ),
)

programmatic_plugin = AgentSkills(skills=[summarizer_skill])
agent2 = Agent(plugins=[programmatic_plugin])

print("=== Programmatic Skill Demo ===\n")

sample_text = """
Strands is an open-source framework for building AI agents.
It provides a simple Python and TypeScript SDK, built-in tool support,
multi-agent orchestration, and a plugin system for extending agent capabilities.
The Skills plugin implements progressive disclosure — skill metadata loads
upfront, while full instructions are fetched on demand, keeping system prompts lean.
"""

response = agent2(f"Please summarize this for me:\n{sample_text}")
print(response)
