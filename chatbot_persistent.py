import streamlit as st
import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path='/home/notebooks/storage/.env')

# ---------------------------
# Set your deployment details
# ---------------------------

API_URL = os.getenv("API_URL_Persistent")
API_KEY = os.getenv("API_KEY_Persistent")
DATAROBOT_KEY = os.getenv("DATAROBOT_KEY_Persistent")
DEPLOYMENT_ID = os.getenv("DEPLOYMENT_ID_Persistent")

DEPLOYMENT_URL = API_URL.format(deployment_id=DEPLOYMENT_ID)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "DataRobot-Key": DATAROBOT_KEY
}

# Page setup
st.set_page_config(page_title="Marketing Compliance Advisor", page_icon=":blue_book:", layout="centered")
st.title(":blue_book: Marketing Compliance Advisor")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
# User input
if prompt := st.chat_input("Enter your question here..."):
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})
    
    # Prepare request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "DataRobot-Key": DATAROBOT_KEY,
        "Content-Type": "application/json",
    }
    payload = [
        {"promptText": prompt}
    ]
    try:
        response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            try:
                # Extract prediction
                raw_prediction = result["data"][0]
                prediction = raw_prediction["prediction"]
                prediction = prediction.replace("\\n", "\n").replace("\n\n", "\n")
            except Exception:
                prediction = f":warning: Unexpected response: {result}"
            # Show assistant message
            with st.chat_message("assistant"):
                st.markdown(prediction)
            st.session_state["messages"].append({"role": "assistant", "content": prediction})
        else:
            error_msg = f"Error {response.status_code}: {response.text}"
            with st.chat_message("assistant"):
                st.error(error_msg)
            st.session_state["messages"].append({"role": "assistant", "content": error_msg})
    except Exception as e:
        error_msg = f"Request failed: {str(e)}"
        with st.chat_message("assistant"):
            st.error(error_msg)
        st.session_state["messages"].append({"role": "assistant", "content": error_msg})