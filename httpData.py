import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import re

def getRecentSongs(bearerToken):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {bearerToken}"
    return requests.get('https://api.spotify.com/v1/me/player/recently-played',headers=headers)

def GetSongFeatures(bearerToken,trackId):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {bearerToken}"
    return requests.get(f'https://api.spotify.com/v1/audio-features/{trackId}',headers=headers)

def getSongsFromPlaylist(bearerToken,playlistId,offset:int=0):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {bearerToken}"
    return requests.get(f"https://api.spotify.com/v1/playlists/{playlistId}/tracks?limit=100&offset={offset}",headers=headers)

def scrape_lyrics(artistname, songname):
    regex = r"[^0-9a-zA-Z\s]|\s\(.*?\)|\(.*?\)|\.|'|\s-.*|-.*"
    artistname = re.sub(regex,"",artistname)
    songname = re.sub(regex,"",songname)
    artistname2 = str(artistname.replace(' ','-')) if ' ' in artistname else str(artistname)
    songname2 = str(songname.replace(' ','-')) if ' ' in songname else str(songname)
    page = requests.get(f'https://genius.com/{artistname2}-{songname2}-lyrics')
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics1 = html.find("div", class_="lyrics")
    lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 YYrds")
    if lyrics1:
        lyrics = lyrics1.get_text()
    elif lyrics2:
        lyrics = lyrics2.get_text(separator=" ")
    elif lyrics1 == lyrics2 == None:
        lyrics = None
    return lyrics