#Esercizio 1 - Creare un set vuoto e assegnarlo a una variabile.
set_vuoto = set()


#Esercizio 2 - Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
set_frutta = {"mela", "banana", "kiwi", "mela"}


#Esercizio 3 - Aggiungere l'elemento "pesca" al set precedente.
set_frutta.add("pesca")


#Esercizio 4 - Rimuovere l'elemento "mela" dal set precedente.
set_frutta.discard("mela")

print(set_frutta)

#Esercizio 5 - Verificare se l'elemento "ananas" è presente nel set precedente.
if "ananas" in set_frutta:
    print("ananas presente")
else:
    print("ananas assente")


#Esercizio 6 - Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".
set_frutta = {"banana", "kiwi", "arancia"}


#Esercizio 7 - Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().
set_numeri = set(range(1, 6))
print(set_numeri)

#Esercizio 8 (difficile) - Creare un nuovo set contenente i numeri pari del set precedente.
set_pari = set()
for n in set_numeri:
    if n%2 == 0:
        set_pari.add(n)
print(f"Numeri pari: {set_pari}")