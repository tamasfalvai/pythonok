def my_checket(value):
    return len(value) == 3 or len(value) == 5
        
    

löszegekre = []
hanyadik = 0
value = input("uzvizvg")
quit =("quit")

print()
print("A program 3 és 5 karakter hosszú szavakat gyűjti! kilépés ENTERREL VAGY QUITTAL.")


while value != "" or quit.lower:
    hanyadik +=1
    value = input(f"{hanyadik}. Szó: ")




if my_checket(value):
    löszegekre.append(value)
    print(f"A 3 vagy 5 karakter hosszú szavak: {löszegekre}")
else:
    ("Ön nem adott meg nekem 3 vagy 5 karakter hosszú szót.")