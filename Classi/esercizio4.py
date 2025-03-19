#Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.marticola = matricola
        self.stipendio = stipendio

    def stampa_dettaglio(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.marticola}, stipendio: {self.stipendio} Euro")
    
    def aumenta_stipendio(self):
        aumento = (self.stipendio / 10) * 100
        self.stipendio += aumento
        print(f"{self.nome} {self.cognome} ha ricevuto un aumento del 10%")

impiegato1 = Impiegato("Mario", "Rossi", 12345, 1500)
impiegato1.stampa_dettaglio()
impiegato1.aumenta_stipendio()
impiegato1.stampa_dettaglio()