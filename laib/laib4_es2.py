# Data una situa di parcheggi trova e stampa l'elnco di tutte le file di posti liberi

# park = ["_" , "_" , "X" , "_" , "_" , "X" , "_" , "_" , "_" , "_" , ]

# pos = 0, lun = 2
# pos = 3, lun = 2
# pos = 6, lun = 4

# se park[i] = "_" il posto è libero:
#   lun = 1
#   se park[i+1] = "_":
#       lun = 2
#       se park[i+2] = "_":
#           lun = 3
#           ...

park = "_" *10

while "_" in park: #finchè ci sono posti liberi
    i = 0
    lun_max = 0
    for i in range(len(park)):
        lun = 0
        while i + lun < len(park) and park[i + lun] == "_":
            lun += 1
        #print("Dal posto: ",i, "c'è una fila di parcheggi liberi lunga: ",lun)
        # ma questa fila di parcheggi libera è la più lunga?
        if lun > lun_max: #è la più lunga tra quelle viste fino ad adesso
            lun_max = lun
            pos_max = i

    print("La lunghezza massima delle file di parcheggi liberi è ",lun_max)
    print("La sequenza di parcheggi liberi più lunga si trova in posizione ",i)
    print("Sequenza max in ",i,"lunga ", lun_max)

    nuova_pos = int(pos_max + lun_max // 2)
    print("Parcheggia in posizione: ", nuova_pos)
    park[nuova_pos] = "X"
    print(park)