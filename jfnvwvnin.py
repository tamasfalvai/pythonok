def eldonto(value):
    return int(value[0]) + int(value[-1] < 10)


szamok = []

value = " "
while value != "":
    value = input("A meg adott szam: ")
    if eldonto(value):
        szamok.append(value)

if len(szamok) > 0:
    print(szamok)
else:
    print("nem volt jó szám")
