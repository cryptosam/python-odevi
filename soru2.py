uzantilar = ['com', 'net', 'org', 'edu.tr', 'com.tr']

url = input("Url giriniz : ")

def urlKontrol(url):
    for i in range(len(url)):
        for j in uzantilar:
            if url[i:] == '.' + j:
                return True

    return False

print(urlKontrol(url))