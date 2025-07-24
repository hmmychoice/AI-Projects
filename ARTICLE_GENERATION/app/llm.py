from langchain_community.llms import Ollama
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from .config import OLLAMA_BASE_URL, OLLAMA_MODEL, TAVILY_API_KEY

ollama_llm = Ollama(
    base_url=OLLAMA_BASE_URL,
    model=OLLAMA_MODEL
)

search = TavilySearchAPIWrapper(
    tavily_api_key=TAVILY_API_KEY
)