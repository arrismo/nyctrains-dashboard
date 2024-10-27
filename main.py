

import requests
import json
import datetime
from contextlib import redirect_stdout
from google.transit import gtfs_realtime_pb2
from protobuf3_to_dict import protobuf_to_dict

# Get MTA ACE Train Data
# MTA train data is returen in a Protocol Buffer format (GTFS format)
response = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace")
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)
feed_dict = protobuf_to_dict(feed)

print(feed_dict)

dump_object = json.dumps(feed_dict, indent=4)
# Save out data to json file -- temporary 
with open('a-train-data.json','w') as f:
   with redirect_stdout(f):
      print(dump_object)
      
      
        
arrival_time = feed_dict['entity'][0]['trip_update']['stop_time_update'][0]['arrival']['time']
departure_time = feed_dict['entity'][0]['trip_update']['stop_time_update'][0]['departure']['time']
print(datetime.datetime.fromtimestamp(departure_time))