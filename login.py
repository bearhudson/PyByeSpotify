import requests

from environs import *

AUTH_URL = 'https://accounts.spotify.com/api/token'
API_ENDPOINT = 'https://api.spotify.com/v1'

class LoginClass:

    def __init__(self):
        auth_response = requests.post(AUTH_URL, {
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

    def get_access_token(self):
        return self.access_token

    def get_user_info(self):
        user_request_url = API_ENDPOINT + '/users/' + USER_ID
        self.user_info_request = requests.get(user_request_url, headers=self.headers)
        self.user_info_request_json = self.user_info_request.json()
        return self.playlist_response_json

    def get_playlists(self):
        playlist_request_url = API_ENDPOINT + '/users/' + USER_ID + '/playlists'
        self.playlist_response = requests.get(playlist_request_url, headers=self.headers)
        self.playlist_response_json = self.playlist_response.json()
        return self.playlist_response_json

    def get_playlist_tracks(self, playlist_id):
        playlist_content_url = API_ENDPOINT + '/playlists/' + playlist_id + '/tracks'
        self.playlist_content = requests.get(playlist_content_url, headers=self.headers)
        self.playlist_content_json = self.playlist_content.json()
        return self.playlist_content_json