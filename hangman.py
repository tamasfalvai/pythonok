import random

def get_rnd_word(word_list: list[str]) -> str:
    return word_list[random.randint(0, len(word_list)-1)]


words = ["kanári", "vánkos", "tükör", "tányér", "kalap",
 "alma", "körte", "barack", "szilva", "banán",
 "narancs", "citrom", "eper", "málna", "ribizli",
   "szeder", "dinnye", "görögdinnye", "szőlő", "kiwi"]

word = get_rnd_word(words) # Függvényhívás


print(word)