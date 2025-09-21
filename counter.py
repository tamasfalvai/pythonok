import random
#Ez a program megszámolja a 20 generált számból mennyinek van 9-es a középső szám.

def getRndNumber(start: int, end: int) -> int:
    '''Véletlen-szerű számokat készít.'''
    return random.randint(start, end)

def createNumbers(count: int = 10) -> list[int]:
    '''Számok listáját adja vissza'''
    numbers = []
    for i in range(count):
        numbers.append(getRndNumber(100, 1000))
    return numbers

def isValidNumber(number: int) -> bool:
    '''Érvényes az a szám, amelyiknek középső karaktere "9"'''
    number = str(number)            #szöveggé alakítás 
    if len(number) % 2 == 0:        #ha a karakter száma páros akkor nem jó mert nincs egyértelmű középső száma 
        return False        
    index = len(number) // 2        # // egész osztás 
    return number[index] == "9"     

# Megszámlálás tétele:
def count_valid_numbers(num_list: list[int]) -> int:
    count = 0
    for n in num_list:
        if isValidNumber(n):
            count += 1
    return count

numbers = createNumbers(50)

print(numbers)
print(f"Középső számjegyük kilenc: {count_valid_numbers(numbers)}")



#index = len(number) // 2        # // egész osztás 
# return number[index] == "9" 

#Magyarázata : a "12345" szónak a hosszának a felét nézzük ami azért jó mert eben az esetben 
# az 2 és a 2. index az a középső karakter és ha kilenc akkor jó ha nem akkor nem 