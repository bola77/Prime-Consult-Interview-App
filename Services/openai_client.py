# services/openai_client.py
import os
import openai
import streamlit as st

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment or st.secrets.")
    openai.api_key = api_key
    return openai

