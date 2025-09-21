# A két függvény ugyanazt csinálja! Tudni kell így is, úgy is!
def is_valid_number(value: str) -> bool:
    return value.isdecimal()

def is_valid_number2(value: str) -> bool:
    numbers = "0123456789"
    i = 0
    # Ha nem ért még a value-sztring végére, akkor minden karakterről eldönti, hogy benne van-e a numbers sztringben.
    while len(value) > i and value[i] in numbers:
        i += 1
    # Ha minden karakter benne volt a numbers-ben (mert számok voltak), akkor végig ért a value-sztringen, és így az i-ciklusváltozó értéke nagyobb lett, mint a value-sztring hossza.
    return i > len(value)

input_value = " "
count = 0
# Mivel szeretnénk jól számolni, ezért az összeg kezdő értéke 0 kell, hogy legyen! 0+10+20 = 30
summa = 0 # Itt képződik az összeg.

while input_value != "": # Enter-ig kérjük be a számokat.
    count += 1
    input_value = input(f"{count}. szám: ")
    if input_value != "" and is_valid_number(input_value):
        summa += int(input_value) # Itt az összeg értékéhez hozzáadom a soron következő számot. Itt összegzünk.

print(f"A megadott számok összege: {summa}")