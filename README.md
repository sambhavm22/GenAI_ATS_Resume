# Smart ATS: Resume Evaluation Tool
Smart ATS is a web application that helps improve resumes for Applicant Tracking Systems (ATS). It evaluates resumes based on job descriptions, providing feedback on how well the resume matches the job and suggesting missing keywords for optimization.

### Features:

1. Resume Evaluation: Upload your resume in PDF format, and Smart ATS will analyze it based on the job description you provide.
2. ATS Insights: The application acts as an experienced ATS, specialized in tech jobs such as software engineering, data science, and big data engineering.
3. Job Matching: It provides a percentage match between the resume and the job description.
4. Keyword Suggestions: Lists the missing keywords that are crucial for the given job description.
5. Profile Summary: Generates a brief summary of the resume's strengths and areas of improvement.
  
### Technologies Used:

1. Streamlit: The web framework for building the user interface.
2. OpenAI API: For generating resume analysis and feedback using GPT models.
3.PyPDF2: To extract text from PDF resumes.
4. Python-dotenv: For managing environment variables securely.

### Installation

1. Clone the repository:
   
- ``git clone https://github.com/sambhavm22/GenAI_ATS_Resume``

2. Install the required dependencies:
- ``pip install -r requirements.txt``

3. Create a .env file in the root directory and add your OpenAI API key:
- ``OPENAI_API_KEY=your_openai_api_key``

### Usage
1. Run the Streamlit app:
   ``streamlit run app.py``
   
2. Upload a resume in PDF format and paste the job description into the text area.

3. Click Submit to get the ATS evaluation, including a match percentage, missing keywords, and a summary.

### Requirements
1. Python 3.10+

2. The following Python libraries:
- streamlit
- python-dotenv
- langchain-openai
- langchain
- openai
- PyPDF2

### How It Works

1. Resume Upload: The application extracts text from the uploaded PDF resume using PyPDF2.
2. Job Description Input: The user pastes the job description into the text area.
3. OpenAI GPT Evaluation: The application sends the resume text and job description to OpenAI's GPT model, which acts as an ATS to evaluate the match and suggest missing keywords.
4. Output: The application returns a percentage match, a list of missing keywords, and a profile summary.

```python
def hello_world():
    print("Hello, World!")


