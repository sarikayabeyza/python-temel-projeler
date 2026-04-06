 #4. Ödev - RPG Karakter Filtreleme

# Veri setini tanımlama 
karakterler = [
    {"isim": "Aragorn", "sinif": "savasci", "seviye": 15, "hp": 220, "altin": 500},
    {"isim": "Gandalf", "sinif": "buyucu", "seviye": 20, "hp": 140, "altin": 300},
    {"isim": "Legolas", "sinif": "okcu", "seviye": 12, "hp": 160, "altin": 550},
    {"isim": "Gimli", "sinif": "savasci", "seviye": 10, "hp": 200, "altin": 600},
    {"isim": "Thranduil", "sinif": "okcu", "seviye": 14, "hp": 175, "altin": 900},
    {"isim": "Saruman", "sinif": "buyucu", "seviye": 18, "hp": 130, "altin": 800}
]

# Lambda kullanarak sınıf kontrolü yapıyoruz

# Karakterin sınıfının "okçu" olup olmadığını kontrol ediyoruz
okcu_mu = lambda k: k["sinif"] == "okcu"

# Seviye > 10 ve HP > 150 kontrolü
guclu_mu = lambda k: k["seviye"] > 10 and k["hp"] > 150




# Comprehension ile Ekip Seçimi 

# 1. Seviyesi 15'ten büyük olanların isim listesi
ust_seviye_isimler = [k["isim"] for k in karakterler if k["seviye"] > 15]

# 2. Altın miktarına göre zengin/fakir etiketi ekleme (Tuple listesi)
ekonomi_durumu = [(k["isim"], "zengin" if k["altin"] > 500 else "fakir") for k in karakterler]




# Sonuçları Yazdırma

print("Üst Seviye Karakterler (Lvl > 15):", ust_seviye_isimler)
print("\nKarakterlerin Ekonomi Durumu:")
for durum in ekonomi_durumu:
    print(durum)

# Lambda testi örneği
print("\nAragorn güçlü mü?:", guclu_mu(karakterler[0]))