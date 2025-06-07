from langchain.agents import Tool
from langgraph.prebuilt import create_react_agent

from multi_agent.config import (get_action_build_llm, get_cypher_llm,
                                get_math_llm, get_supervisor_llm,
                                get_web_search, get_web_search_llm)
from multi_agent.knowledge_graph.build_kg_tools.build_knowledge_graph_tools import (
    action_generator_tool, build_knowledge_graph_tool)
from multi_agent.knowledge_graph.cyper_tools.neo4j_tools import (
    cypher_executor_tool, cypher_generator_tool, download_files_for_course)
from multi_agent.tools import (
    assign_to_build_knowledge_graph_agent_with_description,
    assign_to_cyper_kg_agent_with_description)
from multi_agent.utils.functions import add, divide, multiply
from multi_agent.utils.prompts import (build_knowledge_graph_agent_prompt,
                                       cypher_agent_prompt, math_prompt,
                                       research_prompt, supervisor_prompt)

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
cyper_kg_tools = [
    Tool(
        name="cypher_generator_tool",
        func=cypher_generator_tool,
        description="Convert a natural language question into a Cypher query."
    ),
    Tool(
        name="cypher_executor_tool",
        func=cypher_executor_tool,
        description="Execute a Cypher query on Neo4j and return the results as plain text."
    ),
    Tool(
        name="download_files_for_course",
        func=download_files_for_course,
        description="Download files from a specific course given its course ID."
    ),
]
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
    prompt=build_knowledge_graph_agent_prompt,
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
