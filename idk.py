kezdőé = int(input("Start: "))
stopé = int(input("Stop: "))
step = int(input("Lépés: "))


lista = []
for szám in range(kezdőé, stopé, step):
    if szám  == 0:
        lista.append(szám)


favoriteword = input("Mi a kedvenc szód?: ")

cfavoriteword= favoriteword[0:3:1]
print(f"A kedvenc szód első három karaktere: {cfavoriteword}")

c2fVORITEWORD =  favoriteword[0::2]
print(f"A kedvenc szód minden masodik karaktere: {c2fVORITEWORD} ")

backfavoritewrod = favoriteword[::-1]
print(f"A szó visszafele: {backfavoritewrod}")




print(f"Az 5el oszthatók száma: {igen = len(lista)} ")
