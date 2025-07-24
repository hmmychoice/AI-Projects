from typing import TypedDict

class ArticleState(TypedDict):
    topic: str
    draft: str
    feedback: str
    good_enough: bool
    final_article: str
    critic_count: int