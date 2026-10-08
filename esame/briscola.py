# Acqusisci i dati
seme = input("Inserisci il seme di briscola: ")

carta1 = input("Inserisci la prima carta: ")
carta2 = input("inserisci la seconda carta: ")
VALORI = "24567JQK3A"
SEMI = "CQFP"

# carta1 e carta2 sono due stringhe di due caratteri, 

# Verifica la correttezza dei dati
"""

len(seme) == 1
seme in SEMI /// seme == "C" or seme == "Q" or seme == "F" or seme == "P"

len(carta1) == 2
valore1 in VALORI
seme1 in SEMI

len(carta2) == 2
valore2 in VALORI
seme2 in SEMI

carta1 != carta2
"""

# Determina il vincitore
seme1 = carta1[1]
seme2 = carta2[1]
valore1 = carta1[0]
valore2 = carta2[0]

# valore = 2 4 5 6 7 J Q K 3 A
# ordine = 1 2 3 4 5 6 7 8 9 10

ordine1 = VALORI.index(valore1) + 1
ordine2 = VALORI.index(valore2) + 1

print("ordine", ordine1, ordine2)

"""
if carta1 ha seme di briscola, ma carta2 non ha seme di briscola:
    vince carta1
if carta2 ha seme di briscola, ma carta carta1 non ha seme di briscola:
    vince carta2
"""
if seme1 == seme and seme2 != seme:
    print("Vince", carta1)
elif seme2 == seme and seme1 != seme:
        print("Vince", carta2)
elif seme1 != seme2:
            print("Vince", carta1)
elif ordine1 > ordine2:
                print("Vince", carta1)
else:
                print("Vince", carta2)

# l'equivalente é: if carta1[1] == seme and not(carta2[1] == seme):

# Stampa il risultato