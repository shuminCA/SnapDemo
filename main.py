from typing import Set
from backend import run_llm, add_url
import streamlit as st
from streamlit_chat import message
import datetime

st.header("SnapLogic LLM Bot Demo - EmbedChain")
wiki = st.text_input("Wiki Link", placeholder="Enter your wiki link here..")
prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if wiki:
    with st.spinner("Adding link..."):
        add_url(wiki)

if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(query=prompt)
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(generated_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True, key=f"{datetime.datetime.now()}")
        message(generated_response, key=f"{datetime.datetime.now()}")