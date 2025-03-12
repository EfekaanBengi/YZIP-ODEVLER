    ### SINIFLAR
# Sınıfın içindeki tüm metodların kullanılması gerekmez.
# Sınıfın içindeki metodların kullanılma sırası yoktur.
class Human: 
    # name = "Efecones"
    # built-in
    def __init__(self,name): # Constructor - İnitialize Metodu
        print("Bir Human instance'i üretildi")
        self.name = name

    def __str__(self) -> str:
        return "Str Fonksiyonundan Dönen Değer"

    def talk(self,sentence): 
        # Self java dilindeki .this görevi görüyor
        # ilk parametre her zaman self'tir 
        # (başka bir isim de verebiliriz)
                                                # fonksiyonun içindeki bir data 
        print(f"{self.name} is talking")              #için self kullanmaya gerek
        print(f"{self.name}: {sentence}")             # yok fakat Class içerisindeki
                                           # bir datayı kullanmak istediğimizde
    def walk(self):                            # self kullanmalıyız.
        print(f"{self.name} is walking")

# human 1 in bir Human olduğunu belirtiyoruz
# Aslında zaten çağıracağımız fonkisyonu biliyorsak buna gerekyok

human1 = Human("Efecones")
# human1.name = "Ahmet"
human1.walk()
human1.talk("Merhaba")
print(human1)

human2 = Human("Ömer Yiğit")
# human2.name = "Cem"
human2.walk()
human2.talk("Naber")
print(human2)


  ## Modul Yapısı - Modules
import matematik as mt  # alias
import random           # built-in 
                        # packages
"""
print(matematik.bol(12,4))
print(matematik.cikar(3,8))
"""

print(mt.carp(5,85))
print(random.randint(0,100))