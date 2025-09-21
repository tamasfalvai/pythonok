def check_the_wowels(value):
    vowels = "aáeéiíoóöőuúüű"
    count = 0
    for c in value:
        if c in vowels:
            count += 1
    return count

szó = input("Kérek egy szót: ")
print(f"Ebben a {szó} szóban {check_the_wowels(szó)} szótag van")