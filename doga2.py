def is_divisible_by_3_9(n: int) -> bool:
                    # n egy int vagyis egy szám és boolal tér vissza mely egy True vagy False
    return n % 3 == 0 and n % 9 == 0


numbers = []
value = 1
count = 0
print("Adjon meg számokta 1 és 100 között. A program 3-al és 9el osztható számokta gyűjti.")

while value >= 1 and value <= 100:
    count += 1
    value = int(input(f"{count}. szám: "))
    if value >= 1 and value <= 100 and is_divisible_by_3_9(value):
        numbers.append(str(value))

if (len(numbers) == 0):
    print("Ön nem adott meg 3al és 9el osztható számokta.")
else:
    print("A megadott számokból melyek 3-al és 9el oszthatóak")
    print(", ".join(numbers))
print()