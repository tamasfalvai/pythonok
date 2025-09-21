def is_check(numb):
    ÖSSZEG = 0
    for számjegy in str(numb):           #for ciklus, amely végigiterál a numb változó karakterein
        ÖSSZEG += int(számjegy)          
    return ÖSSZEG < 10



print("Adjon meg nekem számokat!")
print()
value = 0
listaajókho = []
számlálás = 0
lista = []



while str(value) != "":
    számlálás += 1
    value = input(f"{számlálás}.Szám: ")
    if value == "":
        break
    value = int(value)
    lista.append(value)
print("Ön kilépett a programból mert ENTERT nyomot.")
    



for szam in lista:
    if is_check(szam):
        listaajókho.append(szam)

if listaajókho:
    print("A számok melyeknek a számjegyeinek összege kisebb mint 10:", *listaajókho, sep=", ")

else:
    print("Nincs olyan szám melynek karaktereinek összege kisebb mint 10!")