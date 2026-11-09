branslar = ("Yazılım", "Tasarım", "Pazarlama")
tum_ogrenciler = []

ogrenci1_ad = " Merve Dişci ".strip()
tum_ogrenciler.append([ogrenci1_ad, ["Yazılım"]])

ogrenci2_ad = " Mehlike Şahin ".strip()
tum_ogrenciler.append([ogrenci2_ad, ["Tasarım", "Pazarlama"]])

ogrenci3_ad = " Sevim Sarıkaya ".strip()
tum_ogrenciler.append([ogrenci3_ad, ["Yazılım", "Tasarım"]])

baskan_ad = " Ayşenur Alkan ".strip()
tum_ogrenciler.insert(0, [baskan_ad, ["Yazılım", "Tasarım", "Pazarlama"]])

print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")

for ogrenci in tum_ogrenciler:
    if ogrenci[0] == "Ayşenur Alkan":
        tum_ogrenciler.remove(ogrenci)
        break

cikan_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {cikan_ogrenci[0]}")

tum_ogrenciler.append(["Lale Sude", ["Tasarım"]])

print("\nMevcut Orijinal Liste:")
print(tum_ogrenciler)

gecici_sirali = sorted(tum_ogrenciler)
print("\nGeçici Olarak Sıralanmış Liste (sorted):")
print(gecici_sirali)

print("Orijinal Listenin Değişmediğinin Kanıtı (Orijinal Liste):")
print(tum_ogrenciler)

tum_ogrenciler.sort()
print("\nKalıcı Olarak Sıralanmış Ana Liste (sort):")
print(tum_ogrenciler)
