import json
from app.llm import ollama_llm
from app.state import ArticleState

def critic(state: ArticleState):
    draft = state["draft"]
    critic_count = state['critic_count'] + 1

    prompt = f"""
    Critique the following draft for clarity, accuracy, and beginner-friendliness:

    {draft}

    - If the draft is good enough to publish, return: {{"good_enough": true, "feedback": "Looks good!"}}
    - If the draft needs improvements, return: {{"good_enough": false, "feedback": "...specific feedback..."}}

    Respond ONLY in valid JSON.
    """
    print(f"Criticizing draft (attempt {critic_count})")  # Debugging line to check the draft
    response = ollama_llm.invoke(prompt)

    try:
        data = json.loads(response)
        return {
            "good_enough": data["good_enough"],
            "feedback": data["feedback"],
            "critic_count": critic_count
        }
    except Exception as e:
        return {
            "good_enough": False,
            "feedback": "LLM response could not be parsed. Please clarify and improve.",
            "critic_count": critic_count
        }