from langchain_community.utilities.requests import TextRequestsWrapper


def find_doctors(state):
    question = state['question']

    graphql_search_doctors = {
        "operationName": "searchDoctors",
        "variables": {},
        "query": "query searchDoctors {\n  searchClinic {\n    elems {\n      clinicDoctorList {\n        elems {\n          clinic {\n            name\n          }\n          doctor {\n            entityId\n            entity {\n              person {\n                entityId\n                entity {\n                  lastName\n                }\n              }\n              doctorType {\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"
    }

    requests_tool = TextRequestsWrapper()

    # Use the tool
    response = requests_tool.post(url="https://smapi.pv-api.sbc.space/ds-7429590172239724545/graphql",
                                  data=graphql_search_doctors)
    print(response)
    return {"question": question, "context": response}

    #

# Print the response