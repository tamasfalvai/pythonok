def checkthewords(w, lista):
    avan = "a" in w.lower()
    evan = "e" in w.lower()
    páros = len(w) % 2 == 0

    if evan or avan and páros:
        lista.append(w)

value = "rf4"  # Inicializáljuk a value-t egy üres stringre, hogy belépjünk a ciklusba
print()
print("Adjon meg szavakat (STOP) vagy (ENTER) leütéséig!. ")
stop = "stop"
enter = ""
count = 0
lista1 = []

while value.lower() != stop and value != enter:
    count += 1
    value = input(f"{count}.Szó: ")
    if value.lower() != stop and value != enter:  # Csak akkor dolgozzuk fel, ha nem a kilépési feltétel
        checkthewords(value, lista1)

print("Ön kilépett a programból.")





if len(lista1) == 0:
    print("Nem kaptamA vagy E betűt tartalmazó szavak ")
else:
    print("Páros karakterszámú, A vagy E betűt tartalmazó szavak:")
print(lista1)