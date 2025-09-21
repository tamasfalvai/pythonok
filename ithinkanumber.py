import random

def create_random():
    return random.randint(0, 100)

def főrész(value):
    tipps = 0  
    while value != szám:
        tipps += 1   
        value = input(f"{tipps}. Tipp: ")

        if value == "":  # Ha üres az input, kilépünk
            return print("Ön ENTER-T nyomot és ezzel a programból kilépett!!")  # Visszaadja h ENTER-t nyomtál

        value = int(value)  # Csak akkor próbálja átalakítani, ha nem üres

        if value < szám:
            print("A szám nagyobb mint amit te adtál meg.")
        elif value > szám:
            print("A szám kisebb mint amit te adtál meg.")
        else:
            print(f"\nGratulálok a szám melyet kikellett találni nem más mint {szám} és {tipps}.-re sikerült kitalálni.")

print("\nGondoltam egy számot, találd ki!")
value = ""  # Kezdőérték
szám = create_random()
főrész(value)
