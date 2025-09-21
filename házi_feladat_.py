import random


def calculate(value):
    count = 0
    for c in str(value):   
        count += int(c)    
    return count

#Csinálunk egy olyan függvényt amelyben, létre hozunk egy változót, végig megyünk a for ciklussal a be kért számon a str-ing segítségével és a változóban lévő nulla értékhez hozzá adjuk a pl: első számát, jó mert addig megy amennyi szám van szval ha 187654236 akkor -- 187654236


value = int(input("Kérek egy számot: "))
print("A számjegyek összege:", calculate(value))





def longest_word(words):
    longest = ""                 # ide mentjük a leghosszabb szót
    for w in words:              #elindulunk a listán 
        if len(w) > len(longest): # ha a lista egyik tagja nagyobb mint a (legnagyobb) változós szónk akkor kicseréljük a ketttt
            longest = w
    return longest, len(longest)   #vissza adjuk a leghosszabat és a hosszát is 


szavak = ['Alma', 'Körte', 'Banán', 'Narancs', 'Mandarín', 'Citrom', 'Kivi', 'Eper', 'Málna', 'Sárgabarack', 'Cseresznye', 'Meggy', 'Szőlő', 'Ananász', 'Mangó']
print(szavak)
word, length = longest_word(szavak)
print("A leghosszabb szó:", word)
print("Hossza:", length)






def caunting_a_in_word(value):
    wovels = "aáeéiíoóöőuúüű"
    count = 0
    wwovels = ""
    
    for v in value:
        if v in wovels:
            count += 1
            wwovels += v   # minden magánhangzót hozzáfűzünk, ismétléssel is
    print(f"A szóban {count}-nyi magánhangzó van és ezek: {wwovels}")           
    
    
value = input("Kérek egy szót: ")
print(caunting_a_in_word(value))






""" 
def password(value):
    # Legalább 8 karakter hosszú
    if len(value) < 8:
        return False   #ha nem akkor vissaz dobja return falseal és nem fut le tovább de ez csak akkor ha false 
    
    #Van-e benne nagy betű
    for p in value:
        if not p.isupper():
            return False
        if not p.isdigit():
            return False
        
    print(f"Gratuláok a te jelszód helyes: {value}")
        


# Tesztelés
print("A program egy jelszót kér, amelynek legalább 8 karakter hosszúnak, legalább egy számot és egy nagybetűt kell tartalmaznia.")
value = input("Kérek egy jelszót: ")

if password(value):
    print(f"Helyes a jelszó: {value}")
else:
    print("A jelszó nem megfelelő. Győződj meg róla, hogy legalább 8 karakter hosszú, van benne egy nagybetű és egy szám.")
 """













def numbers():
    num_list = list(range(1, 31))  # 1-től 30-ig
    numbs_list = []
    for n in num_list:
        if n % 3 == 0:
            numbs_list.append(n)
    return numbs_list  # visszaadjuk a listát

# Függvény hívása
oszthato_3 = numbers()
print(f"A 3-mal osztható számok: {oszthato_3}")

# Ha külön szeretnéd a get_num_list függvényt
def get_num_list(lista):
    return lista

lista_vissza = get_num_list(oszthato_3)
print(f"A get_num_list függvénnyel visszaadva: {lista_vissza}")




import random

def get_nums():
    numbs = []
    random_nums = random.randint(1, 30)  # hány szám legyen a listában
    for i in range(random_nums):
        randoms = random.randint(0, 30)
        numbs.append(randoms)  # a véletlenszámot adjuk a listához

    count = len(numbs)
    print("A lista:", numbs)
    print("A lista hossza:", count)
    return numbs

# Függvény hívása
get_nums()
