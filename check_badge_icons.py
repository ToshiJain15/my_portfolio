
import requests

username = 'jaintoshi15'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url = f"https://www.hackerrank.com/rest/hackers/{username}/badges"
try:
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if 'models' in data:
        for badge in data['models']:
            print(f"Badge: {badge.get('badge_name')}")
            print(f"Icon: {badge.get('icon_url')}")
            print(f"Small Icon: {badge.get('icon_small_url')}")
            print(f"Medium Icon: {badge.get('icon_medium_url')}")
            print("-" * 20)
except Exception as e:
    print(e)
