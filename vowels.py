def check_the_vowels(value):
    vowels = "aáeéiíoóöőuúüű"
    count = 0
    for c in value:
        if c in vowels:
            count += 1
    return count 



value = input("Kérek egy szót: ")
print(f"A {value} szóban ennyi magánhangzó van {check_the_vowels(value)}.")