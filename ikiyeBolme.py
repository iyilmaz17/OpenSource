import math

def f(x):
    return 4.5 * x - 2 * math.cos(x)

def ikiyeBolme(alt_sinir, ust_sinir, tol=1e-6, max_iter=100):
    if f(alt_sinir) * f(ust_sinir) > 0:
        print("Seçilen aralıkta kök yok.")
        return None, None
    
    iterasyon = 0
    while (ust_sinir - alt_sinir) / 2 > tol and iterasyon < max_iter:
        orta_nokta = (alt_sinir + ust_sinir) / 2
        if f(orta_nokta) == 0:
            break
        elif f(orta_nokta) * f(alt_sinir) < 0:
            ust_sinir = orta_nokta
        else:
            alt_sinir = orta_nokta
        iterasyon += 1

    return orta_nokta, (alt_sinir, ust_sinir)

# Kullanıcıdan alt ve üstü sınırı iste 
alt_sinir = float(input("Alt sınırı girin: "))
ust_sinir = float(input("Üst sınırı girin: "))
# iterasyon sayısını al
iterasyon_sayisi = int(input("Iterasyon sayısını girin: "))

# Fonksiyonu çalıştır
kok, aralik = ikiyeBolme(alt_sinir, ust_sinir, max_iter=iterasyon_sayisi)


print(f"Bulunan kök: {kok}")
print(f"Bulunan kök aralığı: [{aralik[0]}, {aralik[1]}]")