# le tabelle non sono altro che liste di liste

# creiamo un tabella che contenga il medagliere dei vari stati nel pattinaggio artistico
lista_medaglie = ["Oro" , "Argento" , "Bronzo"]

tabella_medaglie_italia = [0, 3, 0]
tabella_medaglie_canada = [3, 0, 1]

tabella_medaglie = [
    [ 0, 3, 0 ],
    [ 0, 0, 1 ],
    [ 0, 0, 1 ],
    [ 1, 0, 0 ],
    [ 0, 0, 1 ],
    [ 3, 1, 1 ],
    [ 0, 1, 0 ],
    [ 1, 0, 1 ]
    ]

print(lista_medaglie[0] [0])

print(tabella_medaglie[0] [0])

#creazione incrementale tabelle
NUMERO_RIGHE = 5
NUMERO_COLONNE = 5
tabella_zeri = []

for riga in range(NUMERO_RIGHE):
    tabella_zeri.append([0]*NUMERO_COLONNE)

print(tabella_zeri)

tabella_zeri[2] [2] = 1

for riga in tabella_medaglie:
    print(riga)

#somma per riga
rowtotal = 0
i = 2  #tieni ferma la riga
for j in range(len(tabella_medaglie[0])):
    rowtotal += tabella_medaglie[2][j]

# somma per colonna
coltotal = 0
j = 1
for i in range(len(tabella_medaglie)):
    coltotal += tabella_medaglie[i][1]

print("rowtotal: " , rowtotal)
print("coltotal: " , coltotal)


lista_paesi = ["Canada" , "Italia" , "Marocco" , "Serbia" , "USA"]
print("Prima del sorting")
print(lista_paesi)

print("Dopo il sorting")
lista_ordinata = lista_paesi.sort()