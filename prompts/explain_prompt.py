from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template("""
Explain the score based on strengths and gaps.

Match Data:
{match}

Score:
{score}

Return explanation clearly.
""")