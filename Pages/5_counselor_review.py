import streamlit as st
from services.state_manager import init_state
from services.model_answer_engine import generate_model_answer

init_state()
st.title("Counselor Review")

if not st.session_state.responses:
    st.warning("No interview data available yet.")
    st.stop()

with st.form("counselor_review"):
    readiness = st.selectbox("Readiness decision", ["Ready", "Needs another practice", "Escalate for counselor intervention"])
    credibility_risk = st.selectbox("Credibility risk", ["Low", "Medium", "High"])
    language_support = st.selectbox("Language support need", ["Low", "Medium", "High"])
    notes = st.text_area("Counselor notes")
    submit = st.form_submit_button("Save review")

if submit:
    st.session_state.counselor_review = {
        "readiness": readiness,
        "credibility_risk": credibility_risk,
        "language_support": language_support,
        "notes": notes,
    }
    st.success("Counselor review saved.")

if st.session_state.counselor_review:
    st.subheader("Current review")
    st.json(st.session_state.counselor_review)

st.subheader("Model answers for counselor reference")

questions = st.session_state.questions
responses = st.session_state.responses

if questions and responses:
    for q in questions:
        st.markdown(f"**Q{q['id']}: {q['question']}**")
        answer_dict = next(
            (r for r in responses if r["question_id"] == q["id"]),
            None,
        )
        student_answer = answer_dict["answer"] if answer_dict else ""

        if st.button(f"Show model answer for Q{q['id']}", key=f"model_{q['id']}"):
            with st.spinner("Generating model answer..."):
                model_answer = generate_model_answer(
                    st.session_state.student_profile,
                    q,
                    student_answer=student_answer,
                )
            st.markdown("_AI model answer:_")
            st.write(model_answer)
else:
    st.info("No questions/responses found for this session.")

