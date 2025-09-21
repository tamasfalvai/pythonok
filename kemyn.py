def do_the_calculate(value):
    value = value.replace(" ", "")
    if "+" in value:
        elsőérték = value.split("+")[0]
        másodikérték = value.split("+")[-1]
        eredmény = int(elsőérték) + int(másodikérték)
        return eredmény
    
    if "-" in value:
        elsőérték = value.split("-")[0]
        másodikérték = value.split("-")[-1]
        eredmény = int(elsőérték) - int(másodikérték)
        return eredmény
    


    if "*" in value:
        elsőérték = value.split("*")[0]
        másodikérték = value.split("*")[-1]
        eredmény = int(elsőérték) * int(másodikérték)
        return eredmény



print("A program kiszámítja az általad megadott kiszámítandót.")

input_value = ""
while input_value.lower() != "q":
    input_value = input("Kérek egy műveletet (q a kilépéshez): ")
    if input_value.lower() != "q":
        print(do_the_calculate(input_value))