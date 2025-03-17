#Esercizio 1 - Creare una lista vuota e assegnarla a una variabile.
x = []

#Esercizio 2 - Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.
numeri = [1, 2, 3, 4, 5]

#Esercizio 3 - Accedere all'elemento con indice 2 della lista precedente.
numeri[2]

#Esercizio 4 - Aggiungere un nuovo elemento "6" alla lista precedente.
numeri.append(6)

#Esercizio 5 - Rimuovere l'elemento con indice 3 dalla lista precedente.
numeri.pop(3)

#Esercizio 6 - Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
y = numeri[:3]
print(y)

#Esercizio 7 - Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
dispari = numeri[1::2]

#Esercizio 8 - Ordinare la lista precedente in ordine decrescente.
dispari.sort(reverse = True)
print(dispari)

#Esercizio 9 - Contare quante volte l'elemento "2" appare nella lista precedente.
conto = 0
for x in dispari:
    if x == 2:
        conto += 1
print(f"Dispari: {dispari}")
print(f"Il 2 appare {conto} volte")