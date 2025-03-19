#---CICLO FOR---

#Esercizio 1 - Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
numeri = [1, 2, 3, 4, 5]
for n in numeri:
    print(n)

#Esercizio 2 - Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
for n in range(10):
    n += 1 
    print(n)

#Esercizio 3 - Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
numeri = [1, 2, 3, 4, 5]
somma = 0
for n in numeri:
    somma += n
print(f"La somma è {somma}")

#Esercizio 4 - Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.
for n in range(2, 21):   
    if n % 2 == 0:
        print(n)


#Esercizio 5 - Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
stringa = "ciao"
for char in stringa:
    print(char)


#Esercizio 6 - Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
for key in dizionario:
    print(key)


#Esercizio 7 - Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
for chiave, valore in dizionario.items():
    print(chiave, ":", valore)

#Esercizio 8 - Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.
lista = ["ciao", "a", "tutti"]
for parola in lista:
    for char in parola:
        print(char)


#Esercizio 9 - Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
conteggio_a = 0
parola = "aiuola"
for char in parola:
    if char == "a":
        conteggio_a += 1
print(conteggio_a)        


#Esercizio 10 - Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.
numeri = [1, 2, 3, 4, 5]
somma = 0
for n in numeri:
    somma += n
media = somma / len(numeri)
print(media)