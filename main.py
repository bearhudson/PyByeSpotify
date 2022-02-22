import requests
import rich
import json
import base64
import hashlib
import html
import os
import getpass
from environs import *
from login import LoginClass


def main():
    user = LoginClass()
    user.get_access_token()
    user_playlists = user.get_playlists(playlist_limit="50", offset="0")
    playlist_content = user_playlists['items']
    for pl_item in playlist_content:
        track_count_slice = pl_item['tracks']
        track_count = track_count_slice['total']
        if track_count <= 20:
            tracks_slice = user.get_playlist_tracks(pl_item['id'])
        elif track_count <= 50:
            tracks_slice = user.get_playlist_tracks(pl_item['id'], track_limit=str(track_count))
        print(f"\n\nPlaylist ID: {pl_item['id']} -- Name: {pl_item['name']} -- Track Count: {track_count}")
        tracks = tracks_slice['items']
        for track in tracks:
            track_slice = track['track']
            artist_list = []
            if len(track_slice['artists']) > 1:
                for artist in track_slice['artists']:
                    artist_list.append(artist['name'])
            else:
                artist_list.append(artist['name'])
            if track_slice['album']['album_type'] == 'single':
                print(f"{artist_list} - {track_slice['name']} [{track_slice['album']['release_date']}]")
            else:
                track_album = track_slice['album']['name']
                print(f"{artist_list} - {track_slice['name']} [{track_album} {track_slice['album']['release_date']}]")


if __name__ == "__main__":
    main()
