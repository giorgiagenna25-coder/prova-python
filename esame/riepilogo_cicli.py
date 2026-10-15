# RIEPILOGO CICLI WHILE, FOR, FOR IN RANGE

#       while condizione:
#           corpo
# La condizione cambia sempre, fino ad un certo punto è vera, poi diventa falsa e quindi il ciclo si
#   interrompe, dipende dalla variabile di controllo 
# La variabile di controllo (i) deve essere definita prima dell'ingresso del ciclo e all'interno del
#   ciclo deve essere definita una legge secondo quale essa si aggiorna (es.i=i+1), comunemente é
#   chiamata contatore
"""
# ESERCIZIO 1
# inserire un numero intero positivo
#   se non fosse positivo, ripetere la richiesta
x = int(input("Numero: "))
while x <= 0:
    print("Dovevi inserire un numero intero positivo")
    x = int(input("Numero: "))

# ESERCIZIO 2
# Inserire 10 numeri interi
# Calcolare il valore dato dalla somma di tutti i numeri pari meno la somma dei numeri dispari
pari = 0
dispari = 0
i = 0 
while i < 10:
    x = int(input("Numero: "))
    if x % 2 == 0:
        pari = pari + x
    else:
        dispari = dispari + x
    i = i + 1
print("La somma dei pari è ", pari)
print("La somma dei dispari è ", dispari)
differenza = print("La differenza tra le somme è ", pari - dispari)

# questo esercizio poteva essere risolto anche con il ciclo FOR
for i in range(10):
    x = int(input("Numero: "))
    if x % 2 == 0:
            pari = pari + x
    else:
            dispari = dispari + x

#ESERCIZIO 3
# contare il munero di lettere maiscuole di una parola
s = input("Parola: ")
maiuscole = 0
for i in s:
     if i.isupper():
          maiuscole += 1
print("Il numero di maiuscole è ", maiuscole)

#oppure:
i = 0 
while i < len(s):
    if s[i].isupper():
        maiuscole += 1
    i += 1
print(maiuscole)

# ESERCIZIO 4
# inserire 10 numeri interi
# calcolare la differenza delle somme di tutti i numeri in posizione pari meno la somma di quelli in
# poszione dispari

# ESERCIZIO 5
# scrivere 10 numeri interi
# dire se erano tutti pari
conta = 0
for i in range(10):
    x = int(input("Numero: "))
    if x %2 == 0:
        conta = conta + 1 #conta quanti sonno i pari
        print("Questo numero è pari")
if conta == 10:
    print("Tutti i numeri sono pari")
else:
    print("Non tutti i numeri sono pari")

# oppure
tutti_pari = True
for i in range(10):
    x = int(input("Numero: "))
    if x %2 == 1:
        tutti_pari = False

if tutti_pari:
    print("Tutti i numeri sono pari")
else:
    print("Non tutti i numeri sono pari")

#ESERCIZIO 7
# cancellare tutte le lettere maiscuole da una una stringa
s = input("Stringa: ")
# ciaoOOOOO a tuttiII
# una stringa no può essere modificata, ma si può creare una nuva con le modifiche necessarie
nuova = ""
for ch in s:
    if not ch.isupper():
        nuova += ch
print(nuova)
"""
# ESERCIZIO 8
# sostituire a tutti le cifre con la cifra successiva (es. 3 --> 4, 4 --> 5, 9 --> 0), non vuol dire
# che tutta la stringa sia formata da cifre
s = input("Stringa alfanumerica: ")
nuova = ""
for ch in s:
    if ch.isdigit():
        if ch == "9":
            new_ch = "0"
        else:
            new_ch = str(int(ch) + 1)
    else:
        new_ch = ch
    nuova += new_ch
print(nuova)