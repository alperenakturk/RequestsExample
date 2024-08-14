import requests
import json


# GET
# user_input = input("Enter id:")
# get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}" #Kaçıncı id istiyorsak buraya yazıyoruz.

# get_response = requests.get(get_url)
# print(get_response.json())

# POST
to_do_item = {"userId": 2, "title": "my to do", "completed": False}
# düz id eklemedik o otomatik oluşuyormuş sitedeki sözlük verileri arasında.

post_url = "https://jsonplaceholder.typicode.com/todos"

# Optional Header --> Genelde sunucuya Bilgi göndermek için kullanırız.
headers = {"Content-Type": "application/json"}

# Post Request örnek
# post_response = requests.post(post_url, json=to_do_item, headers=headers)
# print(post_response.json())

# Post Request örnek 2
post_response = requests.post(post_url, data=json.dumps(to_do_item), headers=headers)
print(post_response.json())
