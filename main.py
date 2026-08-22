import os
import streamlit as st
import google.generativeai as genai
from groq import Groq

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="EstateMind AI",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Fetch API Keys directly from Render Environment Variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Initialize API clients if keys are present
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# 3. Main Interface Header
st.title("🏢 EstateMind AI")
st.caption("Dual-Engine Real Estate AI Agent Portal")

# Sidebar for Document Uploads (Agency Portal)
with st.sidebar:
    st.header("Agency Portal")
    uploaded_file = st.file_uploader("Upload Property Brochure (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("Document uploaded successfully!")

# 4. Chat Interface
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome to EstateMind AI! How can I assist with your property queries today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about listings, pricing, or floor plans..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Response generation logic using Groq or Gemini
    if GROQ_API_KEY:
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            bot_reply = response.choices[0].message.content
        except Exception as e:
            bot_reply = f"Error generating response: {str(e)}"
    else:
        bot_reply = "GROQ_API_KEY is missing. Please add it to your Render Environment settings."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)













