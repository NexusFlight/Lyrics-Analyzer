import json
from Song import SongAllDetails, TrackDetails

def JsonToItem(data):
    try:
        return SongAllDetails(**json.loads(data))
    except:
        print(f"you might need to replace your token error: {data}")
        exit()

def trackDetailsJsonToItem(data):
    return TrackDetails(**json.loads(data))
   