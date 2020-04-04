"""
aula - Composicao
criar uma classe carro que deverá possuir dois
atributos compostos por outras duas classes

1- motor
2 - direção

o motor terá a responsabilidade de controlar a velocidade
ele possui os seguintes atributos
atributo de dado velocidade
metodo acelerar que irá incrementar a velocidade em uma unidade
metodo frear que irá decrementar a velocidade em duas unidades
A direção terá a responsabildade de controlar a direção.
ela terá os seguintes atributos: norte, sul, leste , oeste
metodo virar a direita
metodo virar a esquerda
Exempo

    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self. motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dic = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dic = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dic[self.valor]
        # if self.valor == NORTE:
        # self.valor = LESTE
        # elif self.valor == LESTE:
        # self.valor = SUL
        # elif self.valor == SUL:
        # self.valor = OESTE
        # elif self.valor == OESTE:
        # self.valor = NORTE

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dic[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
