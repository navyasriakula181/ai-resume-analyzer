import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import recommend_roles, get_missing_skills
from roadmap_generator import generate_roadmap


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume to analyze your skills, "
    "find suitable job roles, identify skill gaps, "
    "and generate a learning roadmap."
)


# -----------------------------
# Resume Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# -----------------------------
# Main Processing
# -----------------------------
if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    # Extract text
    text = extract_resume_text(uploaded_file)

    # Check extracted text
    if not text.strip():

        st.error(
            "Could not extract text from this resume. "
            "Please upload a text-based PDF or DOCX file."
        )

        st.stop()

    # Clean text
    cleaned_text = clean_text(text)

    # Extract skills
    skills = extract_skills(cleaned_text)


    # -----------------------------
    # Skills Found
    # -----------------------------
    st.subheader("🛠 Skills Found")

    if skills:

        st.write(", ".join(skills))

    else:

        st.warning(
            "No predefined skills were detected."
        )


    # -----------------------------
    # Job Recommendations
    # -----------------------------
    results = recommend_roles(skills)

    st.subheader("🎯 Recommended Job Roles")


    # Create DataFrame
    result_df = pd.DataFrame(
        [
            {
                "Job Role": result["role"],
                "Match Score (%)": result["score"]
            }
            for result in results
        ]
    )


    # Display table
    st.dataframe(
    result_df,
    width="stretch",
    hide_index=True
)


    # -----------------------------
    # Match Score Chart
    # -----------------------------
    st.subheader("📊 Match Score")

    chart_data = result_df.set_index("Job Role")

    st.bar_chart(chart_data)


    # -----------------------------
    # Top 3 Roles
    # -----------------------------
    st.subheader("🏆 Top 3 Recommended Roles")

    for index, result in enumerate(
        results[:3],
        start=1
    ):

        st.write(
            f"**{index}. {result['role']} — "
            f"{result['score']}%**"
        )


    # -----------------------------
    # Target Role
    # -----------------------------
    st.subheader("🎯 Select Target Role")

    role_names = [
        result["role"]
        for result in results
    ]

    selected_role = st.selectbox(
        "Choose the job role you want to target",
        role_names
    )


    # Find selected role
    jobs = pd.read_csv(
        "data/job_roles.csv"
    )

    role_data = jobs[
        jobs["role"] == selected_role
    ].iloc[0]


    # -----------------------------
    # Selected Role Score
    # -----------------------------
    selected_result = next(
        result for result in results
        if result["role"] == selected_role
    )

    st.metric(
        "Selected Role Match Score",
        f"{selected_result['score']}%"
    )


    # -----------------------------
    # Missing Skills
    # -----------------------------
    missing = get_missing_skills(
        skills,
        role_data["required_skills"]
    )


    st.subheader("❌ Missing Skills")


    if missing:

        for skill in missing:

            st.write(
                f"- {skill}"
            )

    else:

        st.success(
            "Excellent! No major skill gaps detected."
        )


    # -----------------------------
    # Learning Roadmap
    # -----------------------------
    st.subheader("📚 Learning Roadmap")

    roadmap = generate_roadmap(missing)


    if roadmap:

        for week, topic in enumerate(
            roadmap[:4],
            start=1
        ):

            st.write(
                f"**Week {week}:** {topic}"
            )

    else:

        st.success(
            "You already have the required skills "
            "for this role."
        )


# -----------------------------
# Responsible AI Disclaimer
# -----------------------------
st.divider()

st.caption(
    "⚠️ Disclaimer: Match scores are estimates based on "
    "job-related resume content. They should not be used "
    "for automatic hiring or rejection decisions. "
    "Missing keywords do not necessarily mean missing ability."
)