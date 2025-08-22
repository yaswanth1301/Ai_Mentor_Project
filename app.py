import streamlit as st
from transformers import pipeline

# Load AI model
chatbot = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="AI Mentor for Practical Skills", page_icon="🤖")
st.title("🤖 AI Mentor for Practical Skills")
st.write("Your personal AI mentor for project guidance and debugging!")

# --- Chat Mentor ---
st.header("💬 Chat with AI Mentor")
user_input = st.text_input("Ask me anything (project ideas, debugging help, etc.)")

if st.button("Ask Mentor"):
    if user_input.strip() != "":
        response = chatbot(user_input, max_length=60, num_return_sequences=1)
        st.success(response[0]['generated_text'])

# --- Project Suggestion Engine ---
st.header("📂 Project Suggestion Engine")
skill = st.selectbox("Select your skill level", ["Beginner", "Intermediate", "Advanced"])
domain = st.text_input("Enter your domain of interest (AI, Web Dev, Blockchain, etc.)")

if st.button("Suggest Project"):
    if domain.strip() != "":
        prompt = f"Suggest a practical project idea for a {skill} level student in the {domain} domain."
        response = chatbot(prompt, max_length=80, num_return_sequences=1)
        st.info(f"Suggested Project: {response[0]['generated_text']}")

# --- Roadmap Generator ---
st.header("🛣️ Roadmap Generator")
project_idea = st.text_input("Enter your project idea to generate a roadmap")

if st.button("Generate Roadmap"):
    if project_idea.strip() != "":
        prompt = f"Generate a step-by-step roadmap for completing the project: {project_idea}. Break it into milestones."
        response = chatbot(prompt, max_length=120, num_return_sequences=1)
        st.success(f"📌 Roadmap:\n\n{response[0]['generated_text']}")

# --- Debugging Assistant ---
st.header("🐞 Debugging Assistant")
code_error = st.text_area("Paste your code error message or buggy code here:")

if st.button("Debug My Code"):
    if code_error.strip() != "":
        prompt = f"Explain this error and suggest a fix:\n{code_error}"
        response = chatbot(prompt, max_length=120, num_return_sequences=1)
        st.warning(f"🔍 Mentor's Debugging Advice:\n\n{response[0]['generated_text']}")

# --- About Section ---
st.sidebar.title("ℹ️ About This Project")
st.sidebar.info(
    "This AI Mentor helps students bridge theory and practice.\n\n"
    "Features:\n"
    "- Chat Mentor 💬\n"
    "- Project Suggestions 📂\n"
    "- Roadmap Generator 🛣️\n"
    "- Debugging Assistant 🐞\n\n"
    "Developed by Luke 🚀"
)
