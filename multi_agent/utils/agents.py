from langgraph.prebuilt import create_react_agent

from multi_agent.config import get_web_search, get_web_search_llm, get_math_llm, get_supervisor_llm
from multi_agent.utils.functions import add, multiply, divide
from multi_agent.utils.tools import assign_to_math_agent_with_description, assign_to_research_agent_with_description
from multi_agent.utils.prompts import supervisor_prompt, math_prompt, research_prompt


# RESEARCH AGENT
web_search = get_web_search(max_results=3)
web_search_llm = get_web_search_llm()
research_agent = create_react_agent(
    model=web_search_llm,
    tools=[web_search],
    prompt=research_prompt,
    name="research_agent",
)

# MATH AGENT
math_llm = get_math_llm()
math_agent = create_react_agent(
    model=math_llm,
    tools=[add, multiply, divide],
    prompt=math_prompt,
    name="math_agent",
)

# DEFINE SUPERVISOR AGENT
supervisor_agent_with_description = create_react_agent(
    model=get_supervisor_llm(),
    tools=[
        assign_to_research_agent_with_description, 
        assign_to_math_agent_with_description
    ],
    prompt=supervisor_prompt,
    name="supervisor"
)
