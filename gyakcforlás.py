def summa_digits(value):
    count = 0
    if len(value) > 1:
        for s in value:
            count += int(s)
    return count




def get_longest_word(word_list):
    longest = ""
    for s in word_list:
        if len(s) > len(longest):     #megnézzük hogy ha a listában lévő szó nagyobb ak = longesttel
            longest = s

    count = 0
    for s in word_list:
        if longest != s:
            count += 1
    


    return longest, count 
# vissza adja a longestet- és azt h hanyadik a listában 



value = input("Kérek egy számot: ")
print(summa_digits(value))
wordlist = ["kalap", "csemege", "szelemen", "suhan", "végvár"]
print(get_longest_word(wordlist))