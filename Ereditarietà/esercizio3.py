#Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() in modo appropriato per ogni forma. Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.

class Forma():

    def area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__()
        self.lato = lato
    
    def area(self):
        print(self.lato * self.lato)    
class Rettangolo(Forma):
    def __init__(self, altezza, larghezza):
        super().__init__()
        self.altezza = altezza
        self.larghezza = larghezza
    
    def area(self):
        print(self.altezza * self.larghezza)

quadrato = Quadrato(5)
quadrato.area()

rettangolo = Rettangolo(3, 6)
rettangolo.area()