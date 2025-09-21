def szamol_dij(tavolsag):      # először megnézzük hogy hova tartozik ha ezmegvan akkor egy valtozoba rakjuk aza adott értéket és bezsorozzuk a tavolsaggal a válzozót
    if 1 <= tavolsag <= 5:
        dij = 500
    elif 6 <= tavolsag <= 10:
        dij = 1000
    elif 11 <= tavolsag <= 15:
        dij = 1500
    elif 16 <= tavolsag <= 20:
        dij = 2000
    else:
        return "Nem megfelelő távolság! (1-20 km között legyen)"

    return f"A fizetség: {tavolsag * dij} Ft"


tav = int(input("Add meg a megtett utat kilométerben (1-20 km között, egész szám): "))
eredmeny = szamol_dij(tav)
print(eredmeny)
