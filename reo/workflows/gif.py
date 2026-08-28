import requests
import random

TENOR_API_KEY = "S1Oe592nbQvO5yJo4FZbbK9NZE0EvYCc"
TENOR_BASE_URL = "https://tenor.googleapis.com/v2/search"

# working discord CDN gifs - guaranteed to load inside embed
FALLBACK_GIFS = [
    "https://cdn.discordapp.com/attachments/1286969360224882688/1287446868623888497/bully-surprise.gif",
    "https://media.tenor.com/2UYENRica1gAAAAC/cute-anime.gif",
]

def get_gif(name: str, limit: int = 20):
    q = f"anime {name}"
    params = {"q": q, "key": TENOR_API_KEY, "limit": limit, "media_filter": "gif", "contentfilter": "low"}
    try:
        response = requests.get(TENOR_BASE_URL, params=params, timeout=8)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                selected = random.choice(results)
                url = selected.get("media_formats", {}).get("gif", {}).get("url") or selected.get("media_formats", {}).get("tinygif", {}).get("url")
                if url:
                    return url
    except Exception:
        pass
    # API key invalid -> use fallback so GIF always appears inside embed
    return random.choice(FALLBACK_GIFS)
