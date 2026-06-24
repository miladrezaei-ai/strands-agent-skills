import logging
from strands import Agent, AgentSkills, Skill

# Enables Strands debug log level
# logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
# logging.basicConfig(
#     format="%(levelname)s | %(name)s | %(message)s",
#     handlers=[logging.StreamHandler()]
# )

plugin = AgentSkills(skills="./skills/morning")

agent = Agent(plugins=[plugin])

result = agent("Good morning, how is your day")
print(result)
print("----------")
# print(result.metrics.get_summary())