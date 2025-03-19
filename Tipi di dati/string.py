# #Esercizio 1 - Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.
stringa = "ciao mondo!"
stringa_maiuscola = stringa.upper()
print(stringa_maiuscola)

# #Esercizio 2 - Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile
stringa = "BENVENUTI A ROMA"
stringa_minuscola = stringa.lower()
print(stringa_minuscola)

# #Esercizio 3 - Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per dividere la stringa in una lista di parole.
stringa = "Il meglio deve ancora venire"
stringa_splittata = stringa.split(" ")
print(stringa_splittata)

# #Esercizio 4 - Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World" con "Python".
stringa = "Hello World"
print(stringa.replace("World", "Python"))

# #Esercizio 5 - Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..
stringa = "  Ciao  "
print(stringa)
print(stringa.strip())

# #Esercizio 6 - Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
stringa = "abcdefg"
print(stringa[:3])

# #Esercizio 7 - Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".
stringa = "Python"
print(stringa.startswith("Py"))

# #Esercizio 8 - Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.
stringa = "Ciao mondo"
print(stringa.count("o"))

# #Esercizio 9 - Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".
stringa = "Ciao mondo"
risultato = stringa[-5:].upper().replace("O", "K")
print(risultato)


# #---FORMATTAZIONE STRINGHE---

# #Esercizio 1 - Creare due variabili "nome" e "cognome" e concatenarle a schermo.
nome = "Dennis"
cognome = "De Biasi"
print(nome + " " + cognome)

# #Esercizio 2 - Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".
stringa = "Il numero è {}"
numero = 42
print(stringa.format(numero))

# #Esercizio 3 - Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". Per il binario utilizzare bin(numero)
stringa = "Il numero binario di {} è {}".format(42, bin(numero))
print(stringa)

# #Esercizio 4 - Partendo dalla variabile "numero" uguale a 5, utilizzare le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".
numero = 5
stringa = f"Il quadrato di {numero} è {numero*numero}"
print(stringa)

# #Esercizio 5 - Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere "Il mio nome è {nome} ed il cognome è {cognome}". Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.
stringa = f"il mio nome è {nome} e il mio cognome è {cognome}"
print(stringa)