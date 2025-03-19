#Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore()

class Veicolo():
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def accelera(self):
        print("Sto accelerando")

    def frena(self):
        print("Sto frenando")

    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}" 

# class Auto(Veicolo):
#     def __init__(self, marca, modello, anno, colore):
#         super().__init__(marca, modello, anno)

#     def cambia_colore(self, nuovo_colore):
#         self.colore = nuovo_colore

#Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo, in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”.

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore

    def cambia_colore(self, nuovo_colore):
        self.colore = nuovo_colore
    
    def __str__(self):
        return super().__str__() + f", Colore: {self.colore}"
    
auto1 = Auto("Audi", "A2", 2003, "Grigio")    
auto1.accelera()
auto1.frena()
print(auto1.__str__())