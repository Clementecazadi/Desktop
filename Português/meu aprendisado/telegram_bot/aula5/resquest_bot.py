import requests

""""
resp = requests.get()
# requests.post()
jab = resp.json()
"""


def get_info_cep(cep: str):
    url_base = f"https://viacep.com.br/ws/{cep}/json/"
    r = requests.get(url_base)
    return r.json()


cep = get_info_cep("01002000")
print(cep)
