def is_valid_word(szo):
    # Visszatér True-val, ha a szó hossza 3 vagy 5 betű.
    if len(szo) == 3 or len(szo) == 5:
        return True


szavak = []  # Ebben a listában tároljuk az érvényes szavakat.
print()
print("A program a három és az ötbetűs szavakat gyűjti. Kilépés üres bevitellel vagy 'quit'-tal.")

# Első szó bekérése, hogy a while ciklusban a feltétel már ellenőrizhető legyen.
count = 1
value = input(f"{count}. szó: ")

while value != "" and value.lower() != "quit":
    if is_valid_word(value):
        szavak.append(value)
    count += 1
    value = input(f"{count}. szó: ")

if len(szavak) == 0:
    print("Ön nem adott meg 3 vagy 5 betűs szavakat.")
else:
    ",".join(szavak)
    print("A 3 és 5 betűs szavak:", szavak)