from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate.from_template("""
Compare the resume details with the job description.

Resume Data:
{extracted}

Job Description:
{job}

Return matching skills and missing skills.
""")