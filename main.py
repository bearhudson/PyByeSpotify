#!/usr/bin/python3

from login import LoginClass


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
    user = LoginClass()
    user_name = user.user_class.display_name
    print(f"\nPlaylists for user: {user_name}\n--------------")
    playlists = []
    user_playlists = get_playlists_recursive(50, 0, user, playlists)
    for pl_item in user_playlists:
        track_slice = []
        track_count = pl_item.tracks.total
        track_slice = get_tracks_recursive(track_count, 0, user, playlist_id=pl_item.id, track_slice=track_slice)
        print(f"\nPlaylist Name: {pl_item.name} -- Track Count: {track_count}\n--------------")
        for cur_track in track_slice:
            artist_list = []
            for artist in cur_track.track.artists:
                artist_list.append(artist.name)
            track_name = cur_track.track.name
            album_name = cur_track.track.album.name
            print(f"{artist_list} - {album_name} - {track_name}")


if __name__ == "__main__":
    main()
