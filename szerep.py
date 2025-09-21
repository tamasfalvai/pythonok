def check_the_values(életkor, magasság,név):
    if életkor < 28 and magasság > 170:
        print(f"Örülök,{név} megfelelsz a kitételeknek.")
    else: 
        print(f"Sajnálom,{név} nem felelsz meg a feltételeknek.") 




print("Ez egy olyan kérdőív amivel megtudhatja hogy alkalmas e a film szerepére.")
print()
value1 = int(input("Kérek egy életkort: "))
value2 = int(input("Kérek egy magasságot: "))
value3 = input("Kérek egy nevet: ")
check_the_values(value1,value2, value3)