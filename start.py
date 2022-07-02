from DbOps import insertRecord
import httpData
import converter

def getData():
    bearerToken = ''
    playlistId = ''
    playlistLength = 170
    playlistClassification = ''
    #x = httpData.getRecentSongs(bearerToken)
    offet = 0
    while(offet < playlistLength):
        x = httpData.getSongsFromPlaylist(bearerToken,playlistId,offet)
        offet += 100
        y = converter.JsonToItem(x.text)
        i = 1
        for x in y.items:
            print(f"working on {x['track']['name']} by {x['track']['artists'][0]['name']}  {i+offet}  {offet}")
            i += 1
            trackId = x['track']['id']
            artistName = x['track']['artists'][0]['name']
            trackName = x['track']['name']
            lyricsData = httpData.scrape_lyrics(artistName,trackName)
            if(lyricsData == None):
                print(f"failed to get lyrics for {trackName} by {artistName}")
                continue
            
            trackFeatures = converter.trackDetailsJsonToItem(httpData.GetSongFeatures(bearerToken,trackId).text).getAsDict()
            item = {'classification':playlistClassification,'_id':trackId,'Artist':artistName,'Track': trackName, 'lyrics':lyricsData, 'features': trackFeatures}
            try:
                insertRecord(item)
            except:
                print(f"failed to insert {trackName} by {artistName}")
                continue

getData()