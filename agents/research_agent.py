from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from tools.search_tool import get_search_tool
from core.state import AgentState
from dotenv import load_dotenv

load_dotenv()


def research_agent(state: AgentState):
    llm = ChatOpenAI(model="gpt-4o-mini")

    search = get_search_tool()

    # search
    query = f"Current market trends for:  {state['business_idea']}"
    search_result = search.invoke(query)

    # promt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system",
         "You are an expert Market Researcher. Use the provided search results to summarize demand, trends, and audience."),
        ("human", "Business Idea: {idea}\n\nSearch Results: {results}")
    ])

    chain = prompt_template | llm

    # fill the placeholders in the system promt {idea} and {results}
    response = chain.invoke({"idea": state['business_idea'],
                             "results": search_result
                             })

    return {"market_research_data": response.content}
