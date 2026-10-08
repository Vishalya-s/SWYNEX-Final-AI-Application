🧠 SWYNEX Final AI Application — Career & Skill Gap Analyzer

An intelligent career guidance application that compares a user's current skills with the skills required for a selected career role. It identifies skill gaps, calculates an estimated career match score, and provides a personalized learning roadmap.

🎯 Problem Statement

Students and beginners often have difficulty understanding which skills they need for a specific career. They may know some programming or technical skills but may not know what important skills are still missing.

This application helps users understand their current skill level for a selected career and provides clear guidance on what to learn next.

💡 Solution

The AI Career & Skill Gap Analyzer allows users to:

• Enter their existing technical skills
• Select a target career
• Calculate an estimated career match percentage
• Identify matched skills
• Identify missing skills
• Generate a recommended learning roadmap
• Receive an intelligent career-readiness recommendation

✨ Key Features

👤 Skill Input

Users can enter multiple skills separated by commas.

Example:

"Python, Pandas, SQL, Git"

🎯 Career Selection

Users can select from different career roles, including:

• AI/ML Engineer
• Data Scientist
• Data Analyst
• Software Developer
• Web Developer
• Python Developer

📊 Career Match Score

The application calculates an estimated match percentage based on the user's skills and the skills required for the selected career.

✅ Matched Skills

The application identifies skills that the user already has.

📚 Skill Gap Detection

The application identifies important skills that are missing for the selected career.

🗺️ Learning Roadmap

The missing skills are converted into a simple step-by-step learning roadmap.

🧠 Intelligent Recommendation

The application provides career-readiness guidance based on the calculated match score.

⚙️ How the Intelligent Matching Works

The application uses a lightweight skill-matching approach.

1. User skills are collected and cleaned.
2. The selected career's required skills are loaded from the career dataset.
3. User skills are compared with the required skills.
4. Matching skills are identified.
5. Missing skills are identified.
6. A skill-match percentage is calculated.
7. A similarity score is calculated using the overlap between the two skill sets.
8. The scores are combined into an overall career match percentage.
9. The application provides a learning roadmap and recommendation.

This is an intelligent rule-based skill matching system rather than a trained machine-learning model.

🧪 Example Result

User Skills

"Python, Pandas, SQL, Git"

Target Career

Data Scientist

Result

• Overall Match: 36.2%
• Matched Skills: Python, Pandas, SQL
• Skills to Learn: Statistics, NumPy, Scikit-learn, Matplotlib, Machine Learning

Recommended Roadmap

1. Learn Statistics
2. Learn NumPy
3. Learn Scikit-learn
4. Learn Matplotlib
5. Learn Machine Learning

The application also provides an intelligent recommendation encouraging the user to follow the roadmap and build practical projects.

🛠️ Technologies Used

v Python
• Streamlit
• CSV
• Git & GitHub

📁 Project Structure

SWYNEX-Final-AI-Application/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
    └── career_skills.csv

▶️ How to Run

1. Clone the repository

git clone https://github.com/Vishalya-s/SWYNEX-Final-AI-Application.git

2. Open the project

cd SWYNEX-Final-AI-Application

3. Create a virtual environment

python -m venv swynex_env

4. Activate the environment

Windows PowerShell:

.\swynex_env\Scripts\Activate.ps1

5. Install dependencies

python -m pip install -r requirements.txt

6. Run the application

python -m streamlit run app.py

The application will open in the browser.

⚠️ AI Limitations

The application provides an estimated skill match based on the available career dataset.

It does not measure:

• Actual programming ability
• Project quality
• Professional experience
• Personality
• Communication skills
• Current job-market demand
• Depth of knowledge in a particular skill

The match percentage should therefore be treated as guidance rather than an absolute assessment.

⚖️ Ethics & Responsible AI

This application is designed for educational and career guidance purposes.

It should not be used to automatically:

• Reject candidates
• Rank candidates
• Select employees
• Make hiring decisions

Career decisions should consider human judgment, individual goals, experience, interests, and other relevant factors.

The system should be treated as a supportive tool rather than a replacement for human decision-making.

🎓 What I Learned

Through this project, I learned how to:

• Build a complete beginner-friendly AI-style application
• Process structured career and skill data
• Compare user skills with career requirements
• Calculate an interpretable match score
• Identify skill gaps
• Generate a learning roadmap
• Build an interactive Streamlit interface
• Document AI limitations
• Consider ethics and responsible AI
• Package an AI application for GitHub

🚀 Future Improvements

Possible future improvements include:

• Adding more career roles
• Adding more technical and soft skills
• Using a larger career dataset
• Adding personalized course recommendations
• Adding resume-based skill extraction
• Using a trained machine-learning model
• Adding visualization of skill gaps
• Including current job-market information

👩‍💻 Internship Project

SWYNEX Internship — Task 4: Final AI Application

Built as a beginner-friendly AI application demonstrating problem understanding, intelligent skill matching, user interaction, limitations, and responsible AI considerations.