import random

def domyrandomnumb():
    lista = []
    for i in range(10):
        lista.append(random.randint(0,1000))
    return lista


def checkthenumbs(lista):
    good = []
    bad = []
    for c in lista:
        if c % 3 == 0 or c % 5 == 0:
            good.append(c)
    print(f"A 3-al és 5-el osztható számok {good}")




while checkthenumbs(domyrandomnumb) > 8:
    domyrandomnumb() 
    if checkthenumbs(domyrandomnumb) > 8:
        print(checkthenumbs(domyrandomnumb))