# ESERIZIO
"""
Sono date due liste di stringhe: la prima contiene i nomi di persone, mentre la seconda contiene, in
posizione corrispondente, il cognome delle stesse persone.

Si calcoli e si stampi una terza lista di stringhe, che contenga il nome completo delle persone,
rappresentando il nome ed il cognome separati da uno spazio.

Esempio:

Lista dei nomi: ['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']

Lista dei cognomi: ['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']

Risultato:
['Peter Parker', 'Clark Kent', 'Bruce Wayne', 'Tony Stark', 'Steve Rogers', 'Diana Prince', 'Barry Allen', 'Arthur Curry']

"""

nomi = ['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']
cognomi = ['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']

nuova = []
for i in range(len(nomi)):
    completo = nomi[i] + " " + cognomi[i]
    nuova.append(completo)
print(nuova)
print()


# ESERCIZIO
"""
È data una lista di nomi di persone, ciascuno rappresentato da una stringa con nome e cognome separati
da uno spazio.
Si assuma che non vi siano nomi doppi o cognomi doppi.

Costruire e stampare due liste di stringhe, in cui la prima contenga i nomi propri delle persone, e la 
seconda contenga i cognomi delle stesse persone, in ordine corrispondente

Esempio:

Lista di nomi iniziale:
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

Risultato:
Lista nomi: ['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']
Lista cognomi: ['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']
"""

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
for sup in supereroi: #sup = al nome completo del supereroe
    pos_spazio = sup.find(" ") #così trovi l'indice dello spazio, quindi da dove finisce il nome e
                               #inizia il cognome
    nomi.append(sup[ : pos_spazio])
    cognomi.append(sup[pos_spazio + 1 : ])
print("Nomi: ", nomi)
print("Cognomi: ", cognomi)

# un altro modo per fare questo es è farlo con split
nomi = []
cognomi = []
for sup in supereroi:
    separati = sup.split() #separati = ["Peter" , "Parker"]
    nomi.append(separati[0])
    cognomi.append(separati[1])

print("Nomi: ", nomi)
print("Cognomi: ", cognomi)
print()


# ESERCIZIO
"""
Sia data una tabella contenente 7 colonne (corrispondenti ai giorni della settimana) e un numero
variabile di righe (corrispondenti a diversi amici). In ciascuna casella, compare una stringa che
rappresenta il luogo in cui si trova ciascuno degli amici in quella giornata.

Determinare in quali giorni della settimana tutti gli amici sono nello stesso luogo.
"""

luoghi = [
    ['Torino', 'Torino', 'Aosta', 'Aosta', 'Milano', 'Milano', 'Torino'],
    ['Milano', 'Torino', 'Milano', 'Aosta', 'Torino', 'Torino', 'Torino'],
    ['Milano', 'Torino', 'Aosta', 'Aosta', 'Genova', 'Genova', 'Torino'],
]

"""
Risultato atteso:
Nello stesso luogo: giorno 1
Nello stesso luogo: giorno 3
Nello stesso luogo: giorno 6
"""

for giorno in range(len(luoghi[0])): #len(luoghi[0]) = al numero di elementi nella prima riga della 
                                     #tabella (7 giorni)
    #if giorno sono tutti nello stesso giorno
    #if luoghi[0][giorno* == luoghi[1][giorno] and luoghi[2][giorno] == luoghi[0][giorno] ...:
    #if tutti gli amici a >= 1 hanno la proprietà che luoghi[a][giorno] == luoghi[0][giorno]:
    tutti_qui = True
    for amico in range(1, len(luoghi)): #analizza tutti gli amici (tutte le colonne) escluso il primo
        if luoghi[amico][giorno] != luoghi[0][giorno]:
            tutti_qui = False
    if tutti_qui:
        print("Nello stesso luogo: giorno ", giorno) #così parte a contare da 0