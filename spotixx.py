import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
import pandas as pd
from json.decoder import JSONDecodeError

scope = 'user-library-read'
#get the  user name from the terminal
username = sys.argv[1]

#erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-(username)")
    token = util.prompt_for_user_token(username)


#create spotify object
spotifyObject = spotipy.Spotify(auth=token)


offset=0
items=[]
songs=[]
ids = []
pl_id = '3qmsB1xMGKSMxoNhlq2R5X'
while True:
    user_pl = spotifyObject.user_playlist_tracks(username, playlist_id = pl_id,fields=None,limit=100,offset=offset,market=None)
    songs += user_pl['items']
    if user_pl['next'] is not None:
        offset += 100
    else:
        break
with open('{}-{}'.format(username, pl_id), 'w') as outfile:
        json.dump(songs, outfile)

for i in songs:
    ids.append(i['track']['id'])
index=0
audio_features=[]
while index < len(ids):
        audio_features += spotifyObject.audio_features(ids[index:index + 50])
        index += 50

features_list=[]
for features in audio_features:
        features_list.append([features['energy'], features['liveness'],
                              features['tempo'], features['speechiness'],
                              features['acousticness'], features['instrumentalness'],
                              features['time_signature'], features['danceability'],
                              features['key'], features['duration_ms'],
                              features['loudness'], features['valence'],
                              features['mode'], features['type'],
                              features['uri']])

df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                              'tempo', 'speechiness',
                                              'acousticness', 'instrumentalness',
                                              'time_signature', 'danceability',
                                              'key', 'duration_ms', 'loudness',
                                              'valence', 'mode', 'type', 'uri'])
   
df.to_csv('{}-{}.csv'.format(username, pl_id), index=False)