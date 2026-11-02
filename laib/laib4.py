# ESERCIZIO 1
# I.
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


for i in range(len(tabella)):
    for j in range(len(tabella[0])):
        print(tabella[i][j], end=" , ")
