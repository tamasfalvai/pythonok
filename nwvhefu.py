import random

# 1 -> fej, 0 -> írás
# Pénzfeldobás-függvény (1. verzió)
def coinFlip(value):
    heads = []
    for i in range(value):
        number = random.randint(0, 1)
        if number == 1:
            heads.append(number)
    return heads

# Pénzfeldobás-függvény (2. verzió)
def coinFlip_2(value):
    h = 0
    w = 0
    for i in range(value):
        n = random.randint(0, 1)
        if n == 1:
            h += 1
        else:
            w += 1  # w = w + 1
    return h, w


inputValue = int(input("Hányszor dobjuk fel az érmét? "))

########### coinFlip_2 ****************

headCount, writeCount = coinFlip_2(inputValue)

print(f"Fejek száma 2: {headCount}, írások száma:  {writeCount}")

# *************************************
result = coinFlip(inputValue)
countHead = len(result)

print(f"Fejek száma: {countHead}, írás száma: {inputValue - countHead}")