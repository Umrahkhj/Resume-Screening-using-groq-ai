from ai import analyze_resume
import streamlit as st
from resume_parser import extract_text_from_pdf

# Page Configuration
st.set_page_config(
    page_title="AI Resume Screening Assistant",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Screening Assistant")
st.write("Upload your resume and paste the job description for AI analysis.")
st.divider()

# Upload Resume
resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=120
)

# Analyze Button
if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload a resume.")

    elif job_description.strip() == "":
        st.error("Please paste the Job Description.")

    else:

        # Extract Resume Text
        resume_text = extract_text_from_pdf(resume)

        if resume_text.startswith("Error"):
            st.error(resume_text)

        else:

            st.success("✅ Resume uploaded successfully!")

            with st.spinner("🤖 Analyzing Resume..."):

                result = analyze_resume(
                    resume_text,
                    job_description
                )

            st.subheader("🤖 AI Resume Analysis")
            st.markdown(result)

            with st.expander("📄 View Extracted Resume Text"):
                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=180
                )