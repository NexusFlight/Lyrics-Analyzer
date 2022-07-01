import httpData
import converter

lyrics = []
#x = httpData.getRecentSongs()
x = httpData.getSongsFromPlaylist()
y = converter.JsonToItem(x.text)

for x in y.items:
    lyrics.append({'trackID':x['track']['id'],'Artist':x['track']['artists'][0]['name'],'Track': x['track']['name'], 'lyrics':httpData.scrape_lyrics(x['track']['artists'][0]['name'],x['track']['name'])})


for x in lyrics:
    print(x)