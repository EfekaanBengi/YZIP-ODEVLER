def hesap_makinesi(x,y,z):
    if z == "+" :
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        if y==0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:    
            print(x/y)
    else:
        print("Geçersiz işlem türü!")
        
hesap_makinesi(5, 3, '+')   # Çıktı: 5 + 3 = 8
hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
hesap_makinesi(4, 0, '/')   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
hesap_makinesi(6, 2, '%')   # Çıktı: Geçersiz işlem türü!
