import random 

def createmyrandomnumber():
    return random.randint(0,100)  # return hozzáadva

def főprogram(randomszám, value):
    if value > randomszám:
        print("A szám amit megadott az nagyobb mint a randomszám:")
    elif randomszám > value:
        print("A szám amit megadott az kisebb mint a random szám:")
    else:
        print(f"Gratulálok kitaláltad a számot amely nem más mint {randomszám}")

value = 0
szám = createmyrandomnumber()  # zárójelek hozzáadva és egyszer hívjuk meg
számlálás = 0

while value != szám:
    számlálás += 1
    value = int(input("Szám: "))
    főprogram(szám, value)  # value paraméter hozzáadva