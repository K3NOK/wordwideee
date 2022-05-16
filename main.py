Klucz = 5

def Szyfr(txt):
    Zaszyfr = ""
    for i in range(len(txt)):
        if znak > 122 - Klucz:
            Zaszyfr += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfr += chr(ord(txt[i]) + KLUCZ)
        return Zaszyfr
