#ESERCIZIO 1
# scrivere la frase, input, trovare solo le lettere maiuscole
"""
frase = input("Inserire una frase: ")

for carattere in frase:
    if carattere.isupper():
        print(carattere)

for indice, carattere in enumerate(frase):
    if indice % 2 == 1:
        print(carattere)

vocali = "aeiouAEIOU"
risultato = ""
for carattere in frase:
    if carattere in vocali:
        risultato = risultato + "_"
    else:
        risultato = risultato + carattere
print(risultato)

conteggio = 0
numeri = "1234567890"
for caratteri in frase:
    if caratteri in numeri:
        conteggio = conteggio + 1
print(conteggio)

vocali = "aeiouAEIOU"
for indice, carattere in enumerate(frase):
    if carattere in vocali:
        print(indice)
"""

# ESERCIZO 2
"""
parola = input("Inseire parola: ")

for indice in range (len(parola) - 1 , -1 , -1):
    print(parola[indice])
oppure
print(parola[::-1])

for indice in range (len(parola) - 1 , -1 , -1):
    carattere = parola[indice]
    if carattere.isupper():
        print(carattere)
"""

# ESERCIZIO 3
"""
PIN = "1234"
tentativi = 0

while tentativi < 3:
    PIN_inserito = input("Inserire PIN: ")
    if PIN_inserito == PIN:
        print("Il PIN è corretto")
        break
    else:
        print("Il PIN non è corretto")
    tentativi = tentativi + 1
    if tentativi == 3:
        print("La carta è bloccata")
"""

# ESERCIZIO 4
"""
parola = input("Inserire una parola: ")
# scivi tutte le sottostringhe della parola, prima slice 1 carattere, poi slide di 2 caratteri, poi
# slice di 3, fino a slice len(parola)
lun = len(parola)
sottostringa = ""
n = 0
while n <= lun:
    for i in range(lun - n +1):
        sottostringa += parola[i : i+n] +"\n"
    n += 1
print(sottostringa)
"""