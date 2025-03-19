#---CONDIZIONALI IF---

# Esercizio 1 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".
num = input("Inserisci un numero: ")
if num.isnumeric() == True:
    numberInput = int(num)
    if numberInput > 0:
        print(f"{numberInput} è positivo")
    elif numberInput == 0:
        print(f"{numberInput} è uguale a 0")
else:
    print(f"{num} non è un numero o è un numero negativo")

#Esercizio 2 - Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".
primo_numero = input("Inserisci il primo numero: ")
secondo_numero = input("Inserisci il secondo numero: ")
if primo_numero > secondo_numero:
    print(f"{primo_numero} è maggiore di {secondo_numero}")
elif primo_numero < secondo_numero:
        print(f"{primo_numero} è minore di {secondo_numero}")
else:
     print("i numeri inseriti sono uguali")
 
# Esercizio 3 - Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".
parola_verifica = input("Inserisci una parola: ")
if not parola_verifica:
    print("La stringa è vuota")
else:
    print("La stringa non è vuota")

# Esercizio 4 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".
pari_dispari = int(input("Inserisci un numero: "))
if pari_dispari % 2 == 0:
    print(f"{pari_dispari} è pari")
else:
    print(f"{pari_dispari} è dispari")

# # Esercizio 5 - Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
lettera = input("Inserisci una lettera: ")
if lettera in "aeiou":
    print(f"{lettera.upper()} è una vocale")
else:
    print(f"{lettera.upper()} è una consonante")

# # Esercizio 6 - Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
numero = int(input("Inserisci un numero: "))
if numero <= 10 and numero >= 1:
    print(f"Il numero {numero} è compreso tra 1 e 10")
else:
    print(f"Il numero {numero} non è compreso tra 1 e 10")