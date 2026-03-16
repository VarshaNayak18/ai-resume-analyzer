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

    resume_skills = extract_skills(resume_text)

    st.subheader("Detected Resume Skills")

    for skill in resume_skills:
        st.write("✔", skill)

    if job_description:

        job_skills = extract_skills(job_description)

        st.subheader("Job Description Skills")
        
        if len(job_skills) == 0:
            st.write("Add JD skills")
        else:
            for skill in job_skills:
                st.write("✔", skill)
        
        matched_skills = [skill for skill in job_skills if skill in resume_skills]
        st.subheader("Matched Skills")
        
        for skill in matched_skills:
            st.write("✔", skill)
            
        st.write(f"{len(matched_skills)} / {len(job_skills)} skills matched")

        score = calculate_similarity(resume_text, job_description)

        st.subheader("Resume Insights")
        
        st.write("Detected Resume Skills:", len(resume_skills))
        st.write("Job Description Skills:", len(job_skills))
        st.write("Matched Skills:", len(matched_skills))

        st.subheader("Resume Match Score")

        st.write(f"{score}% match with job description")
        
        missing_skills = [skill for skill in job_skills if skill not in resume_skills]
        
        st.subheader("Missing Skills")
        
        if len(job_skills) == 0:
            st.write("Add JD skills")
        elif len(missing_skills) == 0:
            st.write("No missing skills detected!")
        else:
            for skill in missing_skills:
                st.write("❌", skill)

        skill_match_score = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

        st.subheader("AI Resume Evaluation")
        
        st.write(f"Overall Match Score: {score}%")
        
        st.subheader("Score Breakdown")
        
        st.write(f"Skill Match Score: {round(skill_match_score,2)}%")
        st.write(f"Keyword Similarity: {score}%")