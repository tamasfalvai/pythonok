def count_wowels(value):
    vowels = "aáeéiíoóöőuúüű"
    count = 0
    for c in value:
        if c in vowels:
            count +=1
    return print(f"Az ön szava a(z) {value} és ez a szó {count} szótagból áll.")



w = input("Kérek egy szavat: ")
print(count_wowels(w))