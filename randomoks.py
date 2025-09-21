def is_palindromic(n) :
    for i in range(len(n)//2): # 0, 1es osztás 
        if (n[i] != n[-(i+1)]):
# ha a szó indexe nem egyenlő a szám minusz indexével és +1-el
            return False
    return True    

print()
print("Adjon meg palindrom számokat! Kilépés Enter-rel.")
numbers = []

value = "    "
while value != "":
    value = input("A megadott szám: ")
    if value != "":
        if is_palindromic(value):
            numbers.append(value)
            
print("Ön kilépett a programból.")
print(f"\nPalindrom számok a következő számok: {', '.join(numbers)}")


if is_palindromic(value) in numbers:
    print("\nA palindrom számok fele: ", end=" ")
for i in numbers:
    print(int(i)/2, end="  ")