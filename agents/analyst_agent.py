from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from tools.search_tool import get_search_tool
from core.state import AgentState
from dotenv import load_dotenv

load_dotenv()

def analyst_agent(state: AgentState):
    # meken thma competitor kud and weakness blnne meken

    llm = ChatOpenAI(model="gpt-4o-mini")

    search = get_search_tool()

    query = f"Top competitors and alternative services for: {state['business_idea']}"
    search_results = search.invoke(query)

    promt_template = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a Competitor Business Analyst. Your goal is to identify direct competitors, "
            "analyze their SWOT (Strengths, Weaknesses, Opportunities, Threats), and find market gaps."
        ),
        (
            "human",
            "Based on these search results: {results}\n\n"
            "Identify the competitors for the business idea: '{idea}'. "
            "What are their strengths and weaknesses, and where is the market gap?"
        )
    ])

    chain = promt_template | llm

    response = chain.invoke(
        {"results": search_results,
         "idea": state['business_idea']
         }
    )

    # return llm output to state -> dec
    return {"competitor_data": response.content}
