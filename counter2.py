def mygroktask(value):
    elsőn = value.split()[0].lower()
    masodkn = value.split()[-1].lower()

    elsőn2 = elsőn[0:1:-1]
    #előről kezdjük a szót a 1 index lesz a stop ami a 3. karakteer és -1 es steppel megyünk hátra 
    masodkn2 = masodkn[0:-1:2].upper()

    summa = 0
    for c in f"{elsőn}{masodkn}":
        summa += ord(c)
    #Nem mondtad h a szót szóközzel vagy nélküle legyen íy nélküle lesz 


value = "vnefwoivnf"

while  " "  in value and value.lower() != "q":
    value = input("Kérek a nevet:")
    if value.isalpha() and value != "q":
        mygroktask(value)
print("Nem jó nevet adtál meg állítsá magadon és rendes neved add meg.")
    




print("Üdvözlöm A Programunjban Ez A Program A neve Alapján Készít Magának Egy Erős Védelmi Jelszót")