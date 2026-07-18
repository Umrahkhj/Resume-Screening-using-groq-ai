import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an experienced HR Recruiter.

Analyze the candidate's resume against the job description.

Return your response in the following format:

## Resume Match Score
(Give a percentage out of 100)

## Candidate Information
- Name
- Email
- Phone

## Matching Skills

## Missing Skills

## Education

## Experience

## Projects

## Strengths

## Weaknesses

## Final Recommendation
(Shortlist / Reject with reason)

Job Description:
{job_description}

Resume:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error:\n{e}"