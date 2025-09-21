def your_name(value):
    print("A Te neved ebből áll: ")
    Neved = value.upper()  # Minden betű nagybetűs
    Neved = "-".join(Neved)  # Kötőjelet tesz a betűk közé
    return Neved  # Csak az átalakított nevet adja vissza

bekérek = input("Hogy hívnak?: ")
print(your_name(bekérek))  # Kiírjuk az eredményt
