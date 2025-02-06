from enum import verify

import requests
import os

proxy = "http://54.196.240.167:2501"
url = "https://example.com/"
# url = "https://www.pippo.com"
path_cert = os.path.abspath("./certCA.pem")


print(path_cert)

def get_ssl_info(url, proxy=None):
    try:
        if proxy:
            proxies = {
                "http": proxy,
                "https": proxy
            }
            response = requests.get(url, proxies=proxies, stream=True, verify=path_cert)
        else:
            response = requests.get(url, stream=True)

        print(response.status_code)
        cert = response.raw.connection.sock.getpeercert()
        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject_alt_names = cert.get("subjectAltName", [])

        print("Issuer:", issuer)
        print("Subject Alternative Names:", subject_alt_names)
    except Exception as e:
        print(f"Error: {e}")


print("--------- CON PROXY ----------")
get_ssl_info(url, proxy)

print("\n--------- SIN PROXY ----------")
get_ssl_info(url)
