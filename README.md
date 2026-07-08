# PrimeCrown Interview Prep App 🎓

AI-powered university and credibility interview preparation for Prime Crown Consulting.
Built with Streamlit and OpenAI, this app helps students practice structured mock
interviews for UK admissions, UKVI / pre-CAS checks, scholarships, and embassy/visa
credibility assessments.

## ✨ Key features

- **Student intake** – capture profile, target university, course, and background.
- **Interview setup** – configure interview type (Admissions, UKVI / Credibility,
  Scholarship, Embassy / Visa) and difficulty.
- **Structured mock interview** – one-question-at-a-time flow that mirrors real
  panel and UKVI-style interviews.
- **OpenAI-powered questions** – generate university- and course-specific interview
  questions tailored to each student.
- **Rubric-based scoring** – use OpenAI to evaluate relevance, structure, clarity,
  confidence, and overall performance for each answer.
- **Risk flags** – automatically highlight potential credibility issues (e.g.
  weak motivation, vague course fit).
- **Feedback report** – show strengths, improvement areas, risk flags, and score
  tables for counselors and students.
- **Model answers** – generate high-quality example responses for each question to
  use in coaching and workshops.
- **Counselor review** – record readiness decisions, credibility risk level, and
  language-support needs.
- **Simple analytics** – summarize scores by section and track readiness outcomes
  across sessions.

## 🧱 Project structure

```text
primecrown-interview-prep-app/
├── app.py                # main Streamlit entrypoint
├── README.md             # this file
├── requirements.txt      # Python dependencies
├── pages/                # multipage views
│   ├── 1_student_intake.py
│   ├── 2_interview_setup.py
│   ├── 3_live_interview.py
│   ├── 4_feedback_report.py
│   ├── 5_counselor_review.py
│   └── 6_admin_analytics.py
├── services/             # backend logic
│   ├── state_manager.py          # session_state initialization & reset
│   ├── question_engine.py        # OpenAI question generation
│   ├── scoring_engine.py         # OpenAI rubric scoring
│   ├── report_engine.py          # final report assembly
│   ├── model_answer_engine.py    # model answers per question
│   ├── openai_client.py          # shared OpenAI client setup
│   └── storage.py                # JSON export for sessions
├── components/          # reusable UI pieces (progress bars, cards, etc.)
├── prompts/             # prompt text files (optional)
└── data/                # local data (rubrics, exports)
```

This layout follows Streamlit’s recommended file organization for Community
Cloud and generative AI apps.[web:99][web:79]

## 🚀 Getting started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key

Set `OPENAI_API_KEY` via environment or Streamlit secrets:

- Locally (Linux/macOS):

  ```bash
  export OPENAI_API_KEY="sk-..."
  ```

- Streamlit Community Cloud:

  - Go to **App → Settings → Secrets** and add:

    ```toml
    OPENAI_API_KEY = "sk-..."
    ```

OpenAI’s Python API uses `openai.api_key` under the hood, which is set in
`services/openai_client.py`.[web:71][web:67]

### 3. Run the app locally

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

## 🌐 Deploy

### Streamlit Community Cloud

1. Push this project to GitHub (e.g. `bola77/primecrown-interview-prep-app`).
2. On share.streamlit.io, select the repo and set:
   - **Main file path**: `app.py`
   - **Requirements file**: `requirements.txt`
3. Add `OPENAI_API_KEY` under Secrets.
4. Deploy.

Streamlit’s docs confirm that single-app repos with `app.py` at root and a
simple `requirements.txt` are the standard pattern for Community Cloud.[web:99][web:130]

### Railway (or other PaaS)

Use a start command similar to:

```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

and ensure `OPENAI_API_KEY` is set in environment variables.

## 🎯 Intended use

This app is designed for:

- Student recruitment agencies and counselors.
- Prime Crown Consulting staff preparing Nigerian/African students for UK and
  international study interviews.
- Mock UKVI, pre-CAS, scholarship, and embassy interview coaching sessions.
- Group workshops where counselors demonstrate model answers and best-practice
  responses.

It is **not** a visa decision system; it is a preparation and coaching tool to
support better interviews and more confident students.

## 🔮 Roadmap / future ideas

- Integrate Azure OpenAI and Azure Speech for voice-based interviews.
- Add authentication and role-based access (students vs counselors).
- Persist sessions in a relational database (SQLite/PostgreSQL).
- Export student and counselor reports to PDF.
- Add multi-tenant support for partner agencies and university teams.
- Build dashboards across cohorts and intakes for Prime Crown Consulting.

---

Built by Prime Crown Consulting as part of its AI-powered student recruitment
and compliance toolkit.
