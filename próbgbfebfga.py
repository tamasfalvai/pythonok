import random

def get_start_word():
    words = ["ablak", "képes", "kenyér", "álmos", "vajas",
             "béka", "hasad", "kalap", "este", "talicska",
             "parabola", "pipere", "tábla"]
    return random.choice(words)

def is_valid_word(word1, word2):
    # True, ha az első szó utolsó két karaktere == a második szó első két karaktere
    return word1[-2:] == word2[:2]

def main():
    szolanc = []  # itt tároljuk az eddigi szavakat
    start = get_start_word()
    szolanc.append(start)
    
    print("Kezdő szó:", start)
    
    while True:
        uj_szo = input("Kérek egy új szót: ")
        
        # Ellenőrizzük, hogy az új szó megfelel-e a szabálynak
        if is_valid_word(szolanc[-1], uj_szo):
            szolanc.append(uj_szo)
            print("Szólánc:", " - ".join(szolanc))
        else:
            print("Helytelen szó. Vége a játéknak.")
            break

if __name__ == "__main__":
    main()
