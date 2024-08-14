import threading
import requests
import time
import asyncio
import aiohttp


# Verileri tek tek çekme

def get_data_sync(urls):
    start_time = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution Time", elapsed_time, "seconds")
    return json_array


# THREADING ile çoklu data çekme

class ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array


def get_data_threading(urls):
    start_time = time.time()

    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution Time", elapsed_time, "seconds")


# Asyncio ile veri çekme --> İlk yönteme benzer bir şekilde çektiğimiz için bu örnekte verimsiz olacak.
async def get_data_async_but_as_wrapper(urls):
    start_time = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                json_array.append(await resp.json())  # async bir işlemin cevabını await ile alıyorum

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution Time", elapsed_time, "seconds")
    return json_array


async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    start_time = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)  # Tüm taskın içindeki elemanları tek tek içine koyar.

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution Time", elapsed_time, "seconds")
    return json_array


my_url = ["https://postman-echo.com/delay/3"] * 10
# get_data_sync(urls) # Execution Time 37.25164985656738 seconds
# get_data_threading(my_url)  # Execution Time 3.9973878860473633 seconds
# asyncio.run(get_data_async_but_as_wrapper(my_url))  # 36.83913588523865 seconds # asyncio'yu böyle çağırmalıyız.
asyncio.run(get_data_async_concurrently(my_url))  # Execution Time 3.7834692001342773 seconds
