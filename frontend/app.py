import streamlit as st
import requests

st.title("ATS Resume Scorer")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if st.button("Get ATS Score"):
    if resume_file and job_desc:
        files = {"resume": resume_file}
        data = {"job_description": job_desc}

        response = requests.post(
            "http://127.0.0.1:5000/score",
            files=files,
            data=data
        )

        result = response.json()

        st.subheader(f"ATS Score: {result['score']}/100")
        st.write("Missing Skills:", result["missing_skills"])
        st.write("Strength:", result["strength"])
        st.write("Suggestion:", result["suggestion"])
    else:
        st.warning("Please upload resume and job description")
