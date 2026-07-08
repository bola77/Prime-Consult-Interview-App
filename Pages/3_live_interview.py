import streamlit as st
from services.state_manager import init_state
from services.scoring_engine import score_response

init_state()
st.title("Live Interview")

questions = st.session_state.questions
if not questions:
    st.warning("Generate an interview first.")
    st.stop()

idx = st.session_state.current_q_index
if idx >= len(questions):
    st.success("Interview completed. Move to Feedback Report.")
    st.session_state.session_completed = True
    st.stop()

q = questions[idx]
st.progress((idx) / len(questions))
st.subheader(f"Question {idx + 1} of {len(questions)}")
st.write(q["question"])

answer = st.text_area("Student response", key=f"answer_{idx}", height=200)

col1, col2 = st.columns(2)
with col1:
    if st.button("Submit answer"):
        score = score_response(q, answer)
        st.session_state.responses.append({"question_id": q["id"], "question": q["question"], "answer": answer})
        st.session_state.scores.append(score)
        st.session_state.risk_flags.extend(score.get("risk_flags", []))
        st.session_state.current_q_index += 1
        st.rerun()
with col2:
    if st.button("Skip question"):
        st.session_state.responses.append({"question_id": q["id"], "question": q["question"], "answer": ""})
        st.session_state.scores.append(score_response(q, ""))
        st.session_state.current_q_index += 1
        st.rerun()

