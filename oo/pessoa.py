class Pessoa:
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
   jessica = Pessoa(nome='Jessica')
   pedro = Pessoa(jessica, nome='Pedro')
   print(Pessoa.cumprimentar(pedro))
   print(id(pedro))
   print(pedro.cumprimentar())
   print(pedro.nome)
   print(pedro.idade)
   for filho in pedro.filhos:
       print(filho.nome)