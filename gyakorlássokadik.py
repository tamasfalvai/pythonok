import random


def calculate(value1, value2):
    count = 0
    for s in value1:
        if s == value2:
            count += 1
    return count


def do_some_random_numbs():
    randoms = []
    valamennyi = random.randint(1, 20)   #ennyiszer fog uj számot generálni 
    for i in range(valamennyi):
        randoms.append(random.randint(0,20))  # ez a tartomámy között fog uj számot 
    return randoms



def get_the_biggest_numb(randoms):
    the_biggets = 0
    count = 0
    for n in randoms:
        if n > the_biggets:
            the_biggets = n

    for n in randoms:
        if n != the_biggets:
            count += 1
            
    return the_biggets, count



value1 = input("Kérek egy szót: ")
value2 = input("Kérek egy betűt: ")
print(calculate(value1, value2))
print(get_the_biggest_numb(do_some_random_numbs()))