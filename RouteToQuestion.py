from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from pydantic import BaseModel, Field
from langchain_community.chat_models import GigaChat


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    qtype: Literal["info_clinic", "appointment", "info_doctor", "info_free_date"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )


system = """
Твоя задача соотнести вопрос пользователя с одной из категорий:
1. appointment - Запись на приём к врачу \n
2. info_free_date - Вопрос про свободное время у врача \n
3. info_doctor - Список врачей \n
4. info_clinic - Список клиник \n
В ответ написать к какой категории относится вопрос
"""

chat = GigaChat(
    #    model="GigaChat-Pro",
    #    credentials=creds,
    #    scope="GIGACHAT_API_CORP",  # "GIGACHAT_API_PERS",
    verify_ssl_certs=False,

    temperature=0.1
)

structured_llm_router = chat.with_structured_output(RouteQuery)
type_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: {question}"),
    ]
)

categorize_llm = type_prompt | structured_llm_router

print(categorize_llm.invoke({"question": "Какое время свободно 3 сентября у Колесникова?"}))
print(categorize_llm.invoke({"question": "Какие есть хирурги?"}))
print(categorize_llm.invoke({"question": "У какого хирурга есть свободное время на 3 сентября?"}))
print(categorize_llm.invoke({"question": "Запиши на прием к Колесникову на 3 сентября 10:00"}))
