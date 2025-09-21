def is_correct_number(value: str) -> bool:
    return int(value[0]) + int(value[-1]) == 9 or int(value[0]) + int(value[-1]) == 18


input_value = 1
count = 0
numbers = []

while int(input_value) >= 0 and int(input_value) <= 100:
    count += 1
    input_value = input(f"{count}.szám: ")
    if int(input_value) >= 0 and int(input_value) <= 100 and is_correct_number(input_value):
        numbers.append(input_value)

if len(numbers) > 0:
    print("A kért számok amelyeknek a számjegyek összege vagy 9 vagy 18: ")
    print(", ".join(numbers))
else:
    print("Nem kaptam megfelelő számot.")