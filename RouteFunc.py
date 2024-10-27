from RouteToQuestion import categorize_llm


def route_question(state):
    print("---ROUTE QUESTION---")
    question = state["question"]
    source = categorize_llm.invoke({"question": question})
    print(source)
    if source['qtype'] == "info_clinic":
        print("---ROUTE QUESTION TO INFO CLINIC---")
        return "info_clinic"
    elif source['qtype'] == "appointment":
        print("---ROUTE QUESTION TO APPOINTMENT---")
        return "appointment"
    elif source['qtype'] == "info_doctor":
        print("---ROUTE QUESTION TO INFO DOCTOR---")
        return "info_doctor"
    elif source['qtype'] == "info_free_date":
        print("---ROUTE QUESTION TO INFO FREE DATE---")
        return "info_free_date"