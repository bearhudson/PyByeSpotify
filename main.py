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
from trackclass import TrackClass


def main():
    global tracks_slice
    user = LoginClass()
    track_list = []
    user_name_info = user.get_user_info()
    user_name = user_name_info['display_name']
    print(f"\nPlaylists for user: {user_name}")
    user_playlists = user.get_playlists(playlist_limit="2", offset="0")
    playlist_content = user_playlists['items']
    # TODO: use recursion to get the full playlist track listing
    for pl_item in playlist_content:
        track_count_slice = pl_item['tracks']
        track_count = track_count_slice['total']
        if track_count <= 20:
            tracks_slice = user.get_playlist_tracks(pl_item['id'])
        elif 20 < track_count <= 50:
            tracks_slice = user.get_playlist_tracks(pl_item['id'], track_limit=str(track_count))
        elif track_count > 50:
            track_c_remaining = track_count
            while track_c_remaining > 0:
                tracks_slice = user.get_playlist_tracks(pl_item['id'], track_limit=str(track_c_remaining))
        print(f"\nPlaylist ID: {pl_item['id']} -- Name: {pl_item['name']} -- Track Count: {track_count}")
        tracks = tracks_slice['items']
        for track in tracks:
            artist_list = []
            track_slice = track['track']
            artist_slice = track_slice['artists']
            if len(artist_slice) >= 1:
                for artist in artist_slice:
                    artist_list.append(artist['name'])
            else:
                artist_list.append(track_slice['artists'])
            if track_slice['album']['album_type'] == 'single':
                track_list.append(TrackClass(name=track_slice['name'],
                                             artist=artist_list,
                                             release=track_slice['album']['release_date'],
                                             album="",
                                             is_single=True))
                print('single')
                print(track_list[len(track_list)-1].return_details())
            else:
                print('album')
                track_list.append(TrackClass(name=track_slice['name'],
                                             artist=artist_list,
                                             release=track_slice['album']['release_date'],
                                             album=track_slice['album']['name'],
                                             is_single=False))
                print(track_list[len(track_list)-1].return_details())


if __name__ == "__main__":
    main()
