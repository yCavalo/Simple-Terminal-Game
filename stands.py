import random
import time

dado =  random.randint(1, 220)

class stands:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
        self.especial = None


class Player:
    def __init__(self, stand):
        self.nome = "Você"
        self.stand = stand
        self.vida = 150

    def bater(self, alvo):
        dano = random.randint(1, self.stand.dano)
        alvo.vida -= dano
        if(alvo.vida <= 0):
            print("\n{} matou {}" .format(self.nome, alvo.nome))
            alvo.vida = 0
            return;
        print("\n{} deu {} de dano" .format(self.stand.nome, dano))
  
class Inimigo:
    def __init__(self):
        self.nome = "Inimigo"
        self.vida = 200
        self.dano = 35

    def bater(self, alvo):
        dano = random.randint(1, self.dano)
        alvo.vida -= dano
        print("O {} deu {} de dano\n" .format(self.nome, dano))

#Stands da Parte 3:
Star_Platinum = stands("Star Platinum", 60)
Silver_Chariot = stands("Silver Chariot", 45)
Za_Warudo = stands("The World", 60)
#Stands da Parte 4:
Crazy_Diamond = stands("Crazy Diamond", 55)
The_Hand = stands("The Hand", 50)
Killer_Queen = stands("Killer Queen", 45)
#Stands da Parte 5:
Gold_Experience = stands("Gold Experience", 35)
King_Crimson = stands("King Crimson", 50)
#Stands da Parte 6:
Stone_Free = stands("Stone Free", 30)
Whitesnake = stands("Whitesnake", 25)
#Stands da Parte 7:
Tusk = stands("Tusk", 50)
Dirty_Deeds_Done_Dirt_Cheap = stands("D4C", 45)
#Stands da Parte 8:
Soft_And_Wet = stands("Soft & Wet", 45)
Wonder_Of_U = stands("Wonder Of U", 25)