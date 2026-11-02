# ESERCIZIO 1
# I.
print("Punto I.")

tabella = []
RIGHE = int(input("Inserire il numero di righe: "))
COLONNE = int(input("Inserire il numero di colonne: "))

for i in range(RIGHE):
    righe = [0] * COLONNE
    tabella.append(righe)
print()

#Tabella per righe:
for riga in tabella:
    print(riga)

"""
Per stampare tutti gli elementi di una tabella in una sola riga susseguiti ogni volta da quello che
vuoi da mettere dentro le virgolette dell'end:

for i in range(len(tabella)):
    for j in range(len(tabella[0])):
        print(tabella[i][j], end=" , ")
"""
print()

# II.
print("Punto II.")

for i in range(RIGHE):
    for j in range(COLONNE):
        tabella[i][j] = 1

for riga in tabella:
    print(riga)

print()

#III.
print("Punto III.")

for i in range(RIGHE):
    for j in range(COLONNE):
        tabella[i][j] = (i + j) % 2 #così assegna ad ogni valore della tabella il valore della somma
                                    #degli indici il cui risultato viene diviso per due e poi viene
                                    #preso il resto, se c'è resto viene 1, sennò assegna 0 

for riga in tabella:
    print(riga)

print()

#IV.
print("Punto IV.")

for i in range(RIGHE):
    if i == 0 or i == len(tabella) - 1:
        for j in range(COLONNE):
            tabella[i][j] = 0

for riga in tabella:
    print(riga)

print()

#V.
print("Punto V.")

for i in range(RIGHE):
    for j in range(COLONNE):
        if j == 0 or j == RIGHE:
            tabella[i][j] = 1

for riga in tabella:
    print(riga)

print()

# VI.
print("Punto VI.")

somma = 0
for i in range(RIGHE):
    for j in range(COLONNE):
        somma += tabella[i][j]

print("La sooma dei vaolori è: ", somma)