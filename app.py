import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    skills = extract_skills(resume_text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✔", skill)