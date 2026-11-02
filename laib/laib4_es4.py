# ESERCIZIO 4
lista_a = [1, 4, 9, 16]
lista_b = [4, 7, 9, 9, 11]

lista_c = []
for i in lista_a:
    for j in lista_b:
        if i < j:
            lista_c.append(i)
            break   
        else:
            lista_c.append(j)
#DA REVISIONARE - lavorare sugli indici

print(lista_c)