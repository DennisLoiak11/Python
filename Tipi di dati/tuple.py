#Esercizio 1 - Creare una tupla vuota e assegnarla a una variabile.
tupla = ()

#Esercizio 2 - Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
x = ("mela", "banana", "kiwi")

#Esercizio 3 - Accedere all'elemento "banana" della tupla precedente.
print(x[1])

#Esercizio 4 - Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.
y = x[:2]
print(y)

#Esercizio 5 - Verificare se l'elemento "ananas" è presente nella tupla precedente.
if "ananas" in x:
    print("Presente")
else:
    print("Assente")

#Esercizio 6 - Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").
nuova_tupla = ("pesca", "arancia")
tupla_concat = x + nuova_tupla
print(tupla_concat)

#Esercizio 7 - Verificare la lunghezza della tupla precedente.
print(len(tupla_concat))

#Esercizio 8 - Creare una tupla contenente i numeri interi da 1 a 5.
numeri = (1, 2, 3, 4, 5)

#Esercizio 9 (difficile) - Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
numeri_quadrati = tuple(x ** 2 for x in range(1, 6))
print(numeri_quadrati)

#Esercizio 10 - Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.
conta = x.count("mela")
print(conta)