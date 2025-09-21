import random 

def do_my_random_number():
    '''Véletlen szám generátor amit ki kell majd találnod.'''
    return random.randint(0,100)

def what_is_the_number(random_number, input_number):
    if input_number > random_number:
        print("Adj meg kisebb számot")
    elif input_number < random_number:
        print("Adj meg nagyobb számot")
    else:
        print("Gratulálok, a számot ki találtad.")
    

randommnmb = do_my_random_number()
print(randommnmb)
print("Gondoltam egy számot 0 - 100 között, TALÁLD ki!")
input_value = 0


while input_value  > 0 or 100  > input_value:
    input_value2 = int(input("KÉREK EGY OLYAN SZÁMOT AMELY 0-100: "))



while input_value != do_my_random_number():
    input_value2 = int(input("Kérek egy számot: "))
    what_is_the_number(randommnmb,input_value2)