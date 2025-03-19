#Esercizio 1 - Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.
def fai_somma(lista_num):
    return sum(lista_num)
print(fai_somma([1, 2, 3, 4, 5]))


#Esercizio 2 - Scrivi una funzione che prende una stringa e restituisce la stringa invertita.
def parola_inversa(parola):
    print(parola[::-1])
parola_inversa("Roma")

#Esercizio 3 - Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.
def starts_with(lista):
    lista_a = []
    for parola in lista:
        if parola[0] == "A" or parola[0] == "a":
            lista_a.append(parola)
    return lista_a

print(starts_with(["Amore", "Roma", "aiuola", "Acquilone", "ramo", "aereo"]))


#Esercizio 4 - Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.
def numeri_pari(numeri):
    lista_numeri_pari = []
    for n in numeri:
        if n%2 == 0:
            lista_numeri_pari.append(n)
    return lista_numeri_pari

print(numeri_pari([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


#Esercizio 5 - Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.
def lenght(lista_parole):
    lista_lunghezze = []
    for parola in lista_parole:
        lista_lunghezze.append(len(parola))
    return lista_lunghezze
print(lenght(["Amore", "Roma", "aiuola", "Acquilone", "ramo", "aereo"]))


#Esercizio 6 - Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.
def valore_massimo(lista_num):
    return max(lista_num)

print(valore_massimo([1, 34, 76, 43, 90, 21]))


#Esercizio 7 - Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.
def parola_lenght(parole):
    parola_lunga = ""
    for parola in parole:
        if len(parola) > len(parola_lunga):
            parola_lunga = parola
    return parola_lunga

print(parola_lenght(["Amore", "Roma", "aiuola", "Acquilone", "ramo", "aereo"]))        


#Esercizio 8 - Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.
def media_num(lista_num):
    somma = 0
    for n in lista_num:
        somma += n
    avg = somma / len(lista_num)
    return avg

print(media_num([3, 9]))


#Esercizio 10 - Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.
def maggiore(lista):
    lista_n_max = []
    for n in lista:
        if n > 6:
            lista_n_max.append(n)
    return lista_n_max

print(maggiore([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))