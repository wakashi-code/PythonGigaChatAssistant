from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat
from SearchDataOnDataSpace import find_clinics, find_doctors
from ParseJson import parse_doctors

# Авторизация в GigaChat
llm = GigaChat(
    credentials="NzNlMzllMTctMjVlZC00OWM5LTllYmQtNDI4MWJmNTRjNjgxOjlhNTVhODg0LWRjODktNGViZC1iZWJkLTgxYTc5YzY1YzAxOQ==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False,
    streaming=False,
)

messages = []

while True:
    user_input = input("Пользователь: ")
    messages.append(HumanMessage(content=user_input))

    # Проверяем запрос пользователя
    if "список врачей" in user_input.lower() or "Покажи мне список всех врачей" in user_input.lower():
        response_data = find_doctors({"question": user_input})  # Передаём состояние
        doctors_list = response_data.get("context", {})
        result = parse_doctors(doctors_list)

    else:
        res = llm.invoke(messages)
        messages.append(res)
        print("GigaChat: ", res.content)
