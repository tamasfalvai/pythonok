def isvalidword(w):  # függvény
    if len(w) == 3 or len(w) == 5:
    # ha a w hossza 3 vagy 5 akkor TRUE val tér visssza    
        return True


print()  # üres sor
print("A program a megfelelő számokat rakja el majd a program végén kidob.")
print("Kilépés ENTERREL")
wordok = []  # 3 vagy 5 karakter hoszzúak listálya
value = "   "   # while elindításához
számozás = 0 # a számozáshoz
quit = "quit"  # kilépés

while value != "" and value.lower() != quit:
    számozás += 1
    value = input(f"{számozás}. SzÓ: ")
    if isvalidword(value):
        wordok.append(value)

if len(wordok) > 0:
    print(", ".join(wordok))
else:
    print("Ön nem adott meg megfelelő számot.")
