def dij_zsamolas(tavoloság):

    if 1<= tavoloság <= 5:
        dij = 500
    elif 6 <= tavoloság <= 10:
        dij = 1000
    elif 11 <= tavoloság <= 15:
        dij = 1500
    elif 16 <= tavoloság <= 20:
        dij = 2000
    else:
        print("Nem jó számot adtál meg:")


    return f"A fizetséged {dij* tavoloság}Ft "




print("A program kiszámolja, hogy mennyi a fizetése kilométerek alapján.")
print("")
tav = int(input("Hány kilométert tettél meg?: "))
eredmény = dij_zsamolas(tav)
print(eredmény)




# először megnézzük melyik régióba tartozik mert minél nagyobb a kilométerben megtett út annl nagyobb lesz a fizetndő forint / km ezért nem fix árban szorozzuk meh