from langgraph.prebuilt import create_react_agent

from multi_agent.config import (
    get_web_search, get_web_search_llm, get_math_llm, 
    get_supervisor_llm, get_cypher_llm, get_action_build_llm
)
from multi_agent.utils.functions import add, multiply, divide
from multi_agent.tools import (
    assign_to_math_agent_with_description, 
    assign_to_research_agent_with_description, 
    assign_to_cyper_kg_agent_with_description, 
    assign_to_build_knowledge_graph_agent_with_description
)
from multi_agent.utils.prompts import (
    supervisor_prompt, 
    math_prompt, 
    research_prompt, 
    cypher_agent_prompt,
    action_build_generator_prompt
)
from multi_agent.knowledge_graph.cyper_tools.neo4j_tools import (
    cypher_executor_tool, 
    cypher_generator_tool,
    download_files_for_course
)
from multi_agent.knowledge_graph.build_kg_tools.build_knowledge_graph_tools import (
    build_knowledge_graph_tool,
    action_generator_tool
)

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

# CYPER KNOWLEDGE GRAPH AGENT
cyper_kg_llm = get_cypher_llm()
cyper_kg_agent = create_react_agent(
    model=cyper_kg_llm,
    tools=[
        cypher_generator_tool, 
        cypher_executor_tool,
        download_files_for_course
    ],
    prompt=cypher_agent_prompt,
    name="cyper_kg_agent",
)

# BUILD KNOWLEDGE GRAPH AGENT
database_llm = get_action_build_llm()
build_knowledge_graph_agent = create_react_agent(
    model=database_llm,
    tools=[
        action_generator_tool,
        build_knowledge_graph_tool
    ],
    prompt=action_build_generator_prompt,
    name="build_knowledge_graph_agent",
) 

# DEFINE SUPERVISOR AGENT
supervisor_agent_with_description = create_react_agent(
    model=get_supervisor_llm(),
    tools=[
        # assign_to_research_agent_with_description, 
        # assign_to_math_agent_with_description,
        assign_to_cyper_kg_agent_with_description,
        assign_to_build_knowledge_graph_agent_with_description
    ],
    prompt=supervisor_prompt,
    name="supervisor"
)
