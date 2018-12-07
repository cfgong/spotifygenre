import spotipy
import json 
import pandas as pd
from pandas.io.json import json_normalize # for flattening json files

import credentials as creds #credentials file rip
from spotipy.oauth2 import SpotifyClientCredentials

# shhh secret stuff, credentials in crentials.py
# client_credentials_manager = SpotifyClientCredentials(client_id='Your_Client_ID', client_secret='Your_Client_Secret')
client_credentials_manager = SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET)

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
    
    # print attribute names
    """
    attribute_names = playlist_df.columns.values.tolist()
    print("Feature attributes: ", attribute_names, "\n")
    """
    return playlist_df

"""
takes in a playlist json and then prints the playlist name, total tracks, and track info
"""
def print_playlist_tracks(username, playlist):
    # print('%s: PLAYLIST: %s' % (playlist['id'], playlist['name']))
    print('PLAYLIST: %s' % (playlist['name']))
    print('TOTAL TRACKS: %d' % (playlist['tracks']['total']))
    
    results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
    tracks = results['tracks']
    # print(tracks)
    print_tracks(tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        print_tracks(tracks)

"""
take in tracks json and prints tracks
"""
def print_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        # i is the track index, item gives us the track info
        track = item['track']
        # print artist name and item 
        # print("- %s: %s - %s" % (track['id'], track['artists'][0]['name'], track['name']))
        print("- %s - %s" % (track['artists'][0]['name'], track['name']))
"""
print all tracks of a user
"""
def print_all_user_tracks(username, sp):
    playlists = sp.user_playlists(creds.USERNAME)
    for playlist in playlists['items']:
        print_playlist_tracks(creds.USERNAME, playlist)
"""
gets all playlists of a user, gets all the tracks, and returns a df of all tracks
"""
def get_playlist_content(username, sp):
    columns = ['playlist.id', 'playlist.name', 'id', 'artist', 'title']
    tracks_df = pd.DataFrame(columns= columns) #dataframe to hold the track data
    
    playlists = sp.user_playlists(creds.USERNAME)
    for playlist in playlists['items']:
        playlistName = playlist['name']
        playlistID = playlist['id']
        
        results = sp.user_playlist(username, playlistID, fields="tracks,next")
        tracks = results['tracks']
        
        """
        appends track data of each track into the tracks_df dataframe
        """
        def input_track_data(tracks, tracks_df):
            for i, item in enumerate(tracks['items']):
                track = item['track']
                
                artistName = track['artists'][0]['name']
                trackName = track['name']
                trackID = track['id']
                
                df = pd.DataFrame([[playlistID, playlistName, trackID, artistName, trackName]], columns = columns)
                tracks_df = tracks_df.append(df, ignore_index = True)
            return tracks_df
        
        tracks_df = input_track_data(tracks, tracks_df)
        
        while tracks['next']:
            tracks = sp.next(tracks)
            tracks_df = input_track_data(tracks, tracks_df)
    return tracks_df

"""
implement this
"""
def get_playlist_features(username, sp):
    return None
   
if __name__ == '__main__':
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print ("Getting user's playlists details")
    playlist_df = get_user_playlists(creds.USERNAME, sp)
    
    print("Getting all tracks from user's playlists")
    tracks_df = get_playlist_content(creds.USERNAME, sp)
    # print_all_user_tracks(creds.USERNAME, sp)
    print("Getting features from all tracks in the user's playlists")
    features_df = get_playlist_features(creds.USERNAME, sp)
    
