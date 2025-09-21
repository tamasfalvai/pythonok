def évesvizsg(value):
    if value  >= 100:
        print(f"{value} életkorához gratulálok.")
    else:
        szám = 100
        eredmény = szám - value
        print(f"{eredmény} év mulva leszel 100 éves.")


print()
print("A program az életkorát számolja i hogy hány év mulva lesz 100 éves.")
value = int(input("Hány éves vagy?: "))
sorszám = 0
évesvizsg(value)



while value != 100:
    sorszám += 1
    value = int(input("Hány éves valamelyik rokonod?: "))