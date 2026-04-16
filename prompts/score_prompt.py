from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
Based on the match result, assign a score from 0 to 100.

Rules:
Do NOT assume missing skills
Only use given data

Match Data:
{match}

Return only score.
""")