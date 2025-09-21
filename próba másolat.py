def check_the_number(numb,lista):
    if numb == "stop": 



        return False
    if "," in str(numb) or "." in str(numb) or 0 > int(numb):   #feltétel 
        print("Helytelen értéket adtál meg.")
        return False



    else:                        #Ha hamis a feltétének hozzáadjuk a listához
        lista.append(int(numb))
        return True
        
value = 0
számlálás = 0
lista = []
print("A program száámokat kér be")

while value != "stop":
    számlálás += 1
    value = input(f"{számlálás}.szám: ")
    check_the_number(value, lista)
print("Ön kilépett a programból.")



if len(lista) == 0:
    print("Nem volt helyes szá amely pozitív és egsélz is lett volna:)")
else:
    print(f"A pozitív egész számok: {lista} ")



#Magyar nyelven

#Bejön a str-ként a input és ha szám akkor is hadjuk str-ként mert ahho hogy megnezzük h van e benne ",", "." igy kell
#Ellenőrizzük ha a feltételeknek nem felel meg akkor hozzáadjuk a ("JÓ") listához 

#Bizonyos helyen a stop nem működik