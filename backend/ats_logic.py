import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() + " "
    return text.lower()

def extract_skills_from_jd(job_text):
    possible_skills = [
        'python', 'java', 'c', 'c++', 'html', 'css', 'bootstrap',
        'javascript', 'react', 'angular', 'node', 'express',
        'sql', 'mysql', 'mongodb', 'postgresql',
        'machine learning', 'data analysis', 'nlp',
        'git', 'github', 'docker', 'aws', 'flask', 'django'
    ]

    found_skills = []
    job_text = job_text.lower()

    for skill in possible_skills:
        if skill in job_text:
            found_skills.append(skill)

    return found_skills


def skill_match_score(resume_text, job_skills):
    if not job_skills:
        return 0

    matched = 0
    for skill in job_skills:
        if skill in resume_text:
            matched += 1

    return matched / len(job_skills)


def text_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_text])
    return cosine_similarity(vectors[0], vectors[1])[0][0]


def calculate_ats_score(resume_text, job_text):
    job_skills = extract_skills_from_jd(job_text)

    skill_score = skill_match_score(resume_text, job_skills)
    similarity_score = text_similarity(resume_text, job_text)

    final_score = (0.75 * skill_score + 0.25 * similarity_score) * 100

    return round(final_score, 2), job_skills

def find_missing_skills(resume_text, job_skills):
    return [skill for skill in job_skills if skill not in resume_text]
