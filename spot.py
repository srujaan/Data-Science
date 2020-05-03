import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util

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

user = spotifyObject.current_user()
#print(json.dumps(user, sort_keys=True, indent=4))

#current_user_recently_played
searchQuery = spotifyObject.search(q='Taylor Swift', type='artist')

#print(json.dumps(searchQuery, sort_keys=True, indent=4))
#recenly_played = spotifyObject.current_user_recently_played(limit=50,after=None,before=None)
#saved_tracks = spotifyObject.current_user_saved_tracks(limit=50,offset=0)
#print()
#print("SONG'S NAME" + ' - ' + "SONG'S POPULARITY")
#print('*' * 25)
#for item in saved_tracks['items']:
#    track = item['track']
#    print(track['name']  + ' - ' +  str(track['popularity']))
#
#print(json.dumps(saved_tracks, sort_keys=True, indent=4))

#songs += user_pl['items']['name']
#if user_pl['next'] is not None:
#    offset += 100
#with open('{}-{}'.format(user,user_pl),'w') as outfile:
#    json.duoffset += 100mp(songs,outfile)
#print(json.dumps(user_pl, sort_keys=True, indent=4))

offset=0
songs=[]
ids = []
pl_id = '3qmsB1xMGKSMxoNhlq2R5X'
while True:
    user_pl = spotifyObject.user_playlist_tracks(user, playlist_id = pl_id,fields=None,limit=100,offset=offset,market=None)
    songs += user_pl['items']
    if user_pl['next'] is not None:
        offset += 100
    else:
        break
with open('{}-{}'.format(username, pl_id), 'w') as outfile:
        json.dump(songs, outfile)

for i in songs:
    ids.append(i['track']['name'])
    print(ids)

#with open('{}-{}'.format(user, pl_id), 'w') as outfile:
#        json.dump(songs, outfile)
#print(json.dumps(songs, sort_keys=True, indent=4))