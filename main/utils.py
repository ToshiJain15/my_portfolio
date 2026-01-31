
import requests
import logging

logger = logging.getLogger(__name__)

def get_hackerrank_data(username):
    """
    Fetches public profile data from HackerRank.
    Returns a dictionary with badges, certificates, and other stats.
    """
    base_url = "https://www.hackerrank.com/rest/hackers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    data = {
        'badges': [],
        'certificates': [],
        'profile_url': f"https://www.hackerrank.com/profile/{username}"
    }

    try:
        # 1. Fetch Badges (Stars)
        response = requests.get(f"{base_url}/{username}/badges", headers=headers, timeout=5)
        if response.status_code == 200:
            badges_data = response.json()
            # items usually contains the badges
            if 'models' in badges_data:
                for badge in badges_data['models']:
                    # Only keep badges with stars > 0 or specific ones
                    if badge.get('stars', 0) > 0:
                        data['badges'].append({
                            'name': badge.get('badge_name'),
                            'stars': badge.get('stars'),
                            'icon_url': badge.get('icon_url'), # Using small icon if available
                            'category': badge.get('badge_category'),
                        })
    except Exception as e:
        logger.error(f"Error fetching HackerRank badges: {e}")

    try:
        # 2. Fetch Submission Check (Activity) - Optional, maybe just stick to badges for now
        # There isn't a direct simple public API for all certs without parsing HTML sometimes, 
        # but let's check for 'certificates' endpoint or similar if it exists. 
        # Actually most reliable is badges first.
        pass
    except Exception as e:
        logger.error(f"Error fetching HackerRank other data: {e}")

    return data
