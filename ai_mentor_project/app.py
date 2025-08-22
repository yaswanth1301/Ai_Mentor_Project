"""import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Mentor for Practical Skills", page_icon="🤖")
st.title("🤖 AI Mentor for Practical Skills")

# --- Chat Mentor ---
st.header("💬 Chat with AI Mentor")
user_input = st.text_input("Ask me anything (project ideas, debugging help, etc.)")

if st.button("Ask Mentor"):
    if user_input.strip() != "":
        response = requests.get(f"{API_URL}/ask", params={"query": user_input})
        if response.status_code == 200:
            mentor_reply = response.json()["response"]
            st.success(mentor_reply)

# --- Project Suggestion Engine ---
st.header("📂 Project Suggestion Engine")
skill = st.selectbox("Select your skill level", ["Beginner", "Intermediate", "Advanced"])
domain = st.text_input("Enter your domain of interest (AI, Web Dev, Blockchain, etc.)")

if st.button("Suggest Project"):
    if domain.strip() != "":
        response = requests.get(f"{API_URL}/suggest_project", params={"skill": skill, "domain": domain})
        if response.status_code == 200:
            suggestion = response.json()["suggestion"]
            st.info(f"Suggested Project: {suggestion}")

# --- Roadmap Generator ---
st.header("🛣️ Roadmap Generator")
project_idea = st.text_input("Enter your project idea to generate a roadmap")

if st.button("Generate Roadmap"):
    if project_idea.strip() != "":
        response = requests.get(f"{API_URL}/roadmap", params={"project": project_idea})
        if response.status_code == 200:
            roadmap = response.json()["roadmap"]
            st.success(f"📌 Roadmap for {project_idea}:\n\n{roadmap}")
"""

import streamlit as st
import numpy as np
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Mentor for Practical Skills", page_icon="🤖")
st.title("🤖 AI Mentor for Practical Skills")

# --- Chat Mentor ---
st.header("💬 Chat with AI Mentor")
user_input = st.text_input("Ask me anything (project ideas, debugging help, etc.)")

if st.button("Ask Mentor"):
    if user_input.strip() != "":
        response = requests.get(f"{API_URL}/ask", params={"query": user_input})
        if response.status_code == 200:
            mentor_reply = response.json()["response"]
            st.success(mentor_reply)

# --- Project Suggestion Engine ---
st.header("📂 Project Suggestion Engine")
skill = st.selectbox("Select your skill level", ["Beginner", "Intermediate", "Advanced"])
domain = st.text_input("Enter your domain of interest (AI, Web Dev, Blockchain, etc.)")

if st.button("Suggest Project"):
    if domain.strip() != "":
        response = requests.get(f"{API_URL}/suggest_project", params={"skill": skill, "domain": domain})
        if response.status_code == 200:
            suggestion = response.json()["suggestion"]
            st.info(f"Suggested Project: {suggestion}")

# --- Roadmap Generator ---
st.header("🛣️ Roadmap Generator")
project_idea = st.text_input("Enter your project idea to generate a roadmap")

if st.button("Generate Roadmap"):
    if project_idea.strip() != "":
        response = requests.get(f"{API_URL}/roadmap", params={"project": project_idea})
        if response.status_code == 200:
            roadmap = response.json()["roadmap"]
            st.success(f"📌 Roadmap for {project_idea}:\n\n{roadmap}")

# --- Debugging Assistant ---
st.header("🐞 Debugging Assistant")
code_error = st.text_area("Paste your code error message or buggy code here:")

if st.button("Debug My Code"):
    if code_error.strip() != "":
        response = requests.get(f"{API_URL}/debug", params={"code_error": code_error})
        if response.status_code == 200:
            advice = response.json()["advice"]
            st.warning(f"🔍 Mentor's Debugging Advice:\n\n{advice}")
