def checkmywords(w):
    if 'e' in w.lower():
        print(f"Hossz: {len(w)}, Tartalmaz E-t: Igen")
    else:
        print(f"Hossz: {len(w)}, Tartalmaz E-t: Nem")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def statisztika(szavak):
    átlag = 0
    for szó in szavak:
        átlag += len(szó)
    átlag /= len(szavak)  
    print(f"- Átlagos hossz: {átlag}")

    leghosszabb = szavak[0]
    for szó in szavak:
        if len(szó) > len(leghosszabb):
            leghosszabb = szó
    print(f"\n- Leghosszabb szó: {leghosszabb}, hossza: {len(leghosszabb)}")
    
    print(f"\n- E-t tartalmazó szavak: {checkmywords(szavak)}")

    print(f"\n- Prím hosszúságú szavak: {is_prime(szavak)}")



listforwords = []
számlálás = 0

for i in range(5):
    számlálás += 1
    value = input(f"{számlálás}. szó: ")
    listforwords.append(value)
    checkmywords(value)

print("\nStatisztika: ")
statisztika(listforwords)