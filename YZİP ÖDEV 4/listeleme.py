list = []

for i in range(5):
    a = int(input("Listeye eklenecek sayı giriniz: "))
    list.append(a)
print(list)

def hesapla():
    total = 0
    list.sort()
    
    en_buyuk = list[4]
    en_kucuk = list[0]

    for i in range(5):
        total = total + list[i]
    ort = total / (len(list))
    
    print(f"Ortalama: {ort}")
    print(f"En büyük: {en_buyuk}")
    print(f"En küçük: {en_kucuk}")

hesapla()