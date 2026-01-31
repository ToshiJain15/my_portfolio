
import requests

url = "https://hrcdn.net/s3_pub/share_assets/badges/cpp-gold.png"
print(f"Checking {url}...")
try:
    resp = requests.head(url, timeout=5)
    print(f"Status: {resp.status_code}")
except Exception as e:
    print(f"Error: {e}")
