## 2

notu = float(input("Notunuzu girin: "))


if 90 <= notu <= 100:
    harf = "A"
elif 80 <= notu < 90:
    harf = "B"
elif 70 <= notu < 80:
    harf = "C"
elif 60 <= notu < 70:
    harf = "D"
elif 0 <= notu < 60:
    harf = "F"
else:
    harf = "Geçersiz not"

print(f"Notunuz: {harf}")
