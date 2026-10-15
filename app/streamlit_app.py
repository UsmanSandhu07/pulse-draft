import streamlit as st
from src.agent import initialize_agent

st.title("Pulse Draft")

with st.sidebar:
    api_key = st.text_input("Groq API Key", type="password")

topic = st.text_input("What is your post topic?")

if st.button("Draft post"):
    if not api_key:
        st.error("Please provide an API key!")
    else:
        agent = initialize_agent(api_key)
        with st.spinner("Analyzing trends..."):
            response = agent.invoke({"input": f"Draft a professional-network post about {topic}"})
            st.markdown(response["output"])
