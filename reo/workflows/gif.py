import requests
import random

TENOR_API_KEY = "S1Oe592nbQvO5yJo4FZbbK9NZE0EvYCc"
TENOR_BASE_URL = "https://tenor.googleapis.com/v2/search"

FALLBACK_GIFS = [
    "https://media.tenor.com/2UYENRica1gAAAAC/anime-fight.gif",
    "https://media.tenor.com/BYpX4K1w1XAAAAAC/anime-fighting.gif",
    "https://cdn.discordapp.com/attachments/1286969360224882688/1287446868623888497/bully-surprise.gif",
]

def get_gif(name: str, limit: int = 20):
    # fighting anime variable characters
    q = f"anime fighting {name}"
    params = {"q": q, "key": TENOR_API_KEY, "limit": limit, "media_filter": "gif", "contentfilter": "low", "random": "true"}
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
    return random.choice(FALLBACK_GIFS)
