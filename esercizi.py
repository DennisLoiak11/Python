# #---OPERATORI MATEMATICI---

# #Esercizio 1
# numero1 = 1
# numero2 = 2
# somma = numero1 + numero2
# print(somma)

# #Esercizio 6 - Eseguire l'operazione di modulo tra le due variabili e assegnare il risultato ad una nuova variabile "resto". Mandare a schermo.
# numero1 = 10
# numero2 = 5
# resto = numero1 % numero2
# print(resto)

# #Esercizio 7 - Incrementare "numero1" di 1 e decrementare "numero2" di 3. Mandare a schermo i nuovi valori.
# numero1 += 1
# numero2 -= 3
# print(numero1, numero2)


# #---METODI DI STRINGHE---

# #Esercizio 1 - Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.
# stringa = "ciao mondo!"
# stringa_maiuscola = stringa.upper()
# print(stringa_maiuscola)

# #Esercizio 2 - Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile
# stringa = "BENVENUTI A ROMA"
# stringa_minuscola = stringa.lower()
# print(stringa_minuscola)

# #Esercizio 3 - Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per dividere la stringa in una lista di parole.
# stringa = "Il meglio deve ancora venire"
# stringa_splittata = stringa.split(" ")
# print(stringa_splittata)

# #Esercizio 4 - Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World" con "Python".
# stringa = "Hello World"
# print(stringa.replace("World", "Python"))

# #Esercizio 5 - Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa..
# stringa = "  Ciao  "
# print(stringa)
# print(stringa.strip())

# #Esercizio 6 - Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
# stringa = "abcdefg"
# print(stringa[:3])

# #Esercizio 7 - Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".
# stringa = "Python"
# print(stringa.startswith("Py"))

# #Esercizio 8 - Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.
# stringa = "Ciao mondo"
# print(stringa.count("o"))

# #Esercizio 9 - Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".
# stringa = "Ciao mondo"
# risultato = stringa[-5:].upper().replace("O", "K")
# print(risultato)


# #---FORMATTAZIONE STRINGHE---

# #Esercizio 1 - Creare due variabili "nome" e "cognome" e concatenarle a schermo.
# nome = "Dennis"
# cognome = "De Biasi"
# print(nome + " " + cognome)

# #Esercizio 2 - Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".
# stringa = "Il numero è {}"
# numero = 42
# print(stringa.format(numero))

# #Esercizio 3 - Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". Per il binario utilizzare bin(numero)
# stringa = "Il numero binario di {} è {}".format(42, bin(numero))
# print(stringa)

# #Esercizio 4 - Partendo dalla variabile "numero" uguale a 5, utilizzare le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".
# numero = 5
# stringa = f"Il quadrato di {numero} è {numero*numero}"
# print(stringa)

# #Esercizio 5 - Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere "Il mio nome è {nome} ed il cognome è {cognome}". Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.
# stringa = f"il mio nome è {nome} e il mio cognome è {cognome}"
# print(stringa)


# #---CONDIZIONALI IF---

# #Esercizio 1 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".
# # num = input("Inserisci un numero: ")
# # if num.isnumeric() == True:
# #     numberInput = int(num)
# #     if numberInput > 0:
# #         print(f"{numberInput} è positivo")
# #     elif numberInput == 0:
# #         print(f"{numberInput} è uguale a 0")
# # else:
# #     print(f"{num} non è un numero o è un numero negativo")

# # Esercizio 2 - Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".
# # primo_numero = input("Inserisci il primo numero: ")
# # secondo_numero = input("Inserisci il secondo numero: ")

# # if primo_numero > secondo_numero:
# #     print(f"{primo_numero} è maggiore di {secondo_numero}")
# # elif primo_numero < secondo_numero:
# #         print(f"{primo_numero} è minore di {secondo_numero}")
# # else:
# #      print("i numeri inseriti sono uguali")

# # Esercizio 3 - Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".
# # parola_verifica = input("Inserisci una parola: ")
# # if not parola_verifica:
# #     print("La stringa è vuota")
# # else:
# #     print("La stringa non è vuota")


# # Esercizio 4 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".
# pari_dispari = int(input("Inserisci un numero: "))
# if pari_dispari % 2 == 0:
#     print(f"{pari_dispari} è pari")
# else:
#     print(f"{pari_dispari} è dispari")

# # Esercizio 5 - Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
# lettera = input("Inserisci una lettera: ")
# if lettera in "aeiou":
#     print(f"{lettera.upper()} è una vocale")
# else:
#     print(f"{lettera.upper()} è una consonante")

# # Esercizio 6 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
# numero = int(input("Inserisci un numero: "))
# if numero <= 10 and numero >= 1:
#     print(f"Il numero {numero} è compreso tra 1 e 10")
# else:
#     print(f"Il numero {numero} non è compreso tra 1 e 10")


#---CICLO FOR---


#Esercizio 1 - Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.
# numeri = [1, 2, 3, 4, 5]
# for n in numeri:
#     print(n)

#Esercizio 2 - Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.
# for n in range(10):
#     n += 1 
#     print(n)

#Esercizio 3 - Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.
# numeri = [1, 2, 3, 4, 5]
# somma = 0
# for n in numeri:
#     somma += n
# print(f"La somma è {somma}")

#Esercizio 4 - Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.
# for n in range(2, 21):   
#     if n % 2 == 0:
#         print(n)


#Esercizio 5 - Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.
# stringa = "ciao"
# for char in stringa:
#     print(char)


#Esercizio 6 - Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
# dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
# for key in dizionario:
#     print(key)


#Esercizio 7 - Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
# dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
# for chiave, valore in dizionario.items():
#     print(chiave, ":", valore)

#Esercizio 8 - Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.
# lista = ["ciao", "a", "tutti"]
# for parola in lista:
#     for char in parola:
#         print(char)


#Esercizio 9 - Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.
# conteggio_a = 0
# parola = "aiuola"
# for char in parola:
#     if char == "a":
#         conteggio_a += 1
# print(conteggio_a)        


#Esercizio 10 - Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.
# numeri = [1, 2, 3, 4, 5]
# somma = 0
# for n in numeri:
#     somma += n
# media = somma / len(numeri)
# print(media)


#---CICLO WHILE---

#Esercizio 1 - Stampare i numeri interi da 1 a 10 usando un loop while.
# n = 1
# while n <= 10:
#     print(n) 
#     n+=1


#Esercizio 3 - Stampare i numeri pari da 2 a 10 usando un loop while.
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

#Esercizio 4 - Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
# import random

# i = 0
# while i == 0:
#     numero_casuale = random.randint(1, 10)
#     numero = int(input("Inserisci un numero: "))
#     if numero == numero_casuale:
#         print("Numero indovinato")
#         i+=1
#     else: 
#         print("Ritenta")