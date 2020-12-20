eposta = input("Eposta adresi giriniz : ")

def epostaKontrol(eposta):
    control1 = False

    for x in eposta:
        if x == "@":
            control1 = True

        if x == "." and control1:
            return True

    return False

print(epostaKontrol(eposta))