# ESERCIZIO 4
lista_a = [1, 4, 9, 16]
lista_b = [4, 7, 9, 9, 11]
lista_c = []

i = 0
j = 0
while i < len(lista_a) and j < len(lista_b):
    if lista_a[i] < lista_b[j]:
         lista_c.append(lista_a[i])
         i += 1
    else:
         lista_c.append(lista_b[j])
         j += 1
while i < len(lista_a):
     lista_c.append(lista_a[i])
     i += 1
while j < len(lista_b):
     lista_c.append(lista_b[j])
     j += 1

print(lista_c)