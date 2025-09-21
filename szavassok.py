def is_correct_word(value):
    if len(value) % 2 == 0 and ("a" in value.lower() or "e" in value.lower()):
        return True

stop = "stop"
számlálás = 0
lisat = []
print()
print("Adjon meg szavakat! Kilépés ENTERREL vagy STOPPAL.")
value = "bvfhiwu i"


while value != "" and value.lower() != stop:
    számlálás += 1
    value = input(f"{számlálás}. Szó: ")


if is_correct_word(value):  
    lisat.append(value)
    print(f"A megfelelő szavak, melyek páros számú karakterből állnak és tartalmaznak 'e' vagy 'a' betűt:")
    ", ".join(lisat)
    print(lisat)
else:
    print("Ön nem adott meg olyan szót, amely páros karakter számú és tartalmaz 'e' vagy 'a' betűt.")