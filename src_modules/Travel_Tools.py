import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Web search function
def search_web_tool(query: str):
    """
    Searches the web and returns results.
    """
    search_tool = TavilySearchResults(max_results=2)
    return search_tool.invoke(query)

# Test the function
#print(search_web_tool("What is the current net worth of Tesla?"))