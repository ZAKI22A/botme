import requests
import random

TENOR_API_KEY = "S1Oe592nbQvO5yJo4FZbbK9NZE0EvYCc"
TENOR_BASE_URL = "https://tenor.googleapis.com/v2/search"

def get_gif(name: str, limit: int = 20):
    params = {
        "q": f"anime {name}",
        "key": TENOR_API_KEY,
        "limit": limit,
        "media_filter": "gif",
        "contentfilter": "medium"
    }
    try:
        response = requests.get(TENOR_BASE_URL, params=params, timeout=10)
        if response.status_code != 200:
            return None

        data = response.json()
        results = data.get("results", [])

        if not results:
            return None

        selected = random.choice(results)
        media_formats = selected.get("media_formats", {})
        gif_url = media_formats.get("gif", {}).get("url")
        return gif_url
    except Exception:
        return None
