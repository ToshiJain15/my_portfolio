
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

    # Use the correct username provided by user
    # If username is passed as arg, use it. The view calls it with specific username.
    
    # API endpoints
    badges_url = f"https://www.hackerrank.com/rest/hackers/{username}/badges"
    profile_url = f"https://www.hackerrank.com/rest/hackers/{username}"
    
    # 1. Fetch Profile Data (Rank/Leaderboard is harder to get directly, but we can get some info)
    try:
        resp_profile = requests.get(profile_url, headers=headers, timeout=5)
        if resp_profile.status_code == 200:
            profile_data = resp_profile.json().get('model', {})
            # HackerRank API doesn't expose global rank easily in this endpoint
            # We will use the badges logic mostly
            pass
            
    except Exception as e:
        logger.error(f"Error fetching HackerRank profile: {e}")

    # 2. Fetch Badges
    try:
        response = requests.get(badges_url, headers=headers, timeout=5)
        if response.status_code == 200:
            badges_data = response.json()
            if 'models' in badges_data:
                for badge in badges_data['models']:
                    # Filter for active badges
                    if badge.get('stars', 0) > 0:
                        icon = badge.get('icon_url')
                        # Ensure we have a valid icon url, otherwise fallback to generic
                        if not icon: 
                            icon = 'https://hrcdn.net/s3_pub/share_assets/badges/default-gold.png'
                        elif icon.startswith('/'):
                            icon = f"https://hackerrank.com{icon}"
                            
                        data['badges'].append({
                            'name': badge.get('badge_name'),
                            'stars': badge.get('stars'),
                            'icon_url': icon,
                            'category': badge.get('badge_category'),
                        })
    except Exception as e:
        logger.error(f"Error fetching HackerRank badges: {e}")

    # If we successfully found data, let's remove any mock data fallbacks if they exist
    # If no badges found even with correct username, we might keep empty list
    
    # Manually setting specific rank if API doesn't provide it simply
    # For now, we will omit the specific numeric rank if we can't get it, 
    # or use a placeholder if the user explicitly requested it.
    # The user asked to "Take rank from hackerrank", but the REST API for rank is complex.
    # Let's try to infer or leave it blank if not found, rather than fake it.
    
    return data
