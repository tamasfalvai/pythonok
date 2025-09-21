def is_valid_number(number: str) -> bool:
    number_chars = "0123456789"                           #SZÁMOK 0-9
    i = 0                                                 #I VÁLTOZÓ A SZÁMLÁLÁSHOZ
    while i < len(number) and number[i] in number_chars:  
        i += 1

    return i == len(number) and number != ""

# n = input("Szám: ")
# print(is_valid_number(n))
SZÁMLÁÁS = 0
n = ""

while not is_valid_number(n):
    SZÁMLÁÁS +=1
    n = input(f"{SZÁMLÁÁS}.szám:  ")


print("Csak tudsz normális számot adni:! ")
print(int(n))