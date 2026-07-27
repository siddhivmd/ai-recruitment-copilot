import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

server_params = StdioServerParameters(
    command="python",
    args=["mcp_servers/candidate_server.py"],
)

async def query_candidates(question: str):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
            llm_with_tools = llm.bind_tools(tools)

            response = llm_with_tools.invoke([HumanMessage(content=question)])
            if response.tool_calls:
                for call in response.tool_calls:
                    tool = next(t for t in tools if t.name == call["name"])
                    result = await tool.ainvoke(call["args"])
                    return result
            return response.content

if __name__ == "__main__":
    asyncio.run(query_candidates("List all candidates in the database"))