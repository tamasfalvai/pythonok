lista = []
def do_myten_numbers():
    for i in range(10):
        számok = i +1
        lista.append(számok)



def my_summas(lista):
    összeg = sum(lista)
    return összeg


do_myten_numbers()
print(lista)
print(f"A számok összege: {my_summas(lista)}")