def isadfjkdfldf(n):
    return n % 9 == 0
    #visszatér ha aaz n osztható 9el ha 9el akk 3al is osztható


count = 0
value = 1 
lista = []
print("Adjon meg számokta 1 és 100 között. A program 3-al és 9el osztható számokta gyűjti.")

while value <= 100 and value >= 1:
    count += 1
    value = int(input(f"{count}.Szám: "))
    if isadfjkdfldf(value) and value <= 100 and value >= 1:
        lista.append(value)

    

if len(lista) == 0:
    print("nem adtál meg mefelelő számot")
else:
    print("A 3-al és 9 el sopztható számok")
    print(lista)
    print()