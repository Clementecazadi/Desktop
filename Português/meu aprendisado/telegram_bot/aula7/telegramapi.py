import requests
import time
token = "6157993125:AAHX38Zo9Cglqh3y7_-5DqysX0rrsN6tq28"
url_base = f"http:ap//i.telegram.org/bot{token}"

while True:
    resposta = requests.get(url_base + "/getUpdates")
    resposta_dict = resposta.json()
    print(resposta_dict)
    time.sleep(5)
