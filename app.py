import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Gemini AI ChatBot",
    page_icon="🤖",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Title
st.title("🤖 Gemini AI ChatBot")
st.caption("Chat with Google Gemini using Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=user_input
        )
        bot_reply = response.text
    except Exception:
        bot_reply = "⚠️ API limit reached. Please wait and try again."

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
