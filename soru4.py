sayac = 0
for i in range(102, 988):
    i = str(i)

    a = i[0]
    b = i[1]
    c = i[2]

    if not a == b and not a == c and not b == c:
        print(i)
        sayac += 1

print('Toplam : ', sayac)