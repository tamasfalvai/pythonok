import random

def get_random_number() -> int:
    '''Véletlen-szerű számot ad vissza 0 és 100 között'''
    return random.randint(0, 100)

def validate(random_number: int, input_number: int) -> bool:
    if input_number > random_number:
        return 1
    elif input_number < random_number:
        return -1
    else: 
        return 0

print("Gondoltam egy számot 0 és 100 között. Találd ki!")

guessed_number = get_random_number()
print(guessed_number)
value = -1
count = 0

while value != guessed_number:
    count += 1
    #input_string = input(f"{count}. tipp: ")
    # Mi van, ha a felhasználó betűt vagy üres sztringet ad meg???
    value = int(input(f"{count}. tipp: "))
    result = validate(guessed_number, value)

    if result == 1:
        print("A gondolt szám kisebb.")
    elif result == -1:
        print("A gondolt szám nagyobb.")
    else:
        print(f"Gratulálok! A gondolt szám {guessed_number} volt.")

    # Ternary operátor alkalmazásával így néz ki:
    '''
    message = "A gondolt szám kisebb." if result == 1 else "A gondolt szám nagyobb." if result == -1 else f"Gratulálok! A gondolt szám {guessed_number} volt."
    '''

    # print(message)