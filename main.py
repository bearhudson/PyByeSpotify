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
        tracks_slice = []
        if track_count <= 20:
            tracks_slice = user.get_playlist_tracks(pl_item['id'])
        elif 20 < track_count <= 50:
            tracks_slice = user.get_playlist_tracks(pl_item['id'], track_limit=str(track_count))
        elif track_count > 50:
            track_c_remaining = track_count
            while track_c_remaining > 0:
                tracks_slice.append(user.get_playlist_tracks(pl_item['id'], track_limit=str(track_c_remaining)))
        print(f"\nPlaylist ID: {pl_item['id']} -- Name: {pl_item['name']} -- Track Count: {track_count}")
        tracks = tracks_slice['items']
        for track in tracks:
            track_slice = track['track']
            artist_list = []
            artist_slice = track_slice['artists']
            if len(artist_slice) >= 1:
                for artist in artist_slice:
                    artist_list.append(artist['name'])
            else:
                artist_list.append(track_slice['artists'])
            if track_slice['album']['album_type'] == 'single':
                print(f"{artist_list} - {track_slice['name']} [{track_slice['album']['release_date']}]")
            else:
                track_album = track_slice['album']['name']
                print(f"{artist_list} - {track_slice['name']} [{track_album} {track_slice['album']['release_date']}]")
            artist_list.clear()


if __name__ == "__main__":
    main()
