import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup


def getRecentSongs():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {input('Enter spotify bearer token without Bearer:')}"
    return requests.get('https://api.spotify.com/v1/me/player/recently-played',headers=headers)

def getSongsFromPlaylist():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {input('Enter spotify bearer token without Bearer:')}"
    return requests.get(f"https://api.spotify.com/v1/playlists/{input('please enter the playlist Id')}/tracks",headers=headers)

def scrape_lyrics(artistname, songname):
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