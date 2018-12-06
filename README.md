[Get Playlist tracks](https://developer.spotify.com/console/get-playlist-tracks/)
- Spotify Web Console > Playlists > [Get a Playlist's Tracks](https://developer.spotify.com/console/get-playlist-tracks/)
- Share > Copy Spotify URI. Paste the URI anywhere and grab the playlist ID (`spotify:user:username:playlist:playlist_id`)
- `user_id` and `playlist_id` > `items(track(album(name, href), href, id, name))` in `fields`.
- under `OAuth Token` click `GET TOKEN` 
- song data in  `songs.json`
- [Get Audio Features](https://beta.developer.spotify.com/console/get-audio-features-several-tracks/), navigate to Tracks > Get Audio Features for Several Tracks and enter the song ids.
- copy and pasted feature data in `features.json`
