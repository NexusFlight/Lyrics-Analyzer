import json
from Song import Welcome2

def JsonToItem(data):
    return Welcome2(**json.loads(data))
   