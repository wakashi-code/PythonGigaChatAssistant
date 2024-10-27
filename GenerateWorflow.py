from langgraph.graph import END, StateGraph, START

from ClassGraph import GraphState
from GenerateAnswerToUser import generate
from RouteFunc import route_question
from SearchDataOnDataSpace import find_doctors

workflow = StateGraph(GraphState)

#TODO
workflow.add_node("info_doctor", find_doctors)
workflow.add_node("generate", generate)



workflow.add_conditional_edges(
    START,
    route_question,
    {
        "info_doctor": "info_doctor",
    },
)

workflow.add_edge("info_doctor", "generate")

app = workflow.compile()