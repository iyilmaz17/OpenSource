import requests


def get_random_dog_image(breed):
    # Api bağlantı Url
    # Bread köpek cinsini ifade ediyor ve kullanıcıdan alınıyor
    api_url = f"https://dog.ceo/api/breed/{breed}/images/random"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        # Apiden iki değer dönüyor message,status
        #  status = suceces ise doğru resim linki ekrana yazdırılır
        if data['status'] == 'success':
            image_url = data['message']
            return image_url
        # Başarısızsa hata mesajı ekrana yazdırlır
        else:
            print(f"Hata: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ağ hatası: {e}")
        return None


def main():
    breed = input("Lütfen bir köpek cinsi girin: ").lower()
    image_url = get_random_dog_image(breed)

    if image_url:
        print(f"\nİşte {breed} cinsine ait rastgele bir köpek resmi:")
        print(image_url)
    else:
        print("Köpek resmi alınamadı.")


if __name__ == "__main__":
    main()
