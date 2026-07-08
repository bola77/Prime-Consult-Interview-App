import streamlit as st
from services.state_manager import init_state

init_state()
st.title("Student Intake")

with st.form("student_intake"):
    full_name = st.text_input("Full name")
    home_country = st.text_input("Home country", value="Nigeria")
    target_university = st.text_input("Target university")
    target_course = st.text_input("Target course")
    academic_background = st.text_area("Academic background")
    english_level = st.selectbox("English confidence", ["High", "Medium", "Needs support"])
    previous_issues = st.text_area("Previous interview or visa issues")
    submit = st.form_submit_button("Save profile")

if submit:
    st.session_state.student_profile = {
        "full_name": full_name,
        "home_country": home_country,
        "target_university": target_university,
        "target_course": target_course,
        "academic_background": academic_background,
        "english_level": english_level,
        "previous_issues": previous_issues,
    }
    st.success("Student profile saved.")

if st.session_state.student_profile:
    st.subheader("Current profile")
    st.json(st.session_state.student_profile)

