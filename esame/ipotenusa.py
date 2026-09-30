# CALCOLO IPOTENUSA

from math import sqrt
import math

a = 2.5
b = 3.8

c = sqrt(a*a + b*b)

print(a, b, c)

# in questo modo però presupponiamo che l'utente che usa il programma sapppia effettivamente modificare 
# il codice che gli abbiamo fornito in modo da poter modificare i valori dei cateti, per ovviare questo 
# problema possiamo usare la funzione input

from math import sqrt

# a = input("Cateto 1")
# b = input("Cateto 2") 
# se stampassi così il programma darà errore perché non può moltiplicare una stringa, ha bisogno di un 
# numero reale, quindi bisogna aggiungere float, è possibile farlo in due modi:

sa = input("Cateto 1: ")
a = float(sa)
b = float(input("Cateto 2: "))

c = sqrt(a*a + b*b)

print(a, b, c)

# CALCOLO CATETO

from math import sqrt

a = float(input("Cateto 1: "))
c = float(input("Ipotenusa: "))

# noi però dobbiamo prevedere che l'errore umano è possibile e che quindi qualcuno potrebbe inserire un
# cateto più lungo dell'ipotenusa e il pogramma andrebbe in errore, entra in gioco la funzione IF...:
# (controllo condizionale) che ci permette di moficare il percorso del programma in base a ciò che
# accade, è possibile concatenare le varie condizioni attraverso la funzione AND

if a > 0 and c > 0:
    if a > c:
        print("Il cateto non può essere più lungo dell'ipotenusa")
        print("Non è un triangolo valido")

    if a <= c:
        b = sqrt(c*c - a*a)
        print(a, b, c)

# invece che scrivere il caso contrario dell' if, è possibile usare la finzione ELSE:

else:
    print("Il cateto deve avere un valore positivo")

#PER VERIFICARE CHE SIA UN TRIANGOLO RETTANGOLO?

a = float(input("Cateto 1: "))
b = float(input("Cateto 2: "))
c = float(input("Ipotenusa: "))

# spesso però il programma va in errore, o comunque da risposte sbagliate, per via di calcoli tra
# numeri reali molto approssimati, allora usiamo la costante EPSILON molto piccola per verificare
# la differenza tra due numeri reali, oppure usiamo la funzione MATH.ISCLOSE() che definisce una
# tolleranza di differenza tra i due numeri reali, se usata così ci da una tolleranza del 1e-9

from math import isclose

if math.isclose(a*a + b*b, c*c):
    print("È un triangolo rettangolo")
else:
    print("Non è un triangolo rettangolo")
