# ./adk_agent_samples/mcp_agent/agent.py
import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='weather_agent',
    instruction='Help the user get weather information',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@h1deya/mcp-server-weather"],
                #env={},
            )
        )
    ],
)