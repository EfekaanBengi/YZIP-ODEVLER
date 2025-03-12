liste = []

for i in range(5):
    a = int(input("Listeye eklenecek sayı giriniz: "))
    liste.append(a)

print("Orijinal Liste:", liste)

liste2 = liste.copy()
liste2.sort()

i = 0
while i < len(liste2) - 1:  
    if liste2[i] == liste2[i + 1]:  
        liste2.pop(i + 1)  
    else:
        i += 1  

print("Tekrarsız Sıralı Liste:", liste2)
