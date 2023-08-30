import requests
import time


class TelegramBot(object):
    def __init__(self):
        self.token = "
        self.url_base = f"http://api.telegram.org/bot{self.token}/"

    def iniciar(self):
        while True:
            updates: dict = self.obter_updates()
            dados = updates["result"]
            print(dados)
            # updates_id = dados[-1]['update_id']
            mensagem = str(dados[-1]['message']['text'])
            chat_id = dados[-1]['message']['from']['id']
            nome = dados[-1]['message']['from']['first_name']
            self.responder(f"Olá {nome}, meu nome é robô telegram", chat_id)
            print(mensagem)
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
