
import requests

candidates = [
    "https://hrcdn.net/community-frontend/assets/badges/problem-solving-gold.svg",
    "https://hrcdn.net/hackerrank/assets/badges/problem-solving-gold.svg",
    "https://s3.amazonaws.com/hr-assets/0/1570533036-7c39055375-problem-solving.png",
    "https://hrcdn.net/s3_pub/share_assets/badges/problem-solving-gold.png", # 404 confirmed
    "https://hrcdn.net/s3_pub/share_assets/badges/problem-solving-silver.png",
    "https://hrcdn.net/s3_pub/share_assets/badges/python-gold.png", # 404
]

for url in candidates:
    try:
        r = requests.head(url, timeout=3)
        print(f"{r.status_code} : {url}")
    except:
        print(f"Error : {url}")
