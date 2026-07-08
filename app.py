import streamlit as st
from services.state_manager import init_state, reset_interview

st.set_page_config(page_title="PrimeCrown Interview Prep App", page_icon="🎓", layout="wide")
init_state()

st.title("🎓 PrimeCrown Interview Prep App")
st.caption("AI-powered interview preparation for UK admissions and UKVI credibility.")

with st.sidebar:
    st.header("Session overview")
    profile = st.session_state.get("student_profile", {})
    config = st.session_state.get("interview_config", {})
    st.write(f"**Student:** {profile.get('full_name', 'Not set')}")
    st.write(f"**University:** {profile.get('target_university', 'Not set')}")
    st.write(f"**Course:** {profile.get('target_course', 'Not set')}")
    st.write(f"**Interview type:** {config.get('interview_type', 'Not set')}")
    st.write(f"**Progress:** {st.session_state.get('current_q_index', 0)} / {len(st.session_state.get('questions', []))}")
    if st.button("Reset interview"):
        reset_interview()
        st.rerun()

st.markdown("""
Use the pages in the sidebar to:

1. Capture student profile details.
2. Configure the interview type and difficulty.
3. Run a structured mock interview.
4. Review AI feedback and counselor notes.
5. Track outcomes in the analytics view.
""")

