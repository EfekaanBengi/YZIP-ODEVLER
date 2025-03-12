def kac_yil_sonra_100_yas(yas):
    if yas < 100:
        return 100 - yas
    else:
        return "Zaten 100 yaşında veya daha büyük!"


print(kac_yil_sonra_100_yas(25))  
print(kac_yil_sonra_100_yas(100)) 
