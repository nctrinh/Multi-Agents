from langgraph.graph import StateGraph, START, END, MessagesState

from multi_agent.utils.agents import research_agent, math_agent, supervisor_agent_with_description


# CREATE MULTI-AGENT GRAPH
workflow = (
    StateGraph(MessagesState)
    .add_node(
        supervisor_agent_with_description, destinations=("research_agent", "math_agent")
    )
    .add_node(research_agent)
    .add_node(math_agent)
    .add_edge(START, "supervisor")
    .add_edge("research_agent", "supervisor")
    .add_edge("math_agent", "supervisor")
    .compile()
)
