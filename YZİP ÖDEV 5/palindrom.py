def palindrom_kontrol(kelime):
    return kelime == kelime[::-1]


print(palindrom_kontrol("kek"))  
print(palindrom_kontrol("masa"))  