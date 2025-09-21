def print_o_s(value):
    if value.isdecimal():
        ValueInput = int(value)
        for i in range(1,ValueInput , 1):
            print("x" * i)
        for i in range(ValueInput, 0, -1):     #start, stop , step
            print("x" * i)
    else:
        print("Helytelen számnot adtál meg. ")

value1 = input("Kérek egy számot: ")
print(print_o_s(value1))