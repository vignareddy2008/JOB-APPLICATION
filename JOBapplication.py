import streamlit as st


st.set_page_config(
    page_title="Job Application",
    page_icon="💼",
    layout="centered"
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8f9ff);
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 40px;
    padding-bottom: 50px;
}

/* Main title */
h1 {
    text-align: center;
    color: #4f46e5;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 30px;
}

/* Section headers */
h2 {
    color: #312e81;
    background-color: #e0e7ff;
    padding: 12px 18px;
    border-radius: 10px;
    margin-top: 30px;
}

/* Labels */
label {
    font-weight: 600 !important;
    color: #374151 !important;
}

/* Text input and textarea */
.stTextInput input,
.stTextArea textarea {
    border: 2px solid #c7d2fe;
    border-radius: 10px;
    padding: 10px;
    background-color: white;
}

/* Input focus */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #6366f1;
    box-shadow: 0 0 5px rgba(99, 102, 241, 0.3);
}

/* Radio buttons */
.stRadio {
    background-color: white;
    padding: 12px 15px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: white;
    padding: 15px;
    border: 2px dashed #818cf8;
    border-radius: 12px;
}

/* Submit button */
.stButton > button {
    width: 100%;
    height: 50px;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    margin-top: 25px;
}

/* Button hover */
.stButton > button:hover {
    background: linear-gradient(90deg, #3730a3, #6d28d9);
    color: white;
    transform: scale(1.01);
}

/* Divider */
hr {
    border: none;
    height: 2px;
    background-color: #c7d2fe;
}

</style>
""", unsafe_allow_html=True)




st.title("💼 JOB APPLICATION")


st.text_input(
    "POSITION APPLY FOR",
    placeholder="e.g. Software Engineer"
)


st.header("👤 PERSONAL INFORMATION")

st.text_input("NAME", placeholder="Enter your full name")

st.text_input(
    "PRESENT ADDRESS",
    placeholder="Enter your current address"
)

st.text_input(
    "PHONE NUMBER",
    placeholder="Enter your phone number"
)

st.text_input(
    "EMAIL ADDRESS",
    placeholder="Enter your email address"
)


st.header("🎓 EDUCATION")

st.text_input("DEGREE", placeholder="e.g. B.Tech")

st.text_input(
    "COLLEGE",
    placeholder="Enter your college name"
)

st.radio(
    "BRANCH",
    ["CSE", "CSE-AIML", "CSE-DS", "CS", "OTHERS"]
)

st.text_input(
    "YEAR OF GRADUATION",
    placeholder="e.g. 2026"
)

st.text_input(
    "CGPA",
    placeholder="e.g. 8.5"
)


st.header("💻 SKILLS")

st.text_area(
    "WHAT ARE THE SKILLS YOU HAVE?",
    placeholder="e.g. Python, Java, SQL, HTML, CSS, Machine Learning..."
)

st.header("✅ ELIGIBILITY")

st.radio(
    "ARE YOU A B.TECH GRADUATE?",
    ["YES", "NO"]
)

st.radio(
    "ARE YOU A MAJOR?",
    ["YES", "NO"]
)

# Resume
st.header("📄 RESUME")

resume = st.file_uploader(
    "UPLOAD YOUR RESUME HERE",
    type=["pdf", "doc", "docx"]
)

# Experience
st.header("💼 EXPERIENCE")

experience = st.radio(
    "EXPERIENCE",
    ["Experienced", "Non-Experienced"]
)

if experience == "Experienced":
    st.text_input(
        "IF EXPERIENCED, HOW MANY YEARS?",
        placeholder="e.g. 2"
    )
if st.button("🚀 SUBMIT APPLICATION"):
    st.success("✅ Your job application has been submitted successfully!")