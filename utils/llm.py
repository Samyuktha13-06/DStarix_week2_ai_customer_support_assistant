import os
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env. Please add GROQ_API_KEY to your .env file.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0.3,
)