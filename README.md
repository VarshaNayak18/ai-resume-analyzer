# AI Resume Analyzer

An AI-powered web application that analyzes resumes and compares them with job descriptions to evaluate candidate suitability. The system extracts skills from resumes, identifies required skills in job descriptions, and calculates a match score using Natural Language Processing techniques.

## Features

* Extracts text from PDF resumes
* Detects technical skills using NLP
* Identifies skills mentioned in job descriptions
* Calculates resume–job similarity using cosine similarity
* Shows matched and missing skills
* Displays resume insights and score breakdown
* Provides AI-based feedback for resume improvement
* Interactive web interface built with Streamlit

## Tech Stack

**Language**

* Python

**Libraries**

* Streamlit
* scikit-learn
* pandas
* PyPDF2

**Concepts Used**

* Natural Language Processing (NLP)
* Cosine Similarity
* Skill Extraction
* Resume Matching Algorithms

## Project Structure

```
ai-resume-analyzer
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── data
│   └── skills_list.csv
│
├── sample_resumes
│   └── resume1.pdf
│
├── utils
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── similarity.py
│
└── images
```

## How It Works

1. Upload a resume in PDF format.
2. The system extracts text from the resume.
3. NLP techniques detect technical skills from the resume.
4. The job description is analyzed to identify required skills.
5. Cosine similarity calculates how well the resume matches the job description.
6. The system displays:

   * Resume Match Score
   * Resume Skills
   * Job Description Skills
   * Missing Skills
   * AI Evaluation Breakdown

## How to Run the Project

1. Clone the repository

```
   git clone https://github.com/VarshaNayak18/ai-resume-analyzer.git
```

2. Navigate to the project folder

```
   cd ai-resume-analyzer
```

3. Install dependencies

```
   pip install -r requirements.txt
```

4. Run the application

```
   streamlit run app.py
```

## Future Improvements

* Improve skill extraction using advanced NLP models
* Add support for multiple resume formats
* Add job role recommendations
* Implement deep learning based resume analysis