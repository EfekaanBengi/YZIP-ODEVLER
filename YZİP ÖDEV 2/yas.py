## 3

yas = int(input("Yaşınızı girin: "))


if 0 <= yas <= 12:
    grup = "Çocuk"
elif 13 <= yas <= 19:
    grup = "Genç"
elif 20 <= yas <= 59:
    grup = "Yetişkin"
elif yas >= 60:
    grup = "Yaşlı"
else:
    grup = "Geçersiz yaş"

print(f"Yaş grubunuz: {grup}")
