summa = 0
lista11 = []
páros = []
páratlan = []

for i in range(10):
    summa +=1
    lista11.append(summa)
    print(summa,end=", ")


if summa % 2 == 0:
    páros.append(summa)
    ", ".join(páros)
else:
    páratlan.append(summa)
    ",".join(páratlan)



print(f"A práos számok a listából {páros}")
print(f"Páratlan számok a listából: {páratlan}")