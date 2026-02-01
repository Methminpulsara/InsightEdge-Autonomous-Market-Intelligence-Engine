from langgraph.graph import StateGraph
from langgraph.constants import END
from agents import research_agent, analyst_agent, strategist_agent
from state import AgentState


def create_graph():
    # create graph
    workflow = StateGraph(AgentState)

    # add nodes
    workflow.add_node("research_agent", research_agent)
    workflow.add_node("analyst_agent", analyst_agent)
    workflow.add_node("strategist_agent", strategist_agent)

    # set start point
    workflow.set_entry_point("research_agent")

    # make Edges
    workflow.add_edge("research_agent" , "analyst_agent")

    workflow.add_edge("analyst_agent", "strategist_agent")

    workflow.add_edge("strategist_agent", END)

    # compile graph
    return workflow.compile()


