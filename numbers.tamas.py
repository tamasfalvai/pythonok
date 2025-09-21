def is_divisible_by_3_9(n: int) -> bool:
    return n % 3 == 0 and n % 9 == 0

numbers = []
value = 1
count = 0


while value >= 1 and value <= 100:
    count += 1
    value = int(input(f"{count}. szám: "))
    if value >= 1 and value <= 100 and is_divisible_by_3_9(value):
        numbers.append(str(value))

if (len(numbers) == 0):
    print("Nem kaptam jó számokat.")
else:
    print(", ".join(numbers))