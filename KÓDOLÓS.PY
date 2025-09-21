def is_valid_word(word: str) -> bool:
    """A szó érvényes, ha az összes karakter kódpontjának összege > 1000"""
    summa = 0
    for c in word:
        summa += ord(c)
    return summa > 1000

value = ""
i = 0
words = list()

while value.upper() != "STOP":
    i += 1
    value = input(f"{i}. szó: ")
    if is_valid_word(value) and value.upper() != "STOP":
        words.append(value)

if len(words) > 0:
    print(f"Az érvényes szavak listája: {', '.join(words)}")
else:
    print("Nem kaptam érvényes szavakat.")
