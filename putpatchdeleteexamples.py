import requests

get_url = "https://jsonplaceholder.typicode.com/todos/15"  # Kaçıncı id istiyorsak yazıyoruz.

# get_response = requests.get(get_url)
# print(get_response.json())

# PUT --> Tüm parametreleri değiştirebiliriz. Endüstride genelde put kullanılır.
to_do_item_15 = {"userId": 2, "title": "put title", "completed": False}
# put_response = requests.put(get_url, json=to_do_item_15)
# print(put_response.json())

# PATCH --> Tek bir parametreyi değiştirmek için kullanılır. Endüstride pek kullanılmaz
to_do_item_patch_15 = {"title": "Patch Test:"}
# patch_response = requests.patch(get_url, json=to_do_item_patch_15)
# print(patch_response.json())

# DELETE --> Silmek için kullanılır.
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)
