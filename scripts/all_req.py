import requests
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_req(url, proxy):
    try:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=proxies)
        return response.status_code
    except Exception as e:
        return None


try:
    if len(sys.argv) != 2:
        print("Use: python main.py <proxy_host:port>")
        sys.exit(1)

    proxy = sys.argv[1]
    proxy = "http://" + proxy

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, 'hosts')
    print(file_name)
    with open(file_name, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    total_urls = len(urls)
    total_200 = 0
    total_not_200 = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(do_req, url, proxy): url for url in urls}
        for future in as_completed(futures):
            status = future.result()
            if status == 200:
                total_200 += 1
            else:
                total_not_200 += 1

    print(f"Total URLs: {total_urls}")
    print(f"Total 200: {total_200}")
    print(f"Total NOT 200: {total_not_200}")
except Exception as e:
    print(f"An error occurred: {e}")