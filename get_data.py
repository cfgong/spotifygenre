import spotipy
import pandas as pd
from pandas.io.json import json_normalize # for flattening json files

import credentials as creds #credentials file rip
from spotipy.oauth2 import SpotifyClientCredentials

# shhh secret stuff, credentials in crentials.py
# client_credentials_manager = SpotifyClientCredentials(client_id='Your_Client_ID', client_secret='Your_Client_Secret')

"""
get list of labels of a df
"""
def get_df_labels(df):
    return df.columns.values.tolist()


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
    
    # print new attribute names
    """
    attribute_names = get_df_labels(playlist_df)
    print("Feature attributes: ", attribute_names, "\n")
    """
    return playlist_df

"""
takes in a playlist json and then prints the playlist name, total tracks, and track info
"""
def print_playlist_tracks(username, playlist, sp, filename = None):
    playlistName = playlist['name']
    trackCount = playlist['tracks']['total']
    playlistID = playlist['id']
    
    if filename is not None:
        with open(filename, "a", encoding="utf-8") as text_file:
            print(f'PLAYLIST: {playlistName}', file = text_file)
            print(f'TOTAL TRACKS: {trackCount}', file = text_file)
    else:
        # print(f'PLAYLIST: {playlistID} : {playlistName}')
        print(f'PLAYLIST: {playlistName}')
        print(f'TOTAL TRACKS: {trackCount}')

    results = sp.user_playlist(username, playlistID, fields="tracks,next")
    tracks = results['tracks']
    # print(tracks)
    print_tracks(tracks, filename)
    while tracks['next']:
        tracks = sp.next(tracks)
        print_tracks(tracks, filename)

"""
take in tracks json and prints tracks
"""
def print_tracks(tracks, filename):
    for i, item in enumerate(tracks['items']):
        # i is the track index, item gives us the track info
        track = item['track']
        
        artistName = track['artists'][0]['name']
        trackName = track['name']
        trackID = track['id']
        # print artist name and item 
        if filename is not None:
            with open(filename, "a", encoding="utf-8") as text_file:
                print(f"- {artistName} - {trackName}", file = text_file)
        else:
            # print(f"- {trackID} : {artistName} - {trackName}")
            print(f"- {artistName} - {trackName}")
"""
print all tracks of a user
"""
def print_all_user_tracks(username, sp, filename = None):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print_playlist_tracks(username, playlist, sp, filename)
"""
gets all the tracks in the public playlists of a user, returns a df
"""
def get_all_playlist_content(username, sp):
    columns = ['playlist.id', 'playlist.name', 'id', 'artist', 'title']
    tracks_df = pd.DataFrame(columns= columns) #dataframe to hold the track data
    
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        playlistName = playlist['name']
        playlistID = playlist['id']
        tracks_df = get_playlist_content(playlistName, playlistID, tracks_df, columns, sp)
        
    return tracks_df

"""
get content of just one playlist
pass in playlist id
"""
def get_playlist_content(playlistName, playlistID, tracks_df, columns, sp):
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

def get_playlist_content_from_id(playlistID, sp, playlistName = ""):
    columns = ['playlist.id', 'playlist.name', 'id', 'artist', 'title']
    tracks_df = pd.DataFrame(columns= columns) #dataframe to hold the track data
    
    return get_playlist_content(playlistName, playlistID, tracks_df, columns, sp)

"""
gets dataframe of tracks, and returns a df of track features
"""
def get_all_track_features(tracks_df, sp):
    features = sp.audio_features(tracks_df["id"])
    return get_features_df_from_json(features)
"""
gets track id, and returns a df of track features
"""
def get_track_features(track_id, sp):
    features = sp.audio_features(track_id)
    return get_features_df_from_json(features)
"""
gets a features json, and returns a df of track features
"""
def get_features_df_from_json(features):
    features_df = pd.DataFrame(features)

    features_to_remove = ['analysis_url', 'duration_ms', 'id', 'key', 'mode', 'time_signature', 'track_href', 'type', 'uri']
    # print("Features to remove: ", features_to_remove, "\n")
    features_df = features_df.drop(features_to_remove, axis = 1)
    # print new attribute names
    """
    attribute_names = get_df_labels(playlist_df)
    print("Feature attributes: ", attribute_names, "\n")
    """
    return features_df
"""
get playlist_df, tracks_df, features_df using usercredentials
"""
def main(username, client_ID, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # playlist_df = get_user_playlists(username, sp)
    # print ("User's playlists details: playlist_df")
    tracks_df = get_all_playlist_content(username, sp)
    # print("All tracks from user's playlists: tracks_df")
    features_df = get_all_track_features(tracks_df, sp)
    # print("All audio features of tracks in the user's playlists: features_df")
    return tracks_df, features_df

"""
print all user tracks
you can pass an optional argument with filename
"""
def main2(username, client_ID, client_secret, print_to_file = False):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    filename = None
    
    if print_to_file:
        user_details = sp.user(username)
        display_name = user_details["display_name"]
        
        filename = ""
        
        if display_name is None:
            filename = username + "_output.txt"
        else:
            filename = display_name.replace(' ', '') + "_output.txt"
        open(filename, 'w').close()
        
    print_all_user_tracks(username, sp, filename)
    
"""
testing ground function
"""    
def test():
    client_credentials_manager = SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    username = creds.USERNAME
    
    

if __name__ == '__main__':
    username = creds.USERNAME
    # get dataframe of user track data and user feature data
    tracks_df, features_df = main(username, creds.CLIENT_ID, creds.CLIENT_SECRET)
    
    # write user song tracks list to a file
    """
    main2(username, creds.CLIENT_ID, creds.CLIENT_SECRET, print_to_file = True)
    """

    
