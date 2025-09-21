import random 

def create_ID(value: str) ->str:
    first_name = value.split()[0].lower() #vezetéknév
    last_name = value.split()[-1].lower() #kersztnév

    mirror = first_name[3::-1]        
    third = last_name[0:-1:3]
    szumma = 0

    for c in f"{first_name}{last_name}":
        szumma += ord(c)
    spec_chars = "!@#$%^&*()_+-=[]{}|;':\",.<>?/"
    index = szumma % len(spec_chars)

    
    current_spec_char = spec_chars[index]
    mixed_part = f"{mirror}{third}"[::3].upper() #**
    return f"{mirror}{mixed_part}{current_spec_char}{third}{szumma}"

value =""
while value.lower() != "q":
    value = input("Kérek egy nevet: ")
    if value.lower() != "q":
        
        while (" " not in value) and (len(value) < 3) and (not value.isalpha()) :  
            print("Helytelen nevet adott meg!")
            value = input("Kérek egy nevet: ")
            if value.lower() == "q":
                break
        
        print(create_ID(value))
    

print("Ön kilépett a programból")