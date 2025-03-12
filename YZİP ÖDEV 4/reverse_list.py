isimler = []  
isimler2 = [] 
isimler3 = [] 
isimler4 = [] 

for i in range(5):
    a = input("Listeye eklenecek isim giriniz: ")
    isimler.append(a)

print("Orijinal Liste:", isimler)
isimler2 = isimler.copy()
isimler3 = isimler.copy()
isimler4 = isimler.copy()


# Yol 1: Dilimleme yöntemiyle ters çevirme
ters_list = isimler[::-1]

# Yol 2: sort() ile büyükten küçüğe sıralama
ters_list2 = sorted(isimler2, reverse=True)  # sort() yerine sorted() kullanıldı

# Yol 3: Manuel ters çevirme (swap yöntemi)
s = len(isimler3) - 1
for i in range(s // 2):
    tmp = isimler3[i]
    isimler3[i] = isimler3[s]
    isimler3[s] = tmp
    s -= 1

# Yol 4: reverse() metodu ile ters çevirme
isimler4.reverse()

print("Dilimleme ile ters:", ters_list)
print("Sıralama ile ters:", ters_list2)
print("Manuel ters çevirme sonrası:", isimler3)  # reverse() ile ters çevrilmiş hali
print("Reverse fonksiyonu ile: ", isimler4)
