from dotenv import load_dotenv
import os
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def get_search_tool():
    # for search in Google / Internet
    api_wrapper = TavilySearchAPIWrapper()
    return TavilySearchResults(api_wrapper=api_wrapper, max_results=5)

