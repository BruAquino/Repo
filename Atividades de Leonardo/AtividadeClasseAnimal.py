class Animal:
    def __init__(self, nome, especie, idade, peso, sexo):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.sexo = sexo

    def fazerSom(self):
        print (F"{nome} fez um barulho.")
    def comer(self):
        print(F"{nome} comeu algo.")
    def andar(self):
        print(F"{nome} andou.")
    def dormir(self):
        print(F"{nome} dormiu.")

animal1 = Animal(nome = "Alfredo", especie = "Rinoceronte", idade = 23, peso = 790, sexo = "feminino")

print ("testes do animal")
print(" ")
print(animal1.nome)
print(animal1.especie)
print(animal1.idade)
print(animal1.peso)
print(animal1.sexo)

print(" ")
class Cavalo(Animal):
    def __init__(self, nome, especie, idade, peso, sexo, raca  ):
        super().__init__(nome, especie, idade, peso, sexo)
        self.raca = raca

    def galopar(self):
        print (F"{nome} Galopou.")

    def coice(self):
        print (F"{nome} Deu um coice em alguém")

cavalo1 = Cavalo(nome = "Eustáquio", especie = "Cavalo", idade = 23, peso = 12, sexo = "feminino", raca = "Alter-Real")

print ("testes do cavalo")
print(" ")
print(cavalo1.nome)
print(cavalo1.especie)
print(cavalo1.idade)
print(cavalo1.peso)
print(cavalo1.sexo)
print(cavalo1.raca)
