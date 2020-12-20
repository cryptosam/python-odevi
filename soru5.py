#gelen giden tanımlamaları başı
def komut(deger):
    if deger == "receive":
        return 3
    elif deger == "send":
        return 4
    else:
        return 0

def komutYaz(deger):
    if deger == "receive":
        return "Gelen"
    elif deger == "send":
        return "Giden"
    else:
        return "Geçersiz"
#gelen giden tanımlamaları sonu
#1. bölümde verilen değerlere göre sinyal kısmı başlangıcı
def birinciBolum(deger):
    deger = int(deger)
    if 0 <= deger <= 50:
        return "Çok Zayıf Sinyal"
    elif 50 <= deger <= 100:
        return "Zayıf Sinyal"
    elif 100 <= deger <= 150:
        return "Orta Sinyal"
    elif 150 <= deger <= 200:
        return "Güçlü Sinyal"
    elif 201 <= deger <= 255:
        return "Çok Güçlü Sinyal"
    return "Hata"
#1. bölümde verilen değerlere göre sinyal kısmı sonu
#2. bölümde verilen değerlere göre cihazlar kısmı başı
def ikinciBolum(deger):
    deger = int(deger)
    if deger == 1:
        return "Televizyon"
    elif deger == 2:
        return "Çamaşır Makinesi"
    elif deger == 3:
        return "Buzdolabı"
    elif deger == 4:
        return "Fırın"
    else:
        return "Hata"
#2. bölümde verilen değerlere göre cihazlar kısmı sonu
#3. bölümde cihaz on of kontrolü başlangıcı
def ucuncuBolum(deger):
    deger = int(deger)
    if deger == 0:
        return "Off"
    else:
        return "On"
#3. bölümde cihaz on of kontrolü sonu
#4. bölüm cihazdan yanıt istenip istenmediği başı
def dorduncuBolum(deger):
    if deger == 0:
        return "Cevap İstenmiyor"
    else:
        return "Cevap İsteniyor"
#4. bölüm cihazdan yanıt istenip istenmediği sonu

#kod giriş kısmı
kod = input("Komut giriniz : ")

komutlar = kod.split('\\n')

for i in range(0, len(komutlar)-1):
    parametre = komutlar[i].split('-')

    if komut(parametre[0]) > 0:
        if komut(parametre[0]) == len(parametre)-1:
            if birinciBolum(parametre[1]) == "Hata":
                print("Error : birinci bölüm hatalı")
            elif ikinciBolum(parametre[2]) == "Hata":
                print("Error : ikinci bölüm hatalı")
            elif ucuncuBolum(parametre[3]) == "Hata":
                print("Error : üçüncü bölüm hatalı")
            else:
                print("Kod Tipi : " + parametre[0] + " - " + komutYaz(parametre[0]))
                print("Sinyal Gücü : " + parametre[1] + " - " + birinciBolum(parametre[1]))
                print("Cihaz : " + parametre[2] + " - " + ikinciBolum(parametre[2]))
                print("Durumu : " + parametre[3] + " - " + ucuncuBolum(parametre[3]))

                if komut(parametre[0]) == 4:
                    print("Cevap : " + parametre[4] + " - " + dorduncuBolum(parametre[4]))
        else:
            print("Error : birinci bölüm hatalı")
        if i < len(komutlar)-2:
            print('-----')
    else:
        print("Error : send ya da receive içermiyor")
#kod giriş kısmının sonu