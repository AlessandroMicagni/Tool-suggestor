import streamlit as st
from premai import Prem
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
PREMAI_API_KEY = os.getenv("PREMAI_API_KEY")
PROJECT_ID = 7508  # Replace with your actual numeric Project ID

if not PREMAI_API_KEY:
    st.error("🚨 PREMAI_API_KEY not found in your .env file.")
else:
    client = Prem(api_key=PREMAI_API_KEY)

def fetch_completion(user_message):
    try:
        # Added a system message that instructs the assistant on how to respond
        messages =[
    {
        "role": "user",
        "content": (
            "You are a tool suggestor and builder assistant. "
            "The user will describe a task, and you must first provide a list of off-the-shelf tools that can achieve that task. "
            "If no suitable off-the-shelf tools exist, then provide step-by-step instructions on how to build one.\n\n"
            f"User's task: {user_message.strip()}"
        )
    }
]

        response = client.chat.completions.create(
            project_id=PROJECT_ID,
            messages=messages,
            model="gpt-4o",  # We use gpt-4o as previously confirmed available
            max_tokens=1000,
            temperature=0.7
        )

     
        
        print(response)
        # Return the assistant's content directly
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

st.title("Prem Tool Suggestor & Builder")
st.write("Enter a task, and I’ll suggest off-the-shelf tools to achieve it. If no tools exist, I'll give you instructions on how to build one.")

user_input = st.text_input("Describe your task:", "")
if st.button("Get Response"):
    with st.spinner("Contacting Prem API..."):
        answer = fetch_completion(user_input)
        print(answer)
    if answer.startswith("Error:"):
        st.error(answer)
    else:
        st.success("✅ Response received!")
        st.markdown(answer)

