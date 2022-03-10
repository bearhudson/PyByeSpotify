# PyByeSpotify

### Bulk Export your public Spotify playlists to CSV files. 

Well, eventually. Right now we're just writing to the terminal. 

You need to create a Spotify Developer account to get access to your Client ID and Client Secret from the Web API.

* [Go here](https://developer.spotify.com/dashboard/) to start your developer account creation. 
* [Go to your App Dashboard](https://developer.spotify.com/dashboard/applications) and _**CREATE AN APP**_
* Click on your newly created application to find your Client ID and your Client Secret which is hidden from view, initially. 

#### Required Environment Variables

[Spotify API](https://developer.spotify.com/documentation/web-api/)

* CLIENT_ID
* CLIENT_SECRET
* USER_ID -- _Username whose playlist you wish to extract._

#### To export and run
```bash 
Linux_Shell$ export CLIENT_ID="XXXXX"; export CLIENT_SECRET="YYYYY"; export USER_ID="ZZZZZ"; ./main.py
```
----
Apache 2.0
