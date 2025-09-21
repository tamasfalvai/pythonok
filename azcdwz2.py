def azonosító(value):
    spec_chars = "!@#$%^&*()_+-=[]{}|;':\",.<>?/"
    value = value.lower()

    while not " " in value:
        if value.lower() == "q":
            print("Kilépés...")
            return  # Kilép a függvényből
        print("Hibás név! Írd be a Vezetékneved és a Kereszneved is!!")
        value = input("Kérem a teljes nevet Vezetéknév és Keresztnévvel, kilépés:q-val: ")

    szokoz = value.index(" ")
    vezeteknev = value[:szokoz]
    keresztnev = value[szokoz + 1:]

    # 1. Vezetéknév a 3. karaktertől végéig, visszafele
    vezeteknev_mod = vezeteknev[3:][::-1]

    # 2. Keresztnév minden 3. karaktere
    keresztnev_mod = keresztnev[::3]

    # 3. Név ASCII összege
    nev = vezeteknev + keresztnev
    osszeg = sum(ord(k) for k in nev)

    # 4. Speciális karakter kiválasztása
    index = osszeg % len(spec_chars)
    spec = spec_chars[index]

    # 5. Minden 3. karakter nagybetűssé alakítása
    uj_vezetek = ""
    for i, ch in enumerate(vezeteknev_mod):
        uj_vezetek += ch.upper() if i % 3 == 0 else ch

    uj_kereszt = ""
    for i, ch in enumerate(keresztnev_mod):
        uj_kereszt += ch.upper() if i % 3 == 0 else ch

    # 6. Összefűzés
    eredmeny = vezeteknev_mod + uj_vezetek + spec + uj_kereszt + str(osszeg)
    print("Azonosító:", eredmeny)


value = ""

while True:
    print()
    value = input("Kérem a teljes nevet (kilépéshez írj: q): ")
    if value.lower() == "q":
        print("Kilépés a programból.")
        break
    azonosító(value)
