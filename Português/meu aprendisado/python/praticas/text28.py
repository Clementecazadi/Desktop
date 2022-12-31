class cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None

    def inserir_end(self, cidade, estado):
        self.endereco = endereco(cidade, estado)

    def print(self):
        print(f'{self.nome.title()} mora em {self.endereco.cidade}/{self.endereco.estado}')

    def __del__(self):
        print(f'{self.nome} Foi apagado!')


class endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} Foi apagado!')


pessoa = cliente('Clemente', 16)
pessoa.inserir_end('bem fica', 'luanda')
pessoa.print()
del pessoa
pessoa1 = cliente('Jose alberto', 19)
pessoa1.inserir_end('capolo 2', 'luanda')
pessoa1.print()
print('=' * 44)
