#!/usr/bin/python3

from login import LoginClass
from ytmusicapi import YTMusic
from time import sleep


def get_playlists_recursive(count, reps, user, playlists):
    try:
        if count > 20:
            get_playlists_recursive(count - 20, reps + 1, user, playlists)
        playlists += user.get_playlists(playlist_limit=count, offset=(reps * 50))
    except ValueError:
        print("Error")
    return playlists


def get_tracks_recursive(count, reps, user, playlist_id, track_slice):
    try:
        if count > 50:
            get_tracks_recursive(count - 50, reps + 1, user, playlist_id, track_slice)
        track_slice += user.get_playlist_tracks(playlist_id=playlist_id, track_limit=50, offset=(reps * 50))
    except ValueError:
        print("Error")
    return track_slice


def main():
    spotify_user = input("Enter Username: ")
    start_position = int(input("Enter start position[0]: " or 0))
    google_import_bool = bool(input("Run import into Youtube Music[no]?: ") or False)
    user = LoginClass(user_name=f"{spotify_user}")
    yt = YTMusic('oauth.json')
    user_name = user.user_class.display_name
    print(f"\nPlaylists for user: {user_name}\n---")
    playlists = []
    user_playlists = get_playlists_recursive(50, 0, user, playlists)
    if start_position > 0:
        user_playlists = user_playlists[start_position:]
    for pl_item in user_playlists:
        track_slice = []
        track_count = pl_item.tracks.total
        track_slice = get_tracks_recursive(track_count, 0, user, playlist_id=pl_item.id, track_slice=track_slice)
        print(f"\nPlaylist Name: {pl_item.name} -- Track Count: {track_count}\n---")
        if google_import_bool:
            playlistId = yt.create_playlist(f'{pl_item.name}', f'{pl_item.name} Imported from Spotify')
        for cur_track in track_slice:
            artist_list = []
            for artist in cur_track.track.artists:
                artist_list.append(artist.name)
            print(f"{artist_list} - "
                  f"{cur_track.track.name} - "
                  f"{cur_track.track.album.name} - "
                  f"{cur_track.track.album.release_date}")
            search_results = yt.search(f"{artist_list} {cur_track.track.name} {cur_track.track.album.name}")
            if google_import_bool:
                try:
                    yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
                except KeyError:
                    yt.add_playlist_items(playlistId, [search_results[1]['videoId']])
            print(search_results)
            sleep(10)


if __name__ == "__main__":
    main()
