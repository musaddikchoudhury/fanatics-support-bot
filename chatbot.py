import google.generativeai as genai
from knowledge_base import load_knowledge_base
from dotenv import load_dotenv
import os

# 1. Load the secret key from your .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Load the Fanatics data from your text files
FANATICS_DATA = load_knowledge_base()

# 3. Initialize the model (Updated for 2026)
model = genai.GenerativeModel('gemini-3-flash-preview')

def get_response(chat_history):
    # Prepare the context for the AI
    # This instructs the AI to use your specific Fanatics data
    context = f"""
    You are an expert AI Support Assistant for Fanatics. 
    Use the following Knowledge Base to answer questions accurately. 
    If the answer isn't here, refer them to customerfirst@fanatics.com.
    
    KNOWLEDGE BASE:
    {FANATICS_DATA}
    """
    
    # Format history for Gemini
    contents = [{"role": "user", "parts": [context]}]
    for msg in chat_history:
        role = "model" if msg["role"] == "assistant" else "user"
        contents.append({"role": role, "parts": [msg["content"]]})
    
    # Generate the response
    response = model.generate_content(contents)
    return response.text