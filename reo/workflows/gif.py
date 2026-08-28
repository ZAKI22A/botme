import requests
import random

GIPHY_API_KEY = "S1Oe592nbQvO5yJo4FZbbK9NZE0EvYCc"
GIPHY_BASE = "https://api.giphy.com/v1/gifs/search"

FALLBACK_GIFS = [
    "https://cdn.discordapp.com/attachments/1286969360224882688/1287446868623888497/bully-surprise.gif",
]

def get_gif(name: str, limit: int = 20):
    try:
        params = {"api_key": GIPHY_API_KEY, "q": f"anime {name}", "limit": limit, "rating": "pg-13"}
        r = requests.get(GIPHY_BASE, params=params, timeout=8)
        if r.status_code == 200:
            data = r.json().get("data", [])
            if data:
                g = random.choice(data)
                url = g.get("images", {}).get("original", {}).get("url") or g.get("images", {}).get("downsized_large", {}).get("url")
                if url:
                    return url
    except: pass
    return random.choice(FALLBACK_GIFS)
