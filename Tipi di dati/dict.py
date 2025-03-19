#Esercizio 1 - Creare un dizionario vuoto e assegnarlo a una variabile.
primo_dict = dict()
print(type(primo_dict))


#Esercizio 2 - Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
user = {
    "nome" : "Mario",
    "cognome" : "Rossi",
    "età" : 30
}


#Esercizio 3 - Accedere al valore dell'elemento con chiave "età" del dizionario precedente.
print(user["età"])


#Esercizio 4 - Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.
user.update({"email" : "mario.rossi@email.com"})


#Esercizio 5 - Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
user.pop("cognome")
print(user)


#Esercizio 6 - Creare una nuova lista che contenga solo le chiavi del dizionario precedente.
list_keys = []
list_keys.append(user.keys())
print(list_keys)


#Esercizio 7 - Creare una nuova lista che contenga solo i valori del dizionario precedente.
list_values = []
list_values.append(user.values())
print(list_values)


#Esercizio 8 - Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
user.update({"età" : 35})
print(user)


#Esercizio 9 - Contare il numero di elementi nel dizionario precedente.
print(len(user))