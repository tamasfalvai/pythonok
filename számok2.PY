def is_páros(value):
    """Eldönti, hogy egy szám páros-e."""
    return value % 2 == 0  # True, ha páros, False, ha páratlan


lista = []  
szam = int(input("Adj meg egy számot: "))  

while not is_páros(szam):  # Amíg páratlan számot adsz meg
    szam = int(input("Adj meg egy számot ÚJRA: "))  
    if is_páros(szam):  # Ha páros, elmentjük
        lista.append(szam)   

print("Páros számot adtál meg, a PROGRAM véget ér.")
print(lista)