#ESERCIZI
"""
righe = int(input("Inserire il numero di righe: "))
col = int(input("Inserire il numero di colonne: "))
tabella = []

print("Punto 1")
for i in range(righe):
    riga = [0] * col
    tabella.append(riga)
for riga in tabella:
    print(riga)

print()

print("Punto 2")
for i in range(righe):
    for j in range(col):
        tabella[i][j] = 1
for riga in tabella:
    print(riga)

print()

print("Punto 3")
for i in range(righe):
    for j in range(col):
        if (i+j)%2 == 0:
            tabella[i][j]= 0
        else:
            tabella[i][j]= 1
for riga in tabella:
    print(riga)

print()

print("Punto 4")
for i in range(righe):
    for j in range(col):
        if i == 0 or i == righe-1:
            tabella[i][j]= 0
for riga in tabella:
    print(riga)

print()

print("Punto 5")
for i in range(righe):
    for j in range(col):
        if j == 0 or j == col-1:
            tabella[i][j]= 1
for riga in tabella:
    print(riga)

print()

somma = 0
print("Punto 6")
for i in range(righe):
    for j in range(col):
        somma += tabella[i][j]
print(somma)


#ESERCIZI
nomi = ['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']
cognomi = ['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']

uniti = []
for i in range(len(nomi)):
        completo = nomi[i] + " " + cognomi[i]
        uniti.append(completo)
print(uniti)


#ESERCIZIO
supereroi = [
    "Peter Parker",
    "Clark Kent",
    "Bruce Wayne",
    "Tony Stark",
    "Steve Rogers",
    "Diana Prince",
    "Barry Allen",
    "Arthur Curry"
]

nomi = []
cognomi = []
for sup in supereroi:
    separati = sup.split(" ")
    nomi.append(separati[0])
    cognomi.append(separati[1])
print(nomi)
print(cognomi)
"""

#ESERCIZIO
luoghi = [
    ['Torino', 'Torino', 'Aosta', 'Aosta', 'Milano', 'Milano', 'Torino'],
    ['Milano', 'Torino', 'Milano', 'Aosta', 'Torino', 'Torino', 'Torino'],
    ['Milano', 'Torino', 'Aosta', 'Aosta', 'Genova', 'Genova', 'Torino'],
]
GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
for giorno in range(len(luoghi[0])):
    tutti_qui = True
    for a in range(1, len(luoghi)):
        if luoghi[a][giorno] != luoghi[0][giorno]:
            tutti_qui = False
    if tutti_qui:
        print("Nello stesso luogo: giorno", GIORNI[giorno])