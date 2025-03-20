persona = {
    "nome" : "Dennis",
    "cognome" : "De Biasi",
    "eta" : 21
}

operazioni = ("Aggiungere", "Modificare", "Eliminare", "Svuotare")

def start():
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Aggiungi chiave e valore separati da una virgola: ")
        aggiungi(x.split(","))
    
    elif operazione == operazioni[1]:
        print(persona)
        chiave_modifica = input("Quale chiave vuoi modificare? ")
        valore_modifica = input("Inserisci il nuovo valore: ")
        modifica(chiave_modifica, valore_modifica)
    
    elif operazione == operazioni[2]:
        print(persona)
        chiave_cancella = input(f"Quale chiave vuoi eliminare? ")
        elimina(chiave_cancella)
    
    elif operazione == operazioni[3]:
        conferma = input("Sei sicuro di voler eliminare tutti i dati presenti nel dict? ")
        if conferma == "si":
            svuota()


def aggiungi(list):
    chiave = list[0]
    valore = list[1]
    persona[chiave] = valore
    print(persona)

def modifica(param1, param2):
    chiave = param1
    valore = param2
    persona[chiave] = valore
    print(persona)

def elimina(param):
    persona.popitem(param)
    print(persona)

def svuota():
    persona.clear()
    print(persona)

while True:
    start()