from datetime import datetime
import json
from services.openai_client import get_openai_client

def build_interview_blueprint(profile, config):
    interview_type = config.get("interview_type", "Admissions")
    if interview_type == "UKVI / Credibility":
        sections = ["motivation", "course_fit", "career_goals", "financial", "credibility"]
    elif interview_type == "Scholarship":
        sections = ["motivation", "course_fit", "career_goals"]
    else:
        sections = ["motivation", "course_fit", "career_goals", "credibility"]

    return {
        "created_at": datetime.utcnow().isoformat(),
        "sections": sections,
        "university": profile.get("target_university", "Target University"),
        "course": profile.get("target_course", "Chosen Course"),
        "country": profile.get("home_country", "Home Country"),
        "difficulty": config.get("difficulty", "Standard"),
    }

def generate_questions(profile, config):
    blueprint = build_interview_blueprint(profile, config)
    openai = get_openai_client()

    system_msg = (
        "You are an expert international admissions and UKVI interview officer. "
        "Generate concise, realistic interview questions for a mock session."
    )

    user_msg = f"""
Generate interview questions as a JSON list. Each item must have:
- id (integer)
- section (one of {blueprint['sections']})
- question (string)
- difficulty (string)

Context:
- Interview type: {config.get('interview_type')}
- University: {blueprint['university']}
- Course: {blueprint['course']}
- Student home country: {blueprint['country']}
- Difficulty level: {blueprint['difficulty']}

Rules:
- 2 questions for motivation
- 2 for course_fit
- 2 for career_goals
- 1 for financial (if present)
- 2 for credibility (if present)
- Use clear, conversational English.
- Make questions realistic for university/UKVI-style interviews.
Return ONLY valid JSON, no explanation text.
"""

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.4,
    )
    content = resp.choices[^0].message["content"]

    try:
        questions = json.loads(content)
    except json.JSONDecodeError:
        questions = _fallback_questions(blueprint)

    return questions

def _fallback_questions(blueprint):
    sections = blueprint["sections"]
    questions = []
    qid = 1
    for sec in sections:
        for n in range(2):
            questions.append({
                "id": qid,
                "section": sec,
                "question": f"Fallback question {n+1} about {sec} for {blueprint['course']} at {blueprint['university']}.",
                "difficulty": blueprint["difficulty"],
            })
            qid += 1
    return questions

