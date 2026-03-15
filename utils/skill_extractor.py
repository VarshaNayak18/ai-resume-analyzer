import pandas as pd

def extract_skills(resume_text):
    skills = pd.read_csv("data/skills_list.csv", header=None)
    skills_list = skills[0].tolist()

    resume_text = resume_text.lower()

    detected_skills = []

    for skill in skills_list:
        if skill in resume_text:
            detected_skills.append(skill)

    return detected_skills