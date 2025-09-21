import random

def get_start_word():
    words = ["ablak", "képes", "kenyér", "álmos", "vajas",
    "béka", "hasad", "kalap", "este", "talicska", "parabola",
    "pipere", "tábla"]
    return random.choice(words)

def is_valid_word(str1, str2):
    if str1[0:-2:-1] == get_start_word():
        return True


print("Szólánc-program. Az előző szó utólsó szótagja azonos a következő szó első szótagjával.")
print("Rontásnál kilép a program.")
print("2-3 jegyű mássalhangzók nem szerepelhetnek az utólsó szótagban!")

