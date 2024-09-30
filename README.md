# Smart ATS: Resume Evaluation Tool
Smart ATS is a web application that helps improve resumes for Applicant Tracking Systems (ATS). It evaluates resumes based on job descriptions, providing feedback on how well the resume matches the job and suggesting missing keywords for optimization.

Features:
- Resume Evaluation: Upload your resume in PDF format, and Smart ATS will analyze it based on the job description you provide.
- ATS Insights: The application acts as an experienced ATS, specialized in tech jobs such as software engineering, data science, and big data engineering.
- Job Matching: It provides a percentage match between the resume and the job description.
- Keyword Suggestions: Lists the missing keywords that are crucial for the given job description.
  
Profile Summary: Generates a brief summary of the resume's strengths and areas of improvement.
Technologies Used
Streamlit: The web framework for building the user interface.
OpenAI API: For generating resume analysis and feedback using GPT models.
PyPDF2: To extract text from PDF resumes.
Python-dotenv: For managing environment variables securely.

### Installation

1. Clone the repository:
  ``git clone https://github.com/sambhavm22/GenAI_ATS_Resume``

2. Install the required dependencies:
   ``pip install -r requirements.txt``

3. Create a .env file in the root directory and add your OpenAI API key:
   ``OPENAI_API_KEY=your_openai_api_key``
