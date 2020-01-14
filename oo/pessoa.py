class Pessoa:
    #atributo de classe
    olhos = 2

    def __init__(self, *filhos,nome=None,idade=35):
        #atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    luciano=Pessoa(renzo, nome="Luciano")
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
    print(luciano.olhos)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(id(luciano.olhos), id(Pessoa.olhos), id(renzo.olhos))
