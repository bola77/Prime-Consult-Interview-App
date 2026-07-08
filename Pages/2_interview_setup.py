import streamlit as st
from services.state_manager import init_state
from services.question_engine import generate_questions

init_state()
st.title("Interview Setup")

if not st.session_state.student_profile:
    st.warning("Complete Student Intake first.")
    st.stop()

with st.form("interview_setup"):
    interview_type = st.selectbox("Interview type", ["Admissions", "UKVI / Credibility", "Scholarship", "Embassy / Visa"])
    difficulty = st.selectbox("Difficulty", ["Easy", "Standard", "Strict"])
    session_length = st.selectbox("Session length", ["15 min", "30 min", "50 min"])
    followups = st.checkbox("Enable follow-up probing", value=True)
    submit = st.form_submit_button("Generate interview")

if submit:
    st.session_state.interview_config = {
        "interview_type": interview_type,
        "difficulty": difficulty,
        "session_length": session_length,
        "followups": followups,
    }
    st.session_state.questions = generate_questions(st.session_state.student_profile, st.session_state.interview_config)
    st.session_state.current_q_index = 0
    st.session_state.responses = []
    st.session_state.scores = []
    st.session_state.risk_flags = []
    st.session_state.session_started = True
    st.session_state.session_completed = False
    st.success(f"Generated {len(st.session_state.questions)} questions.")

if st.session_state.questions:
    st.subheader("Generated questions")
    for q in st.session_state.questions:
        st.write(f"{q['id']}. {q['question']}")

