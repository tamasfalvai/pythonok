import random

def get_average(number_list):
    summa = 0
    for n in number_list:
        summa = summa + n  # summa += n

    return summa / len(number_list)

# numbers = [1,2,3,4,5,6,7,8,9]

def get_random_number() -> int:
    return random.randint(0, 1000)

def push_number_list(my_list):
    for i in range(10):
        my_list.append(get_random_number())

def print_numbers(my_list):
    str_list = []
    for n in my_list:
        str_list.append(str(n))
    print(", ".join(str_list))

numbers = []
push_number_list(numbers)

print_numbers(numbers)

result = get_average(numbers)

print(f"A számok átlaga: {result}")