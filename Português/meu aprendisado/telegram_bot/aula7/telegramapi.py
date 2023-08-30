import requests
import time
token = 
url_base = f"http:ap//i.telegram.org/bot{token}"

while True:
    resposta = requests.get(url_base + "/getUpdates")
    resposta_dict = resposta.json()
    print(resposta_dict)
    time.sleep(5)
