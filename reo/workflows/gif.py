import requests
import random

TENOR_API_KEY = "S1Oe592nbQvO5yJo4FZbbK9NZE0EvYCc"
TENOR_BASE_URL = "https://tenor.googleapis.com/v2/search"

FALLBACK_GIFS = {
    "slapping": "https://cdn.discordapp.com/attachments/1286969360224882688/1287446868623888497/bully-surprise.gif",
    "hugging": "https://media.tenor.com/kCZHCi1bxg4AAAAC/anime-hug.gif",
    "kissing": "https://media.tenor.com/F02Ep3U6bHAAAAAC/anime-kiss.gif",
    "patting": "https://media.tenor.com/S3cM2CvsR2kAAAAC/anime-pat.gif",
    "crying": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-cry.gif",
    "dancing": "https://media.tenor.com/7qNW48k9Z8oAAAAC/anime-dance.gif",
    "laughing": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-laugh.gif",
    "smiling": "https://media.tenor.com/3o7TKMt1Y1kAAAAC/anime-smile.gif",
    "angry": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-angry.gif",
    "confused": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-confused.gif",
    "sleeping": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-sleep.gif",
}

def get_gif(name: str, limit: int = 20):
    params = {"q": f"anime {name}", "key": TENOR_API_KEY, "limit": limit, "media_filter": "gif", "contentfilter": "low"}
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
    key = name.lower().strip()
    if key in FALLBACK_GIFS:
        return FALLBACK_GIFS[key]
    return random.choice(list(FALLBACK_GIFS.values()))
