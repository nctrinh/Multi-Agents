from langgraph.graph import StateGraph, START, END, MessagesState

from multi_agent.utils.agents import research_agent, math_agent, supervisor_agent


# CREATE MULTI-AGENT GRAPH
supervisor = (
    StateGraph(MessagesState)
    # NOTE: `destinations` is only needed for visualization and doesn't affect runtime behavior
    .add_node(supervisor_agent, destinations=("research_agent", "math_agent", END))
    .add_node(research_agent)
    .add_node(math_agent)
    .add_edge(START, "supervisor")
    # always return back to the supervisor
    .add_edge("research_agent", "supervisor")
    .add_edge("math_agent", "supervisor")
    .compile()
)

if __name__ == "__main__":
    # Ví dụ input ban đầu
    initial_input = {"messages": ["2 + 2 =?"]}
    
    # Chạy graph
    result = supervisor.invoke(initial_input)
    
    # In kết quả
    print("=== KẾT QUẢ ===")
    for message in result["messages"]:
        print(message)