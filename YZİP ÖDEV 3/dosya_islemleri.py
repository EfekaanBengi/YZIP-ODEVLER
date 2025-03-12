# Kullanıcıdan 5 satır veri alıp dosyaya yazan ve sonra okuyup ekrana yazdıran Python programı

dosya_yolu = "c:/Users/efeka/OneDrive/Masaüstü/python/YZİP-A/Ödevler/YZİP ÖDEV 3/kullanici_verisi.txt"

def dosyaya_yaz(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for i in range(5):
            satir = input(f"{i+1}. satırı girin: ")
            dosya.write(satir + "\n")

def dosyayi_oku(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        print("\nDosyanın içeriği:")
        for satir in dosya:
            print(satir.strip())

dosyaya_yaz(dosya_yolu)
dosyayi_oku(dosya_yolu)
