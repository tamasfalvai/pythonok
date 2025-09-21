import random 

#1 a fej , 
#2 a iras 

def coin_flip(value):
    heads = []
    for i in range(value):
        number = random.randint(0,1)
        if number == 1:
            heads.append(number)
            headok = len(heads)
    return print(f"A fejek száma: {headok}")

value = int(input("Hányszor dobjuk fel az érmét: "))
coin_flip(value)