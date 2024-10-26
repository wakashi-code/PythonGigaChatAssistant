### Generate

from langchain import hub
from langchain.chat_models.gigachat import GigaChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import tesxt

# Prompt
system = """
Твоя задача ответить на вопрос, используя информацию из {context}.
{context} представляет из себя результат запроса к внешнему ресурсу в формате json
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: {question}"),
    ]
)

giga = GigaChat(
    model=tesxt.GIGACHAT_MODEL,
    credentials=tesxt.GIGACHAT_CREDENTIALS,
    scope=tesxt.GIGACHAT_SCOPE,
    verify_ssl_certs=False,

    temperature=0.1
)

# Chain
chain = prompt | giga | StrOutputParser()

# Run
test_context='{"data":{"searchClinic":{"elems":[{"clinicDoctorList":{"elems":[{"clinic":{"name":"Клиника N1"},"doctor":{"entityId":"7424408113957502977","entity":{"person":{"entityId":"7424406473279995905","entity":{"lastName":"Biryukov"}},"doctorType":{"name":"Терапевт"}}}},{"clinic":{"name":"Клиника N1"},"doctor":{"entityId":"7424408113957502979","entity":{"person":{"entityId":"7424406477574963202","entity":{"lastName":"Varenikov"}},"doctorType":{"name":"Хирург"}}}}]}}]}}}'

generation = chain.invoke({"context": test_context, "question": "Какие есть хирурги?"})
print(generation)
generation = chain.invoke({"context": test_context, "question": "Какие есть терапевты?"})
print(generation)

def generate(state):

    print("---GENERATE---")
    question = state["question"]
    context = state["context"]

    # RAG generation
    generation = chain.invoke({"context": context, "question": question})
    return {"context": context, "question": question, "generation": generation}