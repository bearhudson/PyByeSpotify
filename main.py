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
    user_playlists = user.get_playlists()
    playlist_content = user_playlists['items']
    for item in playlist_content:
        print(item['id'] + " " + item['name'])
        # tracks = user.get_playlist_tracks(item['id'])
        # print(tracks)


if __name__ == "__main__":
    main()
