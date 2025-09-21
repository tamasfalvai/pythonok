def checkmywords(w):    # "E" ÉS "É" vizsgálunk a szóban!
    w = w.lower()  
    evan = 'e' in w
    évan = 'é' in w

    if evan and évan:
        print(f"Hossz: {len(w)}, Tartalmaz E-t és É-t: Igen")
        return True
    elif evan:
        print(f"Hossz: {len(w)}, Tartalmaz E-t: Igen")
        return True
    elif évan:
        print(f"Hossz: {len(w)}, Tartalmaz É-t: Igen")
        return True
    else:
        print(f"Hossz: {len(w)}, Tartalmaz E-t vagy É-t: Nem")
        return False

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def statisztika(szavak):
    átlag = 0        
    for szó in szavak:     #Végig megyünk a listán.
        átlag += len(szó)  # 0 + szavak hossza 
    átlag /= len(szavak)   #elsztjuk a kapott összeget a listában szereplő szavak számával.

    print(f"- Átlagos hossz: {átlag:.2f}")   #átlag nevű változóban tárolt lebegőpontos számot két tizedesjegy pontossággal kell megjeleníteni
    leghosszabb = szavak[0]
    for szó in szavak:
        if len(szó) > len(leghosszabb):
            leghosszabb = szó
    print(f"- Leghosszabb szó: {leghosszabb}, (hossza: {len(leghosszabb)})")


    prim_hosszusagu_szavak = [szó for szó in szavak if is_prime(len(szó))]
    print(f"- Prím hosszúságú szavak: {', '.join(prim_hosszusagu_szavak)}")


print("Adjon meg egy pár szót és kap róla pár statisztikát!")
darab = int(input("\nHány darab szót szeretnél majd megadni:? "))
listforwords = []
value = "    "
számlálás = 0


while  számlálás < darab:  #while ciklus, ami addig fut, amíg a számlálás kisebb, mint a felhasználó által megadott darab.
    számlálás += 1
    value = input(f"{számlálás}. szó: ")
    listforwords.append(value)
    checkmywords(value)
    if value == "":
        print("Bizonyára üres ENTER-T nyomot ajánlom nem ütni legközelebb!")
        #Azért ide mert ha nem ENTER-T NYOMHANEM HELYESN VÉGIG MEGY AKKOR IS KIIRJA 



print("\nStatisztika: ")
statisztika(listforwords)