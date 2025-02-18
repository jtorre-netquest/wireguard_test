import requests
import os
import sys

def get_ssl_info(url):
    try:
        response = requests.get(url, stream=True)

        print(response.status_code)
        cert = response.raw.connection.sock.getpeercert()
        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject_alt_names = cert.get("subjectAltName", [])

        print("Issuer:", issuer)
        print("Subject Alternative Names:", subject_alt_names)
    except Exception as e:
        print(f"Error: {e}")


# url = "https://example.com/"
url = "https://4411.flitsmeister.app/nl/zones"

print("---------- PROXY ----------")
get_ssl_info(url)