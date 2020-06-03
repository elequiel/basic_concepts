# funcoes de classe sao superiores de funcao de instancia
# para criar funcao de classe e necessario acima da funcao @classmethod
# 
class Gato():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def miar(self):
        return print("Miauu, miauu")


    def andar(self):
        return print(f"{self.nome} esta andando.... \n.....cansei")

gato = Gato("Joane", 4)

class Cliente():
    def __init__(self):
        self.nome = ""
        self.cpf = 0

        self.cofre = Cofre()

class Cofre():
    def __init__(self):
        pass