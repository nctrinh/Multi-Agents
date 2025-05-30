from typing import Annotated

from langchain_core.tools import tool, InjectedToolCallId
from langgraph.graph import MessagesState, END
from langgraph.prebuilt import InjectedState
from langgraph.types import Command


# HANDOFFS
def create_handoff_tool(*, agent_name: str, description: str | None = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help."
    @tool(name, description=description)
    def handoff_tool(
        state: Annotated[MessagesState, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId]
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {agent_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(
            goto=agent_name,
            update={**state, "messages": state["messages"] + [tool_message]},
            graph=Command.PARENT
        )
    return handoff_tool

@tool
def finish_task(
    state: Annotated[MessagesState, InjectedState],
    final_response: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """Call this when the task is complete to provide the final response to the user."""
    tool_message = {
        "role": "tool",
        "content": final_response,
        "name": "finish_task",
        "tool_call_id": tool_call_id,
    }
    return Command(
        goto=END,
        update={**state, "messages": state["messages"] + [tool_message]},
        graph=Command.PARENT
    )



assign_to_research_agent = create_handoff_tool(
    agent_name="research_agent",
    description="Assign task to a researcher agent.",
)

assign_to_math_agent = create_handoff_tool(
    agent_name="math_agent",
    description="Assign task to a math agent.",
)