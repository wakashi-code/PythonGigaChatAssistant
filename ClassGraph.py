from typing import Dict

from typing_extensions import TypedDict


class GraphState(TypedDict):
    args: Dict
    question: str
    generation: str
    context: str