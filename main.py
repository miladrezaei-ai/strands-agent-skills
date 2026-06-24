from strands import Agent, AgentSkills

plugin = AgentSkills(skills="./skills/")
agent = Agent(plugins=[plugin])

# --- Skill 1: email-drafter ---
print("\n" + "=" * 60)
print("SKILL: email-drafter")
print("=" * 60)
response = agent("Write an email to my manager asking for this Friday off because I have a family event.")
print(response)

# --- Skill 2: bug-investigator ---
print("\n" + "=" * 60)
print("SKILL: bug-investigator")
print("=" * 60)
response = agent("TypeError: Cannot read properties of undefined (reading 'map') at App.js:42")
print(response)

# --- Skill 3: git-commit-writer ---
print("\n" + "=" * 60)
print("SKILL: git-commit-writer")
print("=" * 60)
response = agent("I fixed the login button that wasn't responding on mobile devices due to a missing touch event handler.")
print(response)
