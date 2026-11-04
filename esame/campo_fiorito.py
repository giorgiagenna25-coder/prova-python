# ESERCIZIO
# Campo Fiorito
"""
campo = [
    [False, True, True, False]
    [False, False, False, False]
    [True, False, False, True]
    [False, True, False, False]
]
"""
# M = 5

N = int(input("Lato del campo: "))
M = int(input("Numero di fiori: "))

print("Punto 1")
campo = []
for riga in range(N):
    nuova = []
    for colonna in range(N):
        nuova.append(False)
    campo.append(nuova)

"""
Per stampare bene una tabella:
for riga in campo:
    print(riga)
oppure usi la funzione pprint()
"""
from pprint import pprint
pprint(campo)

print("Punto 2")
# Posizione M fiori nel campo a caso
import random

for fiore in range(M):
    riga_fiore = random.randint(0, N-1)
    colonna_fiore = random.randint(0, N-1)
    print(riga_fiore, colonna_fiore) #posizione del fiore
    
    while campo[riga_fiore][colonna_fiore] == True: 
        #se inserisco while al posto di if controlla anche i nuovi valori asseggati dopo il nuovo 
        #sorteggio
        riga_fiore = random.randint(0, N-1)
        colonna_fiore = random.randint(0, N-1)
    
    campo[riga_fiore][colonna_fiore] = True

pprint(campo)

print("Punto 3")
#per stampare il campo con i disegnini
for riga in range(N):
    for colonna in range(N):
        if campo[riga][colonna]:
            print("🌸", end="")
        else:
         print("🟢", end="")
    print()


print("Punto 4")
#per calcolare gli adiacenti a ciascuna colonna:
vicini = []
for riga in range(N):
    nuova_riga = []
    for colonna in range(N):
        #calcolare fiori vicini (valori True) a campo[riga][colonna]
        n_vicini = 0
        #visito tutte le caselle vicine ad ogni True e incremento n_incremento
        for delta_riga in [-1, 0, 1]:
            for delta_colonna in [-1, 0, -1]:
                if (
                    (delta_riga != 0 or delta_colonna != 0) and
                    riga + delta_riga >= 0 and
                    riga + delta_riga < N and
                    colonna + delta_colonna >= 0 and
                    colonna + delta_colonna < N
                ):
                    if campo[riga + delta_riga][colonna + delta_colonna] == True:
                        n_vicini += 1
        nuova_riga.append(n_vicini)
    vicini.append(nuova_riga)
pprint(vicini)