import random


def doitmyrandomnumb():
    return random.randint(0,100)


def main(random, value):
    számlálás = 0
    while value != random:
        számlálás += 1
        value = int(input(f"{számlálás}. szám:"))
        if random  <  value:
            print("A szám kisebb mint amit megadtál!")
        elif value  < random:
            print("A szám nagyobb mint amit te megadtál!")
    print(f"Gratulálok kitaláltad a számot! A szám nem volt más mint: {random} és {számlálás}.-dikra találtad ki ")


value = (1)
print("A program kitalál egy számot 0-100.-ig és azt neked kikell találni, és kilépés ENTERREL VAGY VÉGÉVÉL:")




while  value != "":
    main(doitmyrandomnumb(),value)