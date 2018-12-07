# Spotify Feature Learning
### File descriptions
- `\archive` contains:
    - `Cross Entropy.ipynb` contains three attempts at cross entropy classification & ugly feature histograms
    - `spotify_genre_classifier.ipynb` contains first KNeighborsClassifier attempt
- `\data` contains json song data
- `2_genre_classification_classical_and_rock.ipynb` classifies classical music and rock music based on energy and danceability
- `2_genre_classification_jazz_and_country` classifies classical music and rock music based on acousticness and loudness
- `knn.ipynb` contains an attempt at KNeighbors classification
- `Linear Regression Attempt.ipynb` features scatter plots comparing each pair of features and shows relationships between: loudness and energy, acousticness and Loudness
- `common.py` contains commonly used functions
- `get_data.py` allows for easy attraction of playlist data using Spotify for developers account (see below for more details)
- `knn.ipynb` contains a knn attempt
- `song_feature_distributions.ipynb` features prettified feature histograms for all genres and by genre
- `tinker.ipynb` takes json feature data from a playlist and converts to a pandas dataframe, draws feature histograms of said data


### Directions for getting song features - using Spotify for Developers Account
- you need a spotify CLIENT_ID & CLIENT_SECRET for this
- make a `credentials.py` file and input details, sample format below, you really just need the CLIENT_ID and CLIENT_SECRET
- also input a username for the user you want to analyze
```
PORT_NUMBER = 8080
CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET_HERE'
REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

USERNAME = "YOUR_USERNAME_HERE"
```
- Create a [Spotify for Developers account](https://developer.spotify.com/)
- Create an app to get CLIENT_ID & CLIENT_SECRET (this we saved in the `credentials.py` file)
- to get USERNAME go to Spotify Web Console and go to a user, click on the three dots button > Share > Copy Spotify URI 
- run `get_data.py` to get user data into dataframes
- `main(username, client_ID, client_secret)` returns two dataframes: one df with tracks data, one df with features of said tracks data
- `main2(username, client_ID, client_secret, print_to_file = False):` returns a text file or prints out all the tracks in the public playlists of a user in a semi-nicely formatted manner
- `get_playlist_content_from_id(playlistID, sp, playlistName = "")` just get the playlist track content from one playlist
- `get_all_playlist_content(username, sp)` gets all the tracks in the public playlists of a user, returns a df
- `get_user_playlists(username, sp)` gets all playlists of a user, returns a df
- `get_all_track_features(tracks_df, sp)` gets all track features of a dataframe of tracks, returns a track_df
- `get_track_features(trackID, sp)` gets audio features for a single track, returns a features_df


### Directions for getting features from a playlist - without having a Spotify for Developers Account
- refer to `tinker.ipynb`
- Spotify Web Console > Playlists > [Get a Playlist's Tracks](https://developer.spotify.com/console/get-playlist-tracks/)
- Share > Copy Spotify URI. From the URI grab the playlist ID (`spotify:user:username:playlist:playlist_id`)
- `user_id` and `playlist_id` > `items(track(album(name, href), href, id, name))` in `fields`.
- under `OAuth Token` click `TRY IT` 
- song data in  `songs.json`
- [Get Audio Features](https://beta.developer.spotify.com/console/get-audio-features-several-tracks/), navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids
- copy and paste feature data in `features.json`


### References:
- [Spotipy Docs](https://spotipy.readthedocs.io/en/latest/)
- [github code reference](https://github.com/juandes/spotify-audio-features-data-experiment/blob/master/get_data.py) for [spotipy](https://spotipy.readthedocs.io/en/latest/) usage in `get_data.py`

### To do:
- Code cleanup:
    - add a package requirements file