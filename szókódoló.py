def is_valid_word(word):
    számok = "0123456789"
    for szó in word:
        if számok in word and len(value) >= 2 :
            print("A szó érvénytelen!")
            return False
        else:
            return True
        



def decoderor_word(word):
    kódoltszó = [ord(karakter) for karakter in word]
    print(f"Szó: {word}")
    print(f"A kódolt szó: {kódoltszó}")




print("Adjon meg szavakat!")
print()
value = "hhjfvtcftzc"
számlálás = 0


while value.lower() != "q":
    számlálás += 1
    value = input(f"{számlálás}.Szó: ")
    if is_valid_word(value):
        decoderor_word(value)
    else:
        print("Ön KILÉPETT a programból.")



#A q-t is végig csinálja és nem áll le hanem végig csinálja és a a 2-nél kevesebb karakterű szavaakt is megcsinálja!!!!!!!!!