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
    ## 🔄 How It Works

1. User uploads a PDF or DOCX resume.
2. Resume text is extracted automatically.
3. Text is cleaned and normalized.
4. Technical skills are detected using a skill dictionary.
5. Extracted skills are compared with job-role requirements.
6. Match scores are calculated for different job roles.
7. Top 3 suitable job roles are recommended.
8. Missing skills are identified for the selected role.
9. A learning roadmap is generated based on the missing skills.

## 🚀 Future Enhancements

- AI-based semantic resume matching
- More job roles and skill datasets
- Resume quality scoring
- Personalized interview question generation
- Advanced NLP-based skill extraction
- Resume improvement suggestions
- Job recommendation using real-time job data

## 📌 Project Highlights

- Automated resume analysis
- Technical skill extraction
- Job-role matching
- Skill-gap analysis
- Personalized learning roadmap
- Interactive Streamlit dashboard

## ⚠️ Responsible AI

Match scores are estimates based on job-related resume content. They should not be used for automatic hiring or rejection decisions. Missing keywords do not necessarily mean missing ability.
## 🚀 Live Demo

Try the AI Resume Analyzer here:

👉 [AI Resume Analyzer - Live Demo](https://navyasriakula181-ai-resume-analyzer-app-jgh1xr.streamlit.app/)

Upload your PDF or DOCX resume to analyze skills, calculate job-role match scores, identify missing skills, and generate a learning roadmap.
