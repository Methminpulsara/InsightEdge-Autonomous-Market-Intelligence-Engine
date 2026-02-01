from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from core.state import AgentState
from dotenv import load_dotenv

load_dotenv()


def strategist_agent(state:AgentState):

    # final agent for summery

    llm = ChatOpenAI(model="gpt-5.2-2025-12-11")

    prompt_template = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a Senior Business Strategy Consultant. Your task is to take market research "
            "and competitor analysis data to create a comprehensive, actionable business strategy report."
        ),
        (
            "human",
            "Business Idea: {idea}\n\n"
            "Market Research Data: {research}\n\n"
            "Competitor Data: {competitors}\n\n"
            "Based on the above information, provide a final report in Markdown format including:\n"
            "1. Executive Summary\n"
            "2. SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)\n"
            "3. Market Entry Strategy\n"
            "4. Final Verdict (Go/No-Go Recommendation)"
        )
    ])

    chain = prompt_template | llm

    response = chain.invoke(
        {
            "idea" : state['business_idea'],
            "research":  state['market_research_data'],
            "competitors" : state['competitor_data']
        }
    )

    # final out put share to state -> dec
    return {"final_output": response.content}



