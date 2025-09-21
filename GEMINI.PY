def check(lista):
    listajókhoz = []
    for szám in lista:
        if szám > 0:
            listajókhoz.append(szám)
    for jo_szam in listajókhoz: # Így nem lesz a végén ", "
        print(jo_szam, end=", ")
    print() # Új sor a végére
            




gyümölcsök = ["alma", "körte","alma", "körte", "banán"]
számok = [1,-3,4,6,-84,21,43,-92]



for elem in gyümölcsök:
    print()
    print(elem,end=", ")





print(f"Az összes szám: {számok}")
print("Nullánál nagyobb számok:",end=", ")
check(számok)