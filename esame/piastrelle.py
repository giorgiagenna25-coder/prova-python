# ESERCIZIO "PIASTRELLE"

# In Python è possibile delimitare un stringa in 4 modi diversi: con i singoli apici - "...";'...' -,
# oppure con delle terne di apici - """...""" ; '''...''' -. L'unica differenza tra questi due modi di
# scrivere le stringhe sta nel fatto che se uso le terne di stringhe la mia stringa può svilupparsi su
# più righe e si chiuderà solo quando si chiuderà la terna di stringhe, mantre con quelli singoli la
# stringa si chiude quando si va a capo (solo una riga)

"""
Ipotesi aggiuntive
    Le piastrelle sono quadrate
    Piastrelle bianche e nere hanno la stessa dimensione
    In senso verticale c'è abbastanza spazio

Valori in INPUT:
    Lunghezza totale del muro (lun_muro)
    Lunghezza delle piastrelle (lun_piast)

Valori in OUTPUT:
    Numero di piastrelle bianche e numero di piastrelle nere (bianche, nere)
    Margine laterale tra le piastrelle alle estremità e il muro (margine)

Vincoli:
    Prima e ultima piastrella nere
    Piastrelle di colore alternato 
    Margine uguale alle due estremità (può essere anche 0.0 cm)
"""

"""
ESEMPIO

Muro: 100 cm
Piastrella: 33 cm
2 nere, 1 bianca, margine 0.5 cm

Muro: 100 cm
Piastrella: 25 cm
2 nere, 1 bianca, margine 12.5 cm

Muro: 100 cm
Piastrella: 20 cm
3 nere, 2 bianche, margine 0.0 cm

Muro: 100 cm
Piastrella: 80 cm
1 nera, 0 bianche, margine 10.0 cm

Muro: 50 cm
Piastrella: 80 cm
Impossibile
"""

"""
ALGORITMO

quante = int(lun_muro / lun_piast)

if quante è dispari:
    quante è giusto
else:
    quante è sbagliato --> quante viene decrementato di 1

NOTA: di sicuro 'quante' è dispari    

bianche = int(quante/2)
nere = bianche + 1
margine =(lun_muro -(lun_pias * quante))/2
"""

print("Problema delle piastrelle")

lun_muro = float(input("Lunghezza del muro (cm): "))
lun_piast = float(input("Lunghezza delle piastrelle (cm): "))

if lun_muro <= 0 :
    print("Il muro deve avere lunghezza positiva")
elif lun_piast <= 0:
    print("La piastrella deve avere lunghezza positiva")
elif lun_piast>lun_muro:
    print("La piastrella non può essere più lunga del muro")
else:
    quante = int(lun_muro/lun_piast)
    # print(quante)

    if quante % 2 == 0 : # è pari, con % il programma fa divide e prende in considerazione solo il resto
        quante = quante - 1

    # print (quante)

    bianche = int(quante/2)
    nere = bianche + 1

    margine = (lun_muro - (lun_piast * quante))/2

    print("Numero di piastrelle bianche: ", bianche)
   
    print("Numero di piastrelle nere: ", nere)
   
    print("Margine da lasciare su ogni lato: ", margine)