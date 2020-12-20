girilen = input("İfade giriniz : ")
aranan = input("Aranacak ifade giriniz : ")

sira = girilen.find(aranan)

if sira > -1:
    print(girilen[sira-1:sira] + aranan + girilen[len(aranan)+sira:len(aranan)+sira+1])
else:
    print("İfade içinde bulunamadı")
