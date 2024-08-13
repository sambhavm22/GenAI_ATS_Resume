import streamlit as st
import openai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # Load all environment variables

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(input_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change this to "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a skilled ATS (Applicant Tracking System) specialized in tech jobs."},
            {"role": "user", "content": input_prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt_template = """
Hey, act like a skilled or very experienced ATS (Applicant Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive, and you should provide 
the best assistance for improving the resume. Assign the percentage match based 
on the job description and
list the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in a single string structured as follows:
{{"JD Match": "X%", "MissingKeywords": ["keyword1", "keyword2"], "Profile Summary": "summary text"}}
"""

## Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt_template.format(text=text, jd=jd)
        response = get_openai_response(input_prompt)
        st.subheader("ATS Evaluation")
        st.text_area("Response", value=response, height=200)
