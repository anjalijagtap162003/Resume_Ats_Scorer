from flask import Flask, request, jsonify
from ats_logic import (
    extract_text_from_pdf,
    calculate_ats_score,
    find_missing_skills
)


app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score_resume():
    resume = request.files['resume']
    job_desc = request.form['job_description']

    resume_text = extract_text_from_pdf(resume)

    score, job_skills = calculate_ats_score(resume_text, job_desc)
    missing = find_missing_skills(resume_text, job_skills)

    return jsonify({
        "score": score,
        "job_skills_detected": job_skills,
        "missing_skills": missing,
        "strength": "Good match" if score >= 70 else "Needs improvement",
        "suggestion": "Add missing job-required skills to resume"
    })

if __name__ == "__main__":
    app.run(debug=True)
