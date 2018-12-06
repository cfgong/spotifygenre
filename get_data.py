import json
import spotipy
import pandas as pd

from pandas.io.json import json_normalize # for flattening json files

import credentials as creds #credentials file rip
from spotipy.oauth2 import SpotifyClientCredentials

# shhh secret stuff, credentials in crentials.py
# client_credentials_manager = SpotifyClientCredentials(client_id='Your_Client_ID', client_secret='Your_Client_Secret')
client_credentials_manager = SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET)




def get_user_playlists(username, sp):
    playlists = sp.user_playlists(username)
    playlist_df = json_normalize(playlists['items'])
    
    # Print original attributes before removing unncessary ones
    """
    attribute_names = playlist_df.columns.values.tolist()
    print("Original attributes: ", attribute_names, "\n")
    """
    
    features_to_remove = ['collaborative', 'external_urls.spotify', 'href', 'images', 'owner.display_name', 'owner.external_urls.spotify', 'owner.href', 'owner.id', 'owner.type', 'owner.uri', 'primary_color', 'public', 'snapshot_id', 'tracks.href', 'type', 'uri'] 
    # print("Features to remove: ", features_to_remove, "\n")
    playlist_df = playlist_df.drop(features_to_remove, axis = 1)
    attribute_names = playlist_df.columns.values.tolist()
    print("Feature attributes: ", attribute_names, "\n")
    print(playlist_df)
    return playlist_df

def main(username, *playlist):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print ("Getting user playlist")
    playlist_df = get_user_playlists(username, sp)
    """
    print ("Getting playlist content")
    get_playlist_content(username, playlist, sp)
    print ("Getting playlist audio features")
    get_playlist_audio_features(username, playlist, sp)
    """
    return playlist_df

if __name__ == '__main__':
    playlist_df = main(creds.USERNAME)
