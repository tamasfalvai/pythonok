def calculate(value): 
    value = value.replace(" ","")
    if "+" in value:
        elsőérték = value.split("+")[0]
        másodikérték = value.split("+")[-1]
        eredmény = int(elsőérték) + int(másodikérték)
        return eredmény

    if "-" in value:
        elsőérték = value.split("-")[0]
        másodikérték = value.split("-")[-1]
        eredmény = int(elsőérték) - int(másodikérték)
        return eredmény

    if "*" in value:
        elsőérték = value.split("*")[0]
        másodikérték = value.split("*")[-1]
        eredmény = int(elsőérték) * int(másodikérték)
        return eredmény

print("A program kiszámolja a megadott számítási feladatot.Kilépés 'q-val. Pl: 3+4, 3+ 4, 3 +4, 3 + 4")
value = "3 + 4"
while value.lower() != "q":
    value = input("Kérem a kiszámítandó feladaot: ")
    if value != "q":
        print(calculate(value))
print("Ön kilépett a programból.")