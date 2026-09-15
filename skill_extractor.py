import pandas as pd


def load_skills():
    return pd.read_csv("data/skill_dictionary.csv")


def extract_skills(text):
    skills_df = load_skills()

    found_skills = []

    for skill in skills_df["skill"]:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills