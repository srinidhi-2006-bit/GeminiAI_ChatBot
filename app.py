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

    # ✅ EXACT ANSWER SYSTEM PROMPT
    system_prompt = """You are an expert assistant. Answer EXACTLY what is asked. Rules:
- Answer scope: No extra information beyond what's explicitly asked
- Clarify when needed: Ask ONE clarifying question if ambiguous
- Token-conscious: Use concise, single-sentence responses
- Output framing: No greetings, apologies, or prefaces unless requested
- Factual answers: Provide only verifiable facts with sources when possible
- Error handling: Report exact issue briefly with one actionable step
Answer only the query. Nothing more."""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=[system_prompt, user_input],  # ✅ Add system prompt
            generation_config={
                "max_output_tokens": 150,  # ✅ Token limit for concise responses
                "temperature": 0.1  # ✅ Low creativity for factual answers
            }
        )
        bot_reply = response.text
    except Exception:
        bot_reply = "⚠️ API limit reached. Please wait and try again."

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
