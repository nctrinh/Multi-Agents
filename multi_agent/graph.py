from langgraph.graph import END, START, MessagesState, StateGraph

from multi_agent.agents import (build_knowledge_graph_agent, cyper_kg_agent,
                                supervisor_agent_with_description)

# CREATE MULTI-AGENT GRAPH
workflow = (
    StateGraph(MessagesState)
    .add_node(
        supervisor_agent_with_description, destinations=(
            "cyper_kg_agent", "build_knowledge_graph_agent", END)
    )
    # .add_node(research_agent)
    # .add_node(math_agent)
    .add_node(cyper_kg_agent)
    .add_node(build_knowledge_graph_agent)
    .add_edge(START, "supervisor")
    # .add_edge("research_agent", "supervisor")
    # .add_edge("math_agent", "supervisor")
    .add_edge("cyper_kg_agent", "supervisor")
    .add_edge("build_knowledge_graph_agent", "supervisor")
    .compile()
)
