class fracao:
    def __init__(self, num, denom):
        self.numerador = num
        if denom != 0:
            self.denominador = denom
        else:
            self.denominador = 1

    def multiplicar(self, outra):
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        return fracao(numerador, denominador)

    def inverter(self):
        return fracao(self.denominador, self.numerador)

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def __repr__(self):
        return f'fracao({self.numerador}, {self.denominador})'

    def __mul__(self, outra):
        return self.multiplicar(outra)

    def __or__(self, outra):
        return self.dividir(outra)

    def __neg__(self):
        return fracao(-self.numerador, self.denominador)


if __name__ == '__main__':
    r = fracao(3, 5)
    print(r)
    lista = [4, 'ninja', r]
    print(lista)

