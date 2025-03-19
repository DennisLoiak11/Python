#Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni")

persona1 = Persona("Marco", 32)
persona1.presentati() 