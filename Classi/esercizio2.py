# Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    
    def fai_verso(self):
        if self.specie == "cane":
            print(f"{self.nome} Bau!")
        elif self.specie == "gatto":
            print(f"{self.nome} Maio!")

cane = Animale("fuffy", "cane")
gatto = Animale("tom", "gatto")

cane.fai_verso()
gatto.fai_verso()
