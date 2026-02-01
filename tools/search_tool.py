from dotenv import load_dotenv
import os
from langchain_tavily import TavilySearch

load_dotenv()

def get_search_tool():
    # for search in Google / Internet
    return TavilySearch(max_results=5)

