# Spotify Feature Learning
### File Descriptions
- `\data` contains json song data
- `2_genre_classification_classical_and_rock.ipynb` classifies classical music and rock music based on energy and danceability
- `2_genre_classification_jazz_and_country` classifies classical music and rock music based on acousticness and loudness
- `Cross Entropy.ipynb` contains three attempts at cross entropy classification & ugly feature histograms - TO DELETE?
- `knn.ipynb` contains an attempt at KNeighbors classification
- `Linear Regression Attempt.ipynb` features scatter plots comparing each pair of features and shows relationships between: loudness and energy, acousticness and Loudness
- `song_feature_distributions.ipynb` features prettified feature histograms for all genres and by genre
- `spotify_genre_classifier.ipynb` contains first KNeighborsClassifier attempt - TO DELETE?
- `common.py` contains commonly used functions

### Directions for Getting Features from a playlist
- Spotify Web Console > Playlists > [Get a Playlist's Tracks](https://developer.spotify.com/console/get-playlist-tracks/)
- Share > Copy Spotify URI. From the URI grab the playlist ID (`spotify:user:username:playlist:playlist_id`)
- `user_id` and `playlist_id` > `items(track(album(name, href), href, id, name))` in `fields`.
- under `OAuth Token` click `TRY IT` 
- song data in  `songs.json`
- [Get Audio Features](https://beta.developer.spotify.com/console/get-audio-features-several-tracks/), navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids.
- copy and pasted feature data in `features.json`
