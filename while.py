def is_valid_word(w):
    return len(w) == 3 or len(w) == 5

words = []
count= 0
word = " "

while word != "" and word != "quit":
    count += 1
    word = input(f"{count}. szó: ")
    if is_valid_word(word):
        words.append(word)

if len(words) != 0:
    print(", ".join(words))
else:
    print("Nincs szó.")