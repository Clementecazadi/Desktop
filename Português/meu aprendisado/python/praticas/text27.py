class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.atividade = 'fazer Nada'

    def ativ(self):
        print(f'{self.nome} está a {self.atividade}.')


class comer:
    def __init__(self, comida):
        self.comida = comida

    def __repr__(self):
        return f'estudar {self.comida}'


class estudar:
    def __init__(self, dicipl):
        self.diciplina = dicipl

    def __repr__(self):
        return f'estudar {self.diciplina}'


pessoa = Pessoa('clemente')
pessoa.ativ()
pessoa.atividade = comer('arroz')
pessoa.ativ()
pessoa.atividade = estudar('Matematica')
pessoa.ativ()
