import requests


def get_ticks(moeda='BTC', metodo='ticker') -> dict:
    r = requests.get(f"https://www.mercadobitcoin.net/api/{moeda}/{metodo}/")
    return r.json()


de = get_ticks()
print(de)
