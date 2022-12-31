class comer:
    def __init__(self, comida):
        

class nome:
    def __init__(self, nome):
        self.nome = nome

    def print(self):
        print(f'O nome dele é {self.nome}')



class idade:
    def __init__(self):
        self.idade = idade

    def printt(self):
        print(f'A idade é {self.idade}')


class pessoa(nome, idade):
    def __init__(self, oi, da):
        super(nome, self).__init__()
        super(idade, self).__init__()
        self.nome(oi)
        self.idade = da


pe = pessoa('clemente', 13)
pe.print()
pe.printt()
