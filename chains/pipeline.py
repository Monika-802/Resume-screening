
from langchain_core.output_parsers import StrOutputParser
from prompts.extract_prompt import extract_prompt
from prompts.match_prompt import match_prompt
from prompts.score_prompt import score_prompt
from prompts.explain_prompt import explain_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage


llm = ChatGoogleGenerativeAI(model="gemini-3.1-Flash" , convert_system_message_to_human_message=True)
messages = [
    SystemMessage(content="You are a professional resume screener."),
    HumanMessage(content="Analyze this resume for a software engineer role.")
]


def run_pipeline(resume, job):
    chain = extract_prompt | llm | StrOutputParser()
    extracted = (extract_prompt | llm).invoke({"resume": resume}).content
    match = (match_prompt | llm).invoke({"extracted": extracted, "job": job}).content
    score = (score_prompt | llm).invoke({"match": match}).content
    explanation = (explain_prompt | llm).invoke({"match": match, "score": score}).content


    return {
        "extracted": extracted,
        "match": match,
        "score": score,
        "explanation": explanation,
        "extract": chain
    }