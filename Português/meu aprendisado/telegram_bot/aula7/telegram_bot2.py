import requests
import time


class TelegramBot(object):
    def __init__(self):
        self.token = "
        self.url_base = f"http://api.telegram.org/bot{self.token}/"

    def iniciar(self):
        find_cep: bool = False
        updates: dict = self.obter_updates()
        dados = updates["result"]
        chat_id = dados[-1]['message']['from']['id']
        self.responder("Digite o CEP para encontrar a rua.", chat_id)
        while True:
            updates = self.obter_updates()
            dados = updates['result']
            mensagem = str(dados[-1]['message']['text'])
            chat_id = dados[-1]['message']['from']['id']
            nome = dados[-1]['message']['from']['first_name']
            if mensagem and not find_cep:
                if len(mensagem) == 8:
                    print('Tamanho de cep ok!')
                    c = self.get_info_cep(mensagem)
                    try:
                        self.responder(f"Sua rua é = {c['logradouro']}", chat_id)
                        self.responder(f"Seu estado é = {c['uf']}", chat_id)
                    except KeyError:
                        self.responder('Seu Cep está invalido. Tente novamente', chat_id)
                    else:
                        find_cep = True

            if find_cep:
                self.responder(f"Foi um prazer ajudar-te {nome}.", chat_id)
                break
            print("-" * 34)
            time.sleep(5)

    def obter_updates(self) -> dict:
        link_api = requests.get(self.url_base + 'getUpdates')
        return link_api.json()

    def responder(self, texto: str, chat_id: int) -> None:
        link_requisicao = f"{self.url_base}sendMessage?chat_id={chat_id}" \
                          f"&text={texto}"
        requests.get(link_requisicao)

    @staticmethod
    def get_info_cep(cep: str) -> dict:
        url_base = f"https://viacep.com.br/ws/{cep}/json/"
        r = requests.get(url_base)
        return r.json()


bot = TelegramBot()
bot.iniciar()
