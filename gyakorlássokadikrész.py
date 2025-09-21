import random

def randomok():
    lista = []
    for i in range(20):
        randomszámok = random.randint(1, 12)
        lista.append(randomszámok)

    print(lista, end=", ")  # Az első lista kiírása

    lista2 = []
    for randomszámok in lista:
        if randomszámok % 3 == 0:
            lista2.append(randomszámok)  # ✅ Itt most már Hozzáadjuk a számot

    return lista2  # Visszatérünk a 3-mal osztható számok listájával

print(randomok())  # A függvény visszatérési értékét is kiírjuk
