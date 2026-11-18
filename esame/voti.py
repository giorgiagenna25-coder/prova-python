NOMEFILE = "voti.csv"

import csv

f = open(NOMEFILE, "r", encoding = "utf-8")

reader = csv.reader(f)

voti = []

for campi in reader:
    campi[1] = int(campi[1])
    campi[2] = int(campi[2])
    voti.append(campi)
    
print(voti)

"""
for riga in f:
    campi = riga.rstrip().split(",")
    campi[1] = int(campi[1])
    campi[2] = int(campi[2])
    voti.append(campi)

print(voti)
"""