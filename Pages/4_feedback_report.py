import streamlit as st
import pandas as pd
from services.state_manager import init_state
from services.report_engine import build_final_report
from services.storage import save_session
from services.model_answer_engine import generate_model_answer

init_state()
st.title("Feedback Report")

if not st.session_state.responses:
    st.warning("No completed responses yet.")
    st.stop()

report = build_final_report(
    st.session_state.student_profile,
    st.session_state.interview_config,
    st.session_state.questions,
    st.session_state.responses,
    st.session_state.scores,
)
st.session_state.final_report = report

if report:
    st.metric("Overall score", report["overall_score"])
    st.write(f"**Student:** {report['student']}")
    st.write(f"**Interview type:** {report['interview_type']}")
    st.subheader("Coach summary")
    st.write(report.get("coach_summary", "No summary available."))

    st.subheader("Risk flags")
    for item in report["risk_flags"] or ["No major flags detected."]:
        st.write(f"- {item}")

    st.subheader("Question scores")
    df = pd.DataFrame(st.session_state.scores)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("question_id")[["overall"]])

    if st.button("Save session export"):
        save_session({
            "profile": st.session_state.student_profile,
            "config": st.session_state.interview_config,
            "responses": st.session_state.responses,
            "scores": st.session_state.scores,
            "report": report,
        })
        st.success("Session exported to data/session_exports.json")

st.subheader("Model answers (AI examples)")

questions = st.session_state.questions
responses = st.session_state.responses

if not questions or not responses:
    st.info("Complete an interview to see AI model answers.")
else:
    q_options = {f"Q{q['id']} – {q['question'][:60]}...": q for q in questions}
    selected_label = st.selectbox("Choose a question", list(q_options.keys()))
    selected_question = q_options[selected_label]

    answer_dict = next(
        (r for r in responses if r["question_id"] == selected_question["id"]),
        None,
    )
    student_answer = answer_dict["answer"] if answer_dict else ""

    if st.button("Generate model answer"):
        with st.spinner("Generating model answer..."):
            model_answer = generate_model_answer(
                st.session_state.student_profile,
                selected_question,
                student_answer=student_answer,
            )
        st.markdown("**AI model answer example:**")
        st.write(model_answer)

