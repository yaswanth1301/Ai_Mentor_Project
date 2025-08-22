"""from fastapi import FastAPI
from transformers import pipeline

# Initialize app
app = FastAPI()

# Load a pre-trained model
chatbot = pipeline("text-generation", model="gpt2")

@app.get("/")
def home():
    return {"message": "AI Mentor Backend Running 🚀"}

@app.get("/ask")
def ask(query: str):
    response = chatbot(query, max_length=50, num_return_sequences=1)
    return {"query": query, "response": response[0]['generated_text']}

@app.get("/suggest_project")
def suggest_project(skill: str, domain: str):
    prompt = f"Suggest a practical project idea for a {skill} level student in the {domain} domain."
    response = chatbot(prompt, max_length=60, num_return_sequences=1)
    return {"skill": skill, "domain": domain, "suggestion": response[0]['generated_text']}

# NEW: Roadmap Generator
@app.get("/roadmap")
def roadmap(project: str):
    prompt = f"Generate a step-by-step roadmap for completing the project: {project}. Break it into clear milestones."
    response = chatbot(prompt, max_length=120, num_return_sequences=1)
    return {"project": project, "roadmap": response[0]['generated_text']}
"""

from fastapi import FastAPI
from transformers import pipeline

# Initialize app
app = FastAPI()

# Load a pre-trained model
chatbot = pipeline("text-generation", model="gpt2")

@app.get("/")
def home():
    return {"message": "AI Mentor Backend Running 🚀"}

@app.get("/ask")
def ask(query: str):
    response = chatbot(query, max_length=50, num_return_sequences=1)
    return {"query": query, "response": response[0]['generated_text']}

@app.get("/suggest_project")
def suggest_project(skill: str, domain: str):
    prompt = f"Suggest a practical project idea for a {skill} level student in the {domain} domain."
    response = chatbot(prompt, max_length=60, num_return_sequences=1)
    return {"skill": skill, "domain": domain, "suggestion": response[0]['generated_text']}

@app.get("/roadmap")
def roadmap(project: str):
    prompt = f"Generate a step-by-step roadmap for completing the project: {project}. Break it into clear milestones."
    response = chatbot(prompt, max_length=120, num_return_sequences=1)
    return {"project": project, "roadmap": response[0]['generated_text']}

# NEW: Debugging Assistant
@app.get("/debug")
def debug(code_error: str):
    prompt = f"Explain this error and suggest a fix:\n{code_error}"
    response = chatbot(prompt, max_length=120, num_return_sequences=1)
    return {"error": code_error, "advice": response[0]['generated_text']}
