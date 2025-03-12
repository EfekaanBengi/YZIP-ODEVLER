### 2

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))


toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme hatası)"


print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")