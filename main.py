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
    global track_slice
    user = LoginClass()
    user_name = user.user_class.display_name
    print(f"\nPlaylists for user: {user_name}")
    user_playlists = user.get_playlists(playlist_limit="50", offset="0")
    for pl_item in user_playlists:
        track_count = pl_item.tracks.total
        print(f"\nPlaylist ID: {pl_item.id} -- Name: {pl_item.name} -- Track Count: {track_count}")
        while track_count > 50:
            track_position = int(track_count) - 50
            offset = track_count - track_position
            track_slice = user.get_playlist_tracks(pl_item.id, track_limit=track_position, offset=offset)
            track_count -= track_position
        else:
            track_slice = user.get_playlist_tracks(pl_item.id, track_limit=str(track_count))

        for cur_track in track_slice:
            artist_list = []
            for artist in cur_track.track.artists:
                artist_list.append(artist.name)
            track_name = cur_track.track.name
            album_name = cur_track.track.album.name
            print(f"{artist_list} - {album_name} - {track_name}")


if __name__ == "__main__":
    main()
