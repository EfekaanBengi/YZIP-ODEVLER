faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)

faiz = str(faiz) # float değeri str ye çevirme
print(type(faiz))

# kullanıcadan değer alma
# vade = int(input("Lütfen istediğiniz vade sayısını giriniz"))
# başına int yazılmazsa string olarak kabul eder
print(type(vade))
print(vade)


# String interpolation

print("Seçtiğiniz vade: "+ str(vade))
# print("Seçtiğiniz vade: {vadeSayısı}".format(vade))
print(f"Seçtiğiniz vade: {vade}")


### LİSTELER
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi","Ev Kredisi","Taşıt Kredisi"]
type(krediler)
print(krediler[0]) # => [0] ihtiyaç kredisi [1] Taşıt Kredisi [2] Ev Kredisi

print(len(krediler)) # length. son index = length -1

dizi = ["Vade",10,20,10.1,False] # Karışık bir dizi oluşturabiliriz
print(dizi)

krediler.append("Özel Kredi") # listenin sonuna eleman ekler
print(krediler)
krediler.pop(0) # index girilmezse son satırı siler
print(krediler)
krediler.remove("Taşıt Kredisi") # listede eşleşen ilk elemanı siler
print(krediler)
krediler.extend(["Y Kredisi ","X Kredisi "])
print(krediler)

    ### DÖNGÜLER ### For - Foreach - While
# For Döngüsü
x = 10
for i in range(10):
    print(i)
print("****************")
for i in range(5,x):
    print(i)
print("****************")
for i in range(0,100,8):
    print(i)

for kredi in krediler:
    print(kredi)

# While Döngüsü - Sonsuz Döngü
i = 0
while i<10:
    print("x")
    i += 1

print("***************")
i = 0
while True:
    print("x")
    i += 1
    if i >= 10:
        break 

print("***************")
i=0 
while i < len(krediler):
    print(krediler[i])
    i += 1

print("***************")

i=0 
while i < len(krediler):
    if krediler[i] == "Taşıt Kredisi":
        break
    print(krediler[i])
    i += 1


print("***************")

i=0 
while i < len(krediler):
    print(krediler[i])
    i += 1
    if krediler[i] == "Taşıt Kredisi":
        break

print("***************")

i=0 
while i < len(krediler):
    print(krediler[i])
    if krediler[i] == "Taşıt Kredisi":    # While Döngüsünde
        break                        # i değerinin hangi satırda
    i += 1                           # arttırıldığı çok önemlidir 


    ### FONKSİYONLAR - Definition
fiyat = 100
indirim = 20

def indirimHesapla():
    print(fiyat-indirim)

indirimHesapla()

## Parametreler ile hesaplama
def hesapla(a,b):
    print(a*b)

hesapla(20,5)
hesapla(14,2)
hesapla(7,36)

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("Efekaan")

def calculateSale(price,discount):   
    a = (price*discount)/100    # Daha karışık işlemler de   
    print(price-a)       # fonksiyonlar içerisinde yaptırılabilir   

calculateSale(100,20)