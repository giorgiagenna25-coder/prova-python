"""
#ESERCIZIO 1
num = input("Inserisci un numero a cinque cifre: ")
#num = str(num_int)
#print(num)
if len(num) != 5:
    print("il numero non è di 5 cifre")
else:
    print(num[0])
    print(num[1])
    print(num[2])
    print(num[3])
    print(num[4])
"""

"""
#ESERCIZIO 2
num_tel = input("Inserire numero di telfono: ")
if len(num_tel) == 10:
    pt_1 = num_tel[ : 3]
    pt_2 = num_tel[3 : 6]
    pt_3 = num_tel[6 : 10]
    print("(",pt_1,")",pt_2,"-",pt_3)
else:
    print("Il numero non è valido")
"""

"""
#ESERCIZIO 3
num_int = input("Inserire un numero intero: ")
x = int(num_int)
print("x > 0 and x < 100", x > 0 and x < 100)
print("x > 0 or x < 100", x > 0 or x < 100)
print("x > 0 or 100 < x", x > 0 or 100 < x)
print("x > 0 and x < 100 or x == -1", x > 0 and x < 100 or x == -1)
"""


#ESERCIZIO 4
giorno = input("Inserire giorno: ")
giorno = int(giorno)
# Verificare il giorno

mese = int(input("Inserire il numero del mese: "))
# Verificare il mese
if mese % 3 == 0 and giorno >= 21:
    if mese == 3:
        stagione = "Spring"
    elif mese == 6:
        stagione = "Summer"
    elif mese == 9:
        stagione = "Fall"
    elif mese == 12:
        stagione = "Winter" 
elif mese == 1 or mese == 2 or mese == 3:
    stagione = "Winter"
elif mese == 4 or mese == 5 or mese == 6:
    stagione = "Spring"
elif mese == 7 or mese == 8 or mese == 9:
    stagione = "Summer"
elif mese == 10 or mese == 11 or mese == 12:
    stagione = "Fall"


print("La stagione è:", stagione)