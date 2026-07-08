import streamlit as st

DEFAULTS = {
    "student_profile": {},
    "interview_config": {},
    "questions": [],
    "current_q_index": 0,
    "responses": [],
    "scores": [],
    "risk_flags": [],
    "final_report": None,
    "session_started": False,
    "session_completed": False,
    "counselor_review": {},
    "analytics_events": [],
}

def init_state():
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_interview():
    keep_profile = st.session_state.get("student_profile", {})
    for key, value in DEFAULTS.items():
        if isinstance(value, dict):
            st.session_state[key] = value.copy()
        elif isinstance(value, list):
            st.session_state[key] = list(value)
        else:
            st.session_state[key] = value
    st.session_state["student_profile"] = keep_profile

