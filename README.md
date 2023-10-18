# PyByeSpotify

### Bulk Export your public Spotify playlists to ~~CSV files~~ the terminal and Youtube Music. 

It's free. Don't complain. 

You need to create a Spotify Developer account to get access to your Client ID and Client Secret from the Web API.

* [Go here](https://developer.spotify.com/dashboard/) to start your developer account creation. 
* [Go to your App Dashboard](https://developer.spotify.com/dashboard/applications) and _**CREATE AN APP**_
* Click on your newly created application to find your Client ID and your Client Secret which is hidden from view, initially. 

#### Required Environment Variables

[Spotify API](https://developer.spotify.com/documentation/web-api/)

* CLIENT_ID
* CLIENT_SECRET


#### Generate an oauth.json file for Youtube Music

Follow the instructions for [ytmusicapi](https://ytmusicapi.readthedocs.io/en/stable/index.html) to setup your oauth.json file.
You can find that [here](https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html).

#### To export and run
```bash 
$ export CLIENT_ID="XXXXX"; export CLIENT_SECRET="YYYYY"; ./main.py
```
----
Apache 2.0
