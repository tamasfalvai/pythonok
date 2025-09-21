def is_palindromic(n: int) -> bool:
    for i in range(len(n)//2): # végig megy a szó hosznak a felén 
        if (n[i] != n[-(i+1)]): 
            return False
    return True    

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


print("\nA palindrom számok fele: ", end=" ")
for i in numbers:
    print(int(i)/2, end="  ")