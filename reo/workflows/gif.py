import requests
import random

TENOR_API_KEY = "kVejrDZRfCoSpTBDgv1LMr7VpM2zVqCS"
TENOR_BASE_URL = "https://tenor.googleapis.com/v2/search"

FALLBACK_GIFS = {
    "slapping": "https://media.tenor.com/2UYENRica1gAAAAC/anime-slap.gif",
    "hugging": "https://media.tenor.com/kCZHCi1bxg4AAAAC/anime-hug.gif",
    "kissing": "https://media.tenor.com/F02Ep3U6bHAAAAAC/anime-kiss.gif",
    "patting": "https://media.tenor.com/S3cM2CvsR2kAAAAC/anime-pat.gif",
    "crying": "https://media.tenor.com/8Uq-5pC3v2EAAAAC/anime-cry.gif",
    "dancing": "https://media.tenor.com/7qNW48k9Z8oAAAAC/anime-dance.gif",
    "laughing": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-laugh.gif",
    "smiling": "https://media.tenor.com/3o7TKMt1Y1kAAAAC/anime-smile.gif",
    "angry": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-angry.gif",
    "confused": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-confused.gif",
    "sleeping": "https://media.tenor.com/1nVq0o5rF1EAAAAC/anime-sleep.gif",
}

def get_gif(name: str, limit: int = 20):
    params = {"q": f"anime {name}", "key": TENOR_API_KEY, "limit": limit, "media_filter": "gif", "contentfilter": "medium"}
    try:
        response = requests.get(TENOR_BASE_URL, params=params, timeout=8)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                selected = random.choice(results)
                url = selected.get("media_formats", {}).get("gif", {}).get("url")
                if url:
                    return url
    except Exception:
        pass
    # fallback - random choice still variable
    key = name.lower().strip()
    if key in FALLBACK_GIFS:
        return FALLBACK_GIFS[key]
    # generic fallback anime gif
    return random.choice(list(FALLBACK_GIFS.values()))
