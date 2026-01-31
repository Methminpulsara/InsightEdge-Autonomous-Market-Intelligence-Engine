from typing import TypedDict


class AgentState(TypedDict):
    # input
    business_idea: str

    # market_research
    market_research_data : str

    # competitors
    competitor_data : str

    # output
    final_output : str
