print("kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

# int , integer => tam sayı
vade = 36
ekVade= 6
vade2 = "36"

# float, double, decimal => ondalıklı gösterim
aylikOdeme = 200.50

# bool, boolean => True veya False
yukseldiMi = True

    # matematiklsel operatörler
# toplama (+)
print(5+6)
print(vade+12)
print(vade + ekVade)
print(36 + 6)

# çıkarma (-)
print(5-6)
print(vade-12)
print(vade-ekVade)
print(36-6)

# çarpma (*)
print(5*6)
print(vade*12)
print(vade*ekVade)
print(vade*12)

# bölme (/)
print(5/6)
print(vade/12)
print(vade/ekVade)
print(vade/6)

yeniVade = vade /2
fiyat = 100
indirimleFiyat = fiyat -20

print(yeniVade)
print(indirimleFiyat)

# % => mod/kalan operatörü
print(100%2)
print(vade%5)
print(vade % ekVade)
print(30%10)

    # mantıksal operatörler => Çıktısı True/False yani BOOLEAN'dır
# eşitlik (==)
print(1==1) # True
print(1==2) # False

# Büyük küçük karşılaştırma (< >)
print(1>2) # False
print(3>1) # True
print(1>1) # False
print(1>=1) # True (Büyük eşittir)
print(1<=1) # True (Küçük eşittir)

# eşit değildir (!=)
print(1 != 1) # False
print(1 != 2) # True

# VE, VEYA (or, and)
print(1 > 2 or 5 > 2) # True
print(1 > 2 or 5 < 2) # False
print(1 > 2 and 5 > 2) # False
print(1 < 2 and 5 > 2) # True

print(1 > 2 or 5 > 2 and 3 > 2) # True
print(1 > 2 and 5 > 2 and 3 > 2) # False

    # Karar Yapıları
# if else elif
sayi1 = 10
sayi2 = 15
# sayi1 ,sayi2'den daha büyükse ekrana sayi1 daha büyük yazsın
if (sayi1 > sayi2):
    print("sayi1 büyüktür")
    print("hala if bloğuunun içi")
elif (sayi1 == sayi2): 
# eğer ilk koşul sağlanmıyorsa başka koşullara bakılması için kullanılır
    print("iki sayı eşittir")
else:
# eğer hiçbir ifade doğru değilse burası çalışır
    print("sayi1 büyük değildir")

print("if bloğunun dışı")