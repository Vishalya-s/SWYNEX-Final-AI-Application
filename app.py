import csv
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SWYNEX AI Career & Skill Gap Analyzer",
    page_icon="🧠",
    layout="centered"
)


# -----------------------------
# Load Career Dataset
# -----------------------------
@st.cache_data
def load_careers():
    careers = []

    with open("data/career_skills.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            skills = [
                skill.strip().lower()
                for skill in row["Skills"].split(",")
            ]

            careers.append({
                "role": row["Role"],
                "skills": skills
            })

    return careers


career_data = load_careers()


# -----------------------------
# Helper Functions
# -----------------------------
def clean_skills(skill_text):
    skills = [
        skill.strip().lower()
        for skill in skill_text.split(",")
        if skill.strip()
    ]

    return list(dict.fromkeys(skills))


def analyze_career(user_skills, required_skills):

    matched_skills = [
        skill for skill in user_skills
        if skill in required_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in user_skills
    ]

    # Skill match percentage
    if required_skills:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    # Simple AI-style similarity
    user_set = set(user_skills)
    required_set = set(required_skills)

    common_skills = len(user_set.intersection(required_set))
    total_unique_skills = len(
        user_set.union(required_set)
    )

    if total_unique_skills:
        similarity_score = (
            common_skills / total_unique_skills
        ) * 100
    else:
        similarity_score = 0

    # Combined intelligent score
    final_score = (
        (match_percentage * 0.7)
        + (similarity_score * 0.3)
    )

    return (
        matched_skills,
        missing_skills,
        final_score
    )


# -----------------------------
# Application
# -----------------------------
st.title("🧠 AI Career & Skill Gap Analyzer")

st.write(
    "Analyze your current skills, identify missing skills, "
    "and discover what to learn for your target career."
)

st.divider()

# -----------------------------
# User Skills
# -----------------------------
st.subheader("👤 Your Skills")

skill_input = st.text_area(
    "Enter your skills separated by commas:",
    placeholder="Example: Python, Pandas, SQL, Git"
)

# -----------------------------
# Career Selection
# -----------------------------
st.subheader("🎯 Target Career")

role_names = [
    career["role"]
    for career in career_data
]

selected_role = st.selectbox(
    "Choose your target role:",
    role_names
)

# -----------------------------
# Analyze
# -----------------------------
if st.button("🚀 Analyze My Career"):

    if not skill_input.strip():

        st.warning(
            "⚠️ Please enter at least one skill."
        )

    else:

        user_skills = clean_skills(skill_input)

        selected_career = next(
            career
            for career in career_data
            if career["role"] == selected_role
        )

        required_skills = selected_career["skills"]

        (
            matched_skills,
            missing_skills,
            final_score
        ) = analyze_career(
            user_skills,
            required_skills
        )

        st.divider()

        # -----------------------------
        # Match Score
        # -----------------------------
        st.subheader("📊 Career Match")

        st.metric(
            "Overall Match",
            f"{final_score:.1f}%"
        )

        st.progress(
            min(final_score / 100, 1.0)
        )

        # -----------------------------
        # Matched Skills
        # -----------------------------
        st.subheader("✅ Matched Skills")

        if matched_skills:

            st.success(
                ", ".join(
                    skill.title()
                    for skill in matched_skills
                )
            )

        else:

            st.info(
                "No matching skills found yet."
            )

        # -----------------------------
        # Missing Skills
        # -----------------------------
        st.subheader("📚 Skills to Learn")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"• {skill.title()}")

        else:

            st.success(
                "🎉 You have all the listed skills for this role!"
            )

        # -----------------------------
        # Learning Roadmap
        # -----------------------------
        st.subheader("🗺️ Recommended Learning Roadmap")

        if missing_skills:

            for index, skill in enumerate(
                missing_skills[:5],
                start=1
            ):

                st.write(
                    f"*Step {index}:* Learn {skill.title()}"
                )

        else:

            st.write(
                "Continue improving your existing skills "
                "through practical projects."
            )

        # -----------------------------
        # Intelligent Recommendation
        # -----------------------------
        st.subheader("🧠 AI Recommendation")

        if final_score >= 80:

            st.success(
                "Strong career match! Focus on advanced "
                "projects and real-world experience."
            )

        elif final_score >= 60:

            st.warning(
                "Good foundation. Strengthen the missing "
                "skills to improve your career readiness."
            )

        else:

            st.info(
                "You are at an early stage for this role. "
                "Follow the recommended roadmap and build "
                "projects to improve your skill match."
            )

        # -----------------------------
        # Method
        # -----------------------------
        st.divider()

        st.subheader("⚙️ How the AI Matching Works")

        st.write(
            "The application compares the user's skills with "
            "the skills required for the selected career. "
            "It calculates a skill-match score and a similarity "
            "score, then combines them into an overall career "
            "match percentage."
        )

        # -----------------------------
        # Limitations
        # -----------------------------
        st.subheader("⚠️ AI Limitations")

        st.write(
            "This tool provides an estimated skill match based "
            "on the available career dataset. It does not measure "
            "actual programming ability, project quality, "
            "professional experience, personality, or current "
            "job-market demand."
        )

        # -----------------------------
        # Ethics
        # -----------------------------
        st.subheader("⚖️ Ethics & Responsible AI")

        st.write(
            "This application should be used only as career "
            "guidance. It should not automatically reject, rank, "
            "or select people for employment. Career decisions "
            "should consider human judgment, individual goals, "
            "experience, and interests."
        )