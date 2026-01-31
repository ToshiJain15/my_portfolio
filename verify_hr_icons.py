
import logging
from main.utils import get_hackerrank_data

# Set up basic logging to see errors if any
logging.basicConfig(level=logging.INFO)

print("Fetching data for jaintoshi15...")
data = get_hackerrank_data('jaintoshi15')

print("\n--- BADGES ---")
for badge in data['badges']:
    print(f"Name: {badge['name']}")
    print(f"Stars: {badge['stars']}")
    print(f"Icon URL: {badge['icon_url']}")
    print("-" * 30)
