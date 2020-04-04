class Pessoa:
    #atributo de classe
    olhos = 2

    def __init__(self, *filhos,nome=None,idade=35):
        #atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        #return f'Olá {id(self)}'
        return f'Olá, meu nome é {self.nome}'
    #declarando metodo de classe
    @staticmethod
    def metodo_estatico():
        return 42

    #outra forma de declarar metodo de classe
    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    #sobrescrevendo o metodo cumprimentar para a classe Homem (ação diferente do herdado de Pessoa)

    def cumprimentar(self):
        #chamando e adicionando algo novo do metodo cumprimentar da classe pai
        #cumprimentar_da_classe_pai = self.cumprimentar() #fornece erro de estouro de recursão
        #solução-1
        #cumprimentar_da_classe_pai = Pessoa.cumprimentar(self)
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'

#sobrescrevendo atributos de dados
class Mutante(Pessoa):
    olhos = 3
if __name__ == '__main__':
    #renzo = Homem(nome='renzo')
    renzo = Mutante(nome='renzo')
    #luciano=Pessoa(renzo, nome="Luciano")
    luciano = Homem(renzo, nome="Luciano")
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 2
    print(luciano.olhos)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(id(luciano.olhos), id(Pessoa.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    #return False, homem is pessoa, but pessoa not necessarily homem
    print(isinstance(pessoa, Homem))
    #return True, renzo is homem that inheritance Pessoa
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    #sobrescrevendo métodos
    print(renzo.cumprimentar())
    print(luciano.cumprimentar())