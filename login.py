import requests
from environs import *
from userclass import UserClass
from playlistclass import PlaylistClass
from trackclass import TrackClass

AUTH_ENDPOINT = 'https://accounts.spotify.com/api/token'
API_ENDPOINT = 'https://api.spotify.com/v1'


class LoginClass:

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_info_request = None
        self.playlist_response = None
        self.playlist_class = None
        self.playlist_content = None
        self.track_object = None
        auth_response = requests.post(AUTH_ENDPOINT, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        })
        auth_response_data = auth_response.json()
        self.access_token = auth_response_data['access_token']
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }
        self.user_request_url = API_ENDPOINT + '/users/' + self.user_name
        self.user_class = self.user_check()
        self.params = {}

    def get_access_token(self):
        return self.access_token

    def get_playlists(self, playlist_limit="20", offset="0"):
        self.params = {
            'limit': playlist_limit,
            'offset': offset
        }
        playlist_request_url = API_ENDPOINT + '/users/' + self.user_name + '/playlists'
        self.playlist_response = requests.get(playlist_request_url, headers=self.headers, params=self.params)
        self.playlist_class = PlaylistClass.model_validate_json(self.playlist_response.text)
        return self.playlist_class.items

    def get_playlist_tracks(self, playlist_id, track_limit="50", offset="0"):
        self.params = {
            'limit': track_limit,
            'offset': offset
        }
        playlist_content_url = API_ENDPOINT + '/playlists/' + playlist_id + '/tracks'
        self.playlist_content = requests.get(playlist_content_url, headers=self.headers, params=self.params)
        self.track_object = TrackClass.model_validate_json(self.playlist_content.text)
        return self.track_object.items

    def user_check(self):
        self.user_info_request = requests.get(self.user_request_url, headers=self.headers)
        self.user_info_request.raise_for_status()
        return UserClass.model_validate_json(self.user_info_request.text)
