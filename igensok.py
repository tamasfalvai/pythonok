def count_vowel_in_word(word: str) -> int:
    vowels = "aáeéiíoóöőuúüű"
    count = 0
    for c in word:
        if c in vowels:
            count += 1
    return count

w = input("Kérek egy szót: ")
print(f"A {w} szóban {count_vowel_in_word(w)} db szótag van.")
            