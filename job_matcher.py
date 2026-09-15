import pandas as pd


def load_job_roles():
    return pd.read_csv("data/job_roles.csv")


def calculate_match(resume_skills, required_skills):
    required = [
        skill.strip().lower()
        for skill in required_skills.split(",")
    ]

    resume = [
        skill.lower()
        for skill in resume_skills
    ]

    matched = []

    for skill in required:
        if skill in resume:
            matched.append(skill)

    if len(required) == 0:
        return 0, matched

    score = (len(matched) / len(required)) * 100

    return round(score, 2), matched


def recommend_roles(resume_skills):
    jobs = load_job_roles()

    results = []

    for _, row in jobs.iterrows():

        score, matched = calculate_match(
            resume_skills,
            row["required_skills"]
        )

        results.append({
            "role": row["role"],
            "score": score,
            "matched": matched
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


def get_missing_skills(resume_skills, required_skills):
    required = [
        skill.strip()
        for skill in required_skills.split(",")
    ]

    resume = [
        skill.lower()
        for skill in resume_skills
    ]

    missing = []

    for skill in required:
        if skill.lower() not in resume:
            missing.append(skill)

    return missing