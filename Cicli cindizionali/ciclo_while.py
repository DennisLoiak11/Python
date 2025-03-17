#---CICLO WHILE---

#Esercizio 1 - Stampare i numeri interi da 1 a 10 usando un loop while.
n = 1
while n <= 10:
    print(n) 
    n+=1

#Esercizio 3 - Stampare i numeri pari da 2 a 10 usando un loop while.
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

#Esercizio 4 - Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
import random

i = 0
while i == 0:
    numero_casuale = random.randint(1, 10)
    numero = int(input("Inserisci un numero: "))
    if numero == numero_casuale:
        print("Numero indovinato")
        i+=1
    else: 
        print("Ritenta")