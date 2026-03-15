import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    skills = extract_skills(resume_text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✔", skill)

    if job_description:

        score = calculate_similarity(resume_text, job_description)

        st.subheader("Resume Match Score")

        st.write(f"{score}% match with job description")