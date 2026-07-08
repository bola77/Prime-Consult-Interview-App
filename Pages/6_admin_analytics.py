import streamlit as st
import pandas as pd
from services.state_manager import init_state

init_state()
st.title("Admin Analytics")

scores = st.session_state.get("scores", [])
responses = st.session_state.get("responses", [])
review = st.session_state.get("counselor_review", {})

col1, col2, col3 = st.columns(3)
col1.metric("Responses", len(responses))
col2.metric("Scores logged", len(scores))
col3.metric("Readiness", review.get("readiness", "N/A"))

if scores:
    df = pd.DataFrame(scores)
    st.subheader("Scores by section")
    st.dataframe(df.groupby("section")[["relevance", "structure", "clarity", "confidence", "overall"]].mean().round(2), use_container_width=True)
    st.line_chart(df[["overall"]])
else:
    st.info("Complete at least one interview to populate analytics.")

