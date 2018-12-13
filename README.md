# Spotify Feature Learning
### Data
- [training dataset](https://raw.githubusercontent.com/sql-injection/spotify_data/master/train.csv)
- [testing dataset](https://raw.githubusercontent.com/sql-injection/spotify_data/master/test.csv)
- [complete dataset](https://raw.githubusercontent.com/sql-injection/spotify_data/master/spotify.csv)

### File descriptions
- `\archive` contains:
    - `Cross Entropy.ipynb` contains three attempts at cross entropy classification & ugly feature histograms
    - `spotify_genre_classifier.ipynb` contains first KNeighborsClassifier attempt
- `2_genre_classification_classical_and_rock.ipynb` classifies classical music and rock music based on energy and danceability
- `2_genre_classification_jazz_and_country` classifies classical music and rock music based on acousticness and loudness
- `knn.ipynb` contains an attempt at KNeighbors classification
- `Linear Regression Attempt.ipynb` features scatter plots comparing each pair of features and shows relationships between: loudness and energy, acousticness and Loudness
- `common.py` contains commonly used functions
- `knn.ipynb` contains a knn attempt
- `song_feature_distributions.ipynb` features prettified feature histograms for all genres and by genre

Refer [here](https://github.com/cfgong/spotifytinker) for details on how to retrieve Spotify feature data from other playlists.