from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
Extract the following from the resume:

Skills:
Experience:
Tools:

Resume:
{resume}

Return strictly in this format.
""")