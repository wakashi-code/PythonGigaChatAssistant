from langchain.chat_models.gigachat import GigaChat
import requests

giga = GigaChat(credentials='NzNlMzllMTctMjVlZC00OWM5LTllYmQtNDI4MWJmNTRjNjgxOjlhNTVhODg0LWRjODktNGViZC1iZWJkLTgxYTc5YzY1YzAxOQ==', model='GigaChat', verify_ssl_certs=False)


url = "https://gigachat.devices.sberbank.ru/"

payload={'scope': 'GIGACHAT_API_PERS'}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.Yu-z6Zg5C0QB36xJnRXUvesr2pmqcHIUOeaLBwiwUyB5Hp0oP5_xEO4um_pQGTlDNAq_WOtah7qZneVBvsmORH_QWtuKHjNyKZAcqgDp0jXbegl_YhwLYPyYiKU-yJFxvYSFT2ILFi3g0GeJf1ARemYwAgOjlcroeXr7uF4IIxh1YimwEJUg-MNbt6AaLBcwBl_1Ymvyld6PgW6tT3AWmxgM2dNLlW_AHxbSewnqxHK05cqPsoGTDIcKmFLSevQG3z5zHgWgoMQxBdptsLe8SuXm_-HB9OzEwr6RfejZKU3L2pftDaMxjh2idNXVyYFxwqRJ3sAL1LMTnnqZp8e3iQ.uUNzKE7rUYYxYVknSm3LmQ.2xSpKpS9Zj5Oq4BK_QynHVKia3-Q_N1G4HfQFnHGdCdFSHZjgrSP4sI3ERRZ6PJ7TLiLQV0DYlPfByJwPcXsRnJRrjVXN42Izxyl-WZncdDU1mK_OUTbp_2VYJbx-MHUDMFXbuUM_JJk2cHI7qZGfFoBbiIqw-LrntlRq66KY5z1JpC01_089DXh93tfmypFegAuFLczWH7WRLZuG1zMjqTwEkD3BKI1QUi3lorrB3MqWwOMoFurl6zk90W9BIcXlEkiJ5394pGIq9_k5iP3V20sHnNcAStEvci1IYcCkCB7NYH26TIKas8VyS_Qv9lvsrv6rAzDB5ixrjw0KwafH23Can4UBhNpbE5JvKAQS7wjixBTb8rs02BGn-xBRf2M3qbwa8niSIIjSsVPamFEhj80xR6caBeGYjlBxjpQYPsh5K9X8HuMhWx8dMnTd3p6_-Aurm0Eq8pxmLvKK0_GLLmA3CfI7I2r39OVZLOtcT9YmzRIGBEljyTnyG4UKj0i54hADMBB00RWAM0B8O6JGxxqZNqui9f8G8vJxqCtuJrphEMmPGm6XPv6R68m2zxShWWD5TR1HKZde-Uy2eify6yMQdfiQaHoBYg3hZgEr6_dQbgf1dGoqjtzcz5jrCdEI3Xb5k5gwNTbKJ4Gizqmw92TYqD-KF_XC3uOTPI1YydGzQ-gomeL62ZO0Gz29l8bNwG3YlAcNv2x7lDaTcFXNKZLdsUcl6mqCI9BCyVuQVI.vMWWr1RlalvorrHz737FqyDuFcljsI2D8bEvi6ivjfc'
}

response = requests.get(url, headers=headers, data=payload, verify=False)

print(response.text)