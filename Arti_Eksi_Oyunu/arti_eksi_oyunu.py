import time
import random

list = []

for i in range(1, 101):
    list.append(i)

rastgele = random.choice(list)


print("Merhaba bugün seninle bir oyun oynayacağız")
time.sleep(2)
print("Ben 1'den 100 e kadar bir sayı tutacağım ve sen tahmin etmeye çalışacaksın")
time.sleep(2)
print("Eğer sana '+' dersem bil ki sayı daha yüksek eğer sana '-' dersem bilki sayı daha düşük.")
time.sleep(2)
print("Hadi Başlayalım")



print("Ben sayımı tuttum")


while True:
    tahmin = int(input("Tahminin nedir:"))
    if tahmin > rastgele:
        print("Bu Yanlış : -")
        continue
    elif tahmin < rastgele:
        print("Bu yanlış: +")
        continue
    else:
        print("Tebrikler!!", rastgele,"Sayısını tutmuştum")
        break
        