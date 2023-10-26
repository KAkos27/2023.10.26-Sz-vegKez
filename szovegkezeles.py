def szepnapvan():
    szoveg: str = "Szép nap van!"

    print(szoveg[0])
    print(szoveg[1])
    print(f"A hossz: {len(szoveg)}")
    print(f"Utolsó: {szoveg[len(szoveg)-1]}")

    i: int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i += 1

def szovegkezeles():
    szoveg: str = "Ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper())

    x = szoveg.find("teszt")
    if x >= 0:
        print("Igaz")
    else:
        print("Hamis")

    i = szoveg.find("s")
    print(i)

    s = szoveg.title()
    print(s)

    a = szoveg.replace("teszt", "próba")
    print(a)

def szoveg_vissza(szoveg:str):
    print(szoveg[::-1])

def betuk_szama(szoveg:str):
    print(szoveg.count("a"))
    


