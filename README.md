# Spotify Feature Learning
### File descriptions
- `\data` contains json song data
- `2_genre_classification_classical_and_rock.ipynb` classifies classical music and rock music based on energy and danceability
- `2_genre_classification_jazz_and_country` classifies classical music and rock music based on acousticness and loudness
- `Cross Entropy.ipynb` contains three attempts at cross entropy classification & ugly feature histograms - TO DELETE?
- `knn.ipynb` contains an attempt at KNeighbors classification
- `Linear Regression Attempt.ipynb` features scatter plots comparing each pair of features and shows relationships between: loudness and energy, acousticness and Loudness
- `song_feature_distributions.ipynb` features prettified feature histograms for all genres and by genre
- `spotify_genre_classifier.ipynb` contains first KNeighborsClassifier attempt - TO DELETE?
- `tinker.ipynb` takes json feature data from a playlist and converts to a pandas dataframe, draws feature histograms of said data
- `common.py` contains commonly used functions

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
- more to come here

### Directions for getting features from a playlist - without having a Spotify for Developers Account
- Spotify Web Console > Playlists > [Get a Playlist's Tracks](https://developer.spotify.com/console/get-playlist-tracks/)
- Share > Copy Spotify URI. From the URI grab the playlist ID (`spotify:user:username:playlist:playlist_id`)
- `user_id` and `playlist_id` > `items(track(album(name, href), href, id, name))` in `fields`.
- under `OAuth Token` click `TRY IT` 
- song data in  `songs.json`
- [Get Audio Features](https://beta.developer.spotify.com/console/get-audio-features-several-tracks/), navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids
- copy and paste feature data in `features.json`
