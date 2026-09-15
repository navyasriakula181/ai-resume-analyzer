# 📄 AI Resume Analyzer & Job Recommendation System

An AI-based web application that analyzes resumes, extracts skills, recommends suitable job roles, identifies missing skills, and generates a learning roadmap.

## 🚀 Features

- Upload PDF and DOCX resumes
- Extract resume text automatically
- Detect technical skills
- Calculate job-role match scores
- Recommend Top 3 suitable job roles
- Identify missing skills
- Generate a personalized learning roadmap
- Interactive Streamlit dashboard
- Responsible AI disclaimer

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- PyPDF
- python-docx

## 📂 Project Structure

```text
ai_resume_analyzer/
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
└── data/
    ├── job_roles.csv
    └── skill_dictionary.csv