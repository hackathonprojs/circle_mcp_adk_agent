# ./adk_agent_samples/mcp_agent/agent.py
import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='circle_agent',
    instruction='Help the user access USDC stable coin through our Circle MCP',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="uv",
                args=["--directory", 
                      "/home/t/mydata/hackathon/mcp/trial/circle_mcp1/circle_mcp_server/", 
                      "run",
                      "server.py"],
                #env={"STRIPE_SECRET_KEY": os.getenv("STRIPE_SECRET_KEY")},
            )
        )
    ],
)