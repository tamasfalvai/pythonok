def check_my_number(n):
    if int(str(n)[1]) + int(str(n)[2]) == 10 and len(str(n)) == 3 and n % 2 == 1:
        return True

print()
print("A program bekér számokat, ha a feltételeknek megfelel, akkor azt a végén kiírja, és addig kér be, amíg nem lesz 5 darab ilyen szám.")
listforgodnumb = []
számlálás = 0

while len(listforgodnumb) != 5:
    számlálás += 1
    value = int(input(f"{számlálás}. Szám: "))
    if check_my_number(value):
        listforgodnumb.append(str(value))  # Stringként tároljuk az értéket

# Az összes szám kiírása, ha 5 megfelelőt kaptunk
print()
print("Az 5 érvényes :")
print(", ".join(listforgodnumb))  # Mivel már stringek, így működik a join