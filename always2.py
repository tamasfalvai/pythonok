def is_correct(n):
    if int(str(n)[0]) + int(str(n)[-1]) == 9 or int(str(n)[0]) + int(str(n)[-1]) == 18:
        return True
    
# ugyanaz

    #return int(str(n)[0]) + int(str(n)[-1]) == 9 or int(str(n)[0]) + int(str(n)[-1]) == 18



inputvalue = 1
count = 0
litsaaszámokhoz = []
lista2 = []
print("\nAdjon meg pozitív egész számnokta 100-ig!")



while inputvalue >= 0 and inputvalue <= 100:
    count += 1
    inputvalue = int(input(f"{count}. szám: "))
    if  inputvalue >= 0 and inputvalue <= 100 and is_correct(inputvalue):
        litsaaszámokhoz.append(inputvalue)





if len(litsaaszámokhoz) > 0: 
    print("A 9 és 18 számjegyes számok: ")
    print(litsaaszámokhoz)
else:
    print("Nme kaptam megfelelő számot.") 