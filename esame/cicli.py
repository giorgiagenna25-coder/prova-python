"""
#per stampare i numeri da 0 a 3
print(0)
print(1)
print(2)
print(3)

# ma se volessimo stampare i numeri da 0 a N, non conoscendo N non possiamo usare le funzioni di prima,
# non sappaimo il numero di righe che dobbiamo scrivere e fino a che numero dobbiamo arrivare,
# usiamo i CICLI, la funzione WHILE

n = 0
while n<=3:
    print(n)
    n+=1
"""


#ESERCIZIO TASSO FISSO
# vogliamo calcolare il bilancio del conto, che parte da un valore saldo_inziale, considerato un tasso
# fisso di interesse composto annuo del r% e fermarci all'anno in cui il totale supera 20000€ e
# restituire in output l'anno di stop, il saldo finale e la differenza tra saldo finale e iniziale

saldo_iniziale = 1000
saldo = saldo_iniziale
TASSO = 5
anno = 0         #anno = 1

while anno < 10:        #saldo <= 20000:
    saldo += saldo * TASSO/100       #scrivere ...+= vuol dire ... = ... +
    anno += 1

differenza = saldo - saldo_iniziale

print(saldo)
print("Anno: " + str(anno) + "\nSaldo: " + str(saldo) + "\nDifferenza: " + str(differenza))