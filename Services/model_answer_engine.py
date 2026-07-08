import json
from services.openai_client import get_openai_client

SYSTEM_PROMPT = """
You are an expert international admissions and UKVI interview trainer.
For each question, write a concise, high-quality model answer.

Requirements:
- 3–6 sentences.
- Clear structure (motivation, background, course fit, future plans where relevant).
- Honest tone suitable for a genuine student.
- No invented personal details (use only what is provided in the profile).
- Avoid sounding robotic or memorized.
"""

def generate_model_answer(profile, question_obj, student_answer=None):
    openai = get_openai_client()
    question_text = question_obj["question"]

    context = {
        "student_profile": {
            "full_name": profile.get("full_name"),
            "home_country": profile.get("home_country"),
            "target_university": profile.get("target_university"),
            "target_course": profile.get("target_course"),
            "academic_background": profile.get("academic_background"),
            "english_level": profile.get("english_level"),
        },
        "question": question_text,
        "section": question_obj.get("section"),
        "student_answer": student_answer,
    }

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Use the following JSON context to write ONE model answer.\n"
                "Respond with plain text only, no JSON or bullet list.\n\n"
                + json.dumps(context)
            ),
        },
    ]

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.5,
    )

    return resp.choices[^0].message["content"]

