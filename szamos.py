def drawNumber(value: str) -> None:
    if value.isdecimal():
        number = int(value)
        for i in range(1, number ,1):
            print("o " * i)
        for i in range(number, 0, -1):
            print("o " * i)
    else:
        print("Helytelen értéket adtak meg.")

n = input("Kérek egy számot: ")
print(drawNumber(n))