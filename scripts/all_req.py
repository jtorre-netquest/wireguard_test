import requests
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_req(url):
    try:
        response = requests.get(url, stream=True)
        return response.status_code
    except Exception as e:
        return None


try:
    file_name = "hosts.reduced"
    with open(file_name, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    total_urls = len(urls)
    total_200 = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(do_req, url, proxy): url for url in urls}
        for future in as_completed(futures):
            status = future.result()
            if status == 200:
                total_200 += 1

    print(f"Total URLs: {total_urls}")
    print(f"Total 200: {total_200}")
except Exception as e:
    print(f"An error occurred: {e}")