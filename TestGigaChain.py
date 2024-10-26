from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat

# Авторизация в GigaChat
llm = GigaChat(
    credentials="NzNlMzllMTctMjVlZC00OWM5LTllYmQtNDI4MWJmNTRjNjgxOjlhNTVhODg0LWRjODktNGViZC1iZWJkLTgxYTc5YzY1YzAxOQ==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    # Отключает проверку наличия сертификатов НУЦ Минцифры
    verify_ssl_certs=False,
    streaming=False,
)

llm.get_model("GigaChat")


messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    user_input = input("Пользователь: ")

    messages.append(HumanMessage(content=user_input))
    res = llm.invoke(messages)
    messages.append(res)
    print("GigaChat: ", res.content)