# Kérj be egy számot string formátumban
num_str = input("Kérem, adjon meg egy számot: ")

# Konvertáljuk integer-re
num = int(num_str)

# Ellenőrizzük, hogy páros vagy páratlan
if num % 2 == 0:
    print(f"A(z) {num} páros szám.")
else:
    print(f"A(z) {num} páratlan szám.")
