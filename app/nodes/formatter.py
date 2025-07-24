from app.llm import ollama_llm
from app.state import ArticleState

def formatter(state: ArticleState):
    draft = state["draft"]
    feedback = state.get("feedback", "")

    prompt = f"""
    Here is the final draft:
    {draft}

    Here is the feedback:
    {feedback}

    Please polish this draft to be clear, engaging, and ready for publishing on Medium.
    Keep the tone friendly and beginner-friendly. Only return the final article text without any additional comments or explanations.
    """

    response = ollama_llm.invoke(prompt)
    return {"final_article": response}