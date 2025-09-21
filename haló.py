def my_checket(value):
    if len(value) == 3 or len(value) == 5:
        return True
    return False  # Ha nem 3 vagy 5 karakteres, akkor False-t ad vissza

löszegekre = []
hanyadik = 0

value = input("uzvizvg")  # Az első bekérés
quit = "quit"

print()
print("A program 3 és 5 karakter hosszú szavakat gyűjti! Kilépés ENTERREL VAGY QUITTAL.")

while value != "" and value.lower() != quit:
    hanyadik += 1
    if my_checket(value):  # Ellenőrizzük a szót
        löszegekre.append(value)
    else:
        print("Ön nem adott meg nekem 3 vagy 5 karakter hosszú szót.")

    value = input(f"{hanyadik}. Szó: ")  # Új szó bekérése

print(f"A 3 vagy 5 karakter hosszú szavak: {löszegekre}")
