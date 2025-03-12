def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme hatası)"
    
    return {
        "Toplam": toplam,
        "Fark": fark,
        "Çarpım": carpim,
        "Bölüm": bolum
    }

sonuc = hesap_makinesi(10, 2)
print(sonuc)
