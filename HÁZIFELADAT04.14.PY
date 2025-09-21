def is_all_even(number, listaarosszhoz):
    for szam in number:           # VÉGIG MEGY MINDEN SZÁMJEGYEN 
        if int(szam) % 2 != 0:
            listaarosszhoz.append(szam)    #páratlanokat szelektáljuk
    return len(listaarosszhoz) == 0


def geet_digit_sum(number):
    summa = 0    
    for szam in number:  
        summa += int(szam)   #mindig hozzáadja az aktuális számjegyet az összeghez
    return summa  


print("Adjon meg számokat! (kilépés ENTER-rel.):  ")
print()
value = 0
számláló = 0
listaaroszhoz = []


while value != "":
    számláló += 1
    value = input(f"{számláló}.Szám: ")    # AZÉRT STR ME IGY NEM KELL A FÜGGVÉNYBE EGYBŐL ÁTALAKÍTANI STR-É
    listaaroszhoz.clear()                  #a lista mindig tiszta legyen az új szám előtt.
    minden_páros = is_all_even(value, listaaroszhoz)
    if minden_páros:
        összeg = geet_digit_sum(value)
        print(f"Minden számjegye páros és az összege: {összeg}")
    else:
        print(f"Ezek számjegyek páratlanok: {listaaroszhoz}")
print("Ön kilépett a programból.")
