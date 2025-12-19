
ATS Resume Scorer
=================

This project is an ATS (Applicant Tracking System) Resume Scorer that evaluates how well a resume matches a given job description. 
It extracts text from a PDF resume, analyzes job description skills, calculates similarity, and returns an ATS score with suggestions.


TECH STACK
--------------------------------------
• Python
• Flask  (Backend API)
• Streamlit (Frontend UI)
• Scikit-learn (TF-IDF similarity)
• PyPDF2 (PDF text extraction)


PROJECT STRUCTURE
---------------------------------------------------
ats_logic.py    → Core ATS logic (skills + scoring)
app.py (Flask)  → Backend API to process resume & JD
app.py (Streamlit) → Frontend UI calling Flask API



INSTALLATION & SETUP
--------------------------------------

1️. Install Dependencies :
pip install flask streamlit PyPDF2 scikit-learn requests

2️. Run Flask Backend :
python app.py

Flask will start at:
http://localhost:8501

3️. Run Streamlit Frontend :
streamlit run app.py

Streamlit UI will open in browser.



API ENDPOINT
--------------------------------------
POST  /score

Form Data:
resume  → PDF file upload
job_description → text

Response Example:
{
 "score": 82.5,
 "job_skills_detected": ["python","sql"],
 "missing_skills": ["django"],
 "strength": "Good match",
 "suggestion": "Add missing job-required skills to resume"
}

