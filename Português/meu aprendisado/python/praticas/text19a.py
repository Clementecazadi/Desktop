class Pessoa:
    from datetime import date
    ano = date.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome.capitalize().strip()
        self.idade = int(idade)
        self._comendo = comendo
        self._falando = falando
        self.nasceu = self.ano - idade

    def comer(self, alimento):
        if self._comendo:
            print(f'O/A {self.nome} já esta comendo.')
            return

        print(f'O/A {self.nome} esta comendo {alimento}.')
        self._comendo = True

    def para_comer(self):
        if not self._comendo:
            print(f'O/A {self.nome} não esta comendo.')
            return
        print(f'O/A {self.nome} parou de comer.')
        self._comendo = False

    def falar(self, asunto):
        if self._falando:
            print(f'O/A {self.nome} já esta falando.')
            return

        print(f'O/A {self.nome} esta falando sobre {asunto}.')
        self._falando = True

    def parar_falar(self):
        if not self._falando:
            print(f'O/A {self.nome} não esta falando.')
            return

        print(f'O/A {self.nome} parou de falar.')
        self._falando = False
