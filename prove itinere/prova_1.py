# ESERCIZIO 2
# inserisci una parola e se trovi doppie metti la maiuscola: anna --> aNa

parola = input("Inserire una parola: ")
new = ""
for lettera in parola:
    if lettera+lettera in parola:
        doppia = lettera+lettera
        doppia = str(lettera.upper())
        new = new + doppia
    else:
        new += lettera
    nuova_parola = new
    
    
print(nuova_parola)