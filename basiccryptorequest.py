import requests


def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:  # işlem başarılı ise demek. bunu http status code lardan biliyoruz
        # for crypto in response.json(): #Json formatı üzerinden döngüyü başlattık daha rahat okumak için
        # print(crypto["price"])
        return response.json()


crypto_response = get_crypto_data()
user_input = input("Enter your crypto currency: ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break
