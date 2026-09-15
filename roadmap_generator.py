roadmap = {
    "Python": "Revise Python programming and OOP",
    "SQL": "Learn SQL queries and database operations",
    "Machine Learning": "Study ML algorithms and model evaluation",
    "FastAPI": "Learn REST APIs using FastAPI",
    "Docker": "Learn Docker fundamentals and containerization",
    "MLflow": "Learn ML experiment tracking",
    "Power BI": "Learn dashboard creation and data visualization",
    "NLP": "Learn text preprocessing and NLP fundamentals",
    "Transformers": "Study Transformer architecture",
    "Hugging Face": "Practice using Hugging Face models",
    "OpenCV": "Learn image processing using OpenCV",
    "Git": "Practice Git version control",
    "AWS": "Learn basic cloud deployment",
    "LLM": "Learn Large Language Model fundamentals",
    "RAG": "Learn Retrieval-Augmented Generation"
}


def generate_roadmap(missing_skills):

    result = []

    for skill in missing_skills:

        if skill in roadmap:
            result.append(roadmap[skill])

        else:
            result.append(
                f"Learn {skill} fundamentals and build a small project"
            )

    return result