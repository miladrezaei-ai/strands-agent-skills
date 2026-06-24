import streamlit as st
from strands import Agent, AgentSkills

st.set_page_config(page_title="Strands Skills Demo", page_icon="🧠", layout="wide")

# ---------------------------------------------------------------------------
# Sidebar — available skills + quick-trigger buttons
# ---------------------------------------------------------------------------
with st.sidebar:
    st.title("🧠 Strands Skills Demo")
    st.markdown("An agent loaded with **3 skills** — each activates on demand based on your message.")
    st.divider()

    st.markdown("### Available Skills")
    st.markdown("📧 **email-drafter** — writes professional emails")
    st.markdown("🔍 **bug-investigator** — diagnoses errors & stack traces")
    st.markdown("📝 **git-commit-writer** — generates conventional commit messages")
    st.divider()

    st.markdown("### Try an example")
    col1, col2, col3 = st.columns(3)

    email_prompt = "Write an email to my manager asking for this Friday off because I have a family event."
    bug_prompt = "TypeError: Cannot read properties of undefined (reading 'map') at App.js:42"
    git_prompt = "I fixed the login button that wasn't responding on mobile due to a missing touch event handler."

    if col1.button("📧 Email", use_container_width=True):
        st.session_state.quick_prompt = email_prompt
    if col2.button("🔍 Bug", use_container_width=True):
        st.session_state.quick_prompt = bug_prompt
    if col3.button("📝 Commit", use_container_width=True):
        st.session_state.quick_prompt = git_prompt

# ---------------------------------------------------------------------------
# Agent — cached so it's created once per session
# ---------------------------------------------------------------------------
@st.cache_resource
def load_agent():
    plugin = AgentSkills(skills="./skills/")
    return Agent(plugins=[plugin]), plugin

agent, plugin = load_agent()

# ---------------------------------------------------------------------------
# Chat state
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------------------------------
# Main — chat UI
# ---------------------------------------------------------------------------
st.markdown("## Chat")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and "skill" in msg:
            st.caption(f"Skill activated: **{msg['skill']}**")
        st.markdown(msg["content"])

# Handle quick prompt from sidebar buttons
if "quick_prompt" in st.session_state:
    prompt = st.session_state.pop("quick_prompt")
else:
    prompt = st.chat_input("Ask anything — try an email request, a bug, or a code change...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            before = {s.name for s in plugin.get_activated_skills(agent)}
            response = agent(prompt)
            after = {s.name for s in plugin.get_activated_skills(agent)}

        newly_activated = after - before
        skill_label = next(iter(newly_activated)) if newly_activated else "general"

        st.caption(f"Skill activated: **{skill_label}**")
        st.markdown(str(response))

    st.session_state.messages.append({
        "role": "assistant",
        "content": str(response),
        "skill": skill_label,
    })
