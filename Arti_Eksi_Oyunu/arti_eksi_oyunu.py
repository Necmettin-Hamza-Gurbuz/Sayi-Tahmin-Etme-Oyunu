import time
import random

liste = []
for i in range(1, 101):
    liste.append(i)

rastgele = random.choice(liste)

print("Merhaba! Bugün seninle bir oyun oynayacağız.")
time.sleep(3)
print("Ben 1'den 100'e kadar bir sayı tutacağım ve sen tahmin etmeye çalışacaksın.")
time.sleep(3)
print("Eğer sana '+' dersem bil ki sayı daha yüksek, eğer sana '-' dersem bil ki sayı daha düşük.")
time.sleep(3)
print("Tamamdır! Hadi başlayalım.")
time.sleep(2)

deneme_hakki = int(input("Kaç deneme hakkı istersin?: "))

while deneme_hakki > 0:
    tahmin = int(input("Tahminin nedir: "))
    
    if not 1 <= tahmin <= 100:
        print("Lütfen belirtilen aralıkta bir sayı giriniz.")
        continue

    if tahmin > rastgele:
        print("Bu yanlış: -")
        time.sleep(0.4)
        
    elif tahmin < rastgele:
        print("Bu yanlış: +")
        time.sleep(0.4)
        
    else:
        print("Tebrikler!!", rastgele, "Sayısını tutmuştum.")
        break

    deneme_hakki -= 1

    if deneme_hakki == 0:
        print("Maalesef hakkın doldu. Doğru sayı:", rastgele)

time.sleep(5)
