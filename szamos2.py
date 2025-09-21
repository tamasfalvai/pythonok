def Draw_Numbers(value):
    if value.isdecimal():    # megnézzük hogy tényleg szám 2 ha igen akkor 
        vvalue = int(value)  # számmá alakítjuk 
        for i in range(1, vvalue, 1):   # egy ciklussal végig megyünk start 1 stop a SZÁM és step 1 előre írjuk 
            print(i * "x")              #kiirjuk annyiszor az annyiszor az x-et mint adott esetben a SZÁMszor
        for i in range(vvalue,0, -1):   #visszafele ismegismételjük 
            print(i * "x")
    else:
        print("Nem helyes a szám amit megadtál.")




value1 = input("Kérek egy számot: ")
Draw_Numbers(value1)