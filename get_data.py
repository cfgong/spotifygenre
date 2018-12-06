import spotipy

import pandas as pd
from pandas.io.json import json_normalize # for flattening json files

import credentials as creds #credentials file rip
from spotipy.oauth2 import SpotifyClientCredentials

# shhh secret stuff, credentials in crentials.py
# client_credentials_manager = SpotifyClientCredentials(client_id='Your_Client_ID', client_secret='Your_Client_Secret')
client_credentials_manager = SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET)

"""
Takes in a username, and playlist_id
Get all the playlists of a user.
Return a pandas df with the playlists's ids, names, and numbers of tracks. 
"""

def get_playlist_content(username, playlist_id, sp):
    content = sp.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=0, market=None)
    content = sp.user_playlists(username)
    content_df = json_normalize(content['items'])
    print(content)
    print(content_df)
    return content

"""
implement this
"""
def get_playlist_audio_features(username, playlist_id, sp):
    return None

"""
Takes in a username. 
Get all the playlists of a user.
Return a pandas df with the playlists's ids, names, and numbers of tracks. 
"""

def get_user_playlists(username, sp):
    playlists = sp.user_playlists(username)
    playlist_df = json_normalize(playlists['items'])
    
    features_to_remove = ['collaborative', 'external_urls.spotify', 'href', 'images', 'owner.display_name', 'owner.external_urls.spotify', 'owner.href', 'owner.id', 'owner.type', 'owner.uri', 'primary_color', 'public', 'snapshot_id', 'tracks.href', 'type', 'uri'] 
    playlist_df = playlist_df.drop(features_to_remove, axis = 1)
    attribute_names = playlist_df.columns.values.tolist()
    
    print("Feature attributes: ", attribute_names, "\n")
    print(playlist_df)
    
    return playlist_df

def main(username, *playlist):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print ("Getting user playlist")
    playlist_df = get_user_playlists(username, sp)
    
    playlist_id = playlist_df["id"][0]

    print ("Getting playlist content")
    content_df = get_playlist_content(username, playlist_id, sp)
    
    """
    print ("Getting playlist audio features")
    get_playlist_audio_features(username, playlist, sp)
    """
    return playlist_df, content_df

if __name__ == '__main__':
    playlist_df, content_df = main(creds.USERNAME)
