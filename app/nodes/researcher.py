from app.llm import ollama_llm, search
from app.state import ArticleState

def researcher(state: ArticleState):
    topic = state["topic"]
    feedback = state.get("feedback", "")

    search_results = search.results(topic, max_results=3)

    refinement = f"\nAlso improve the draft using this feedback: {feedback}" if feedback else ""

    prompt = f"""
    Topic: "{topic}"

    Below are real search results about this topic:
    {search_results}

    Using these search results, write or improve a detailed, beginner-friendly article. Feel free to add 
    some additional knowledge related to the topic that may not be in the search results.
    Be clear, factual, and helpful.
    {refinement}
    """
    print(f"Researching topic: {topic}")  # Debugging line to check the topic

    response = ollama_llm.invoke(prompt)
    return {"draft": response}