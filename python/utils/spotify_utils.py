import pandas as pd

def get_user_playlists_dataframe(spotipy, user):

    user_playlists = spotipy.user_playlists(user)
    playlist_dataframe = pd.DataFrame.from_dict(user_playlists['items'])

    return playlist_dataframe


def get_playlist_tracks_dataframe(spotipy, playlist_id):

    playlist_items = spotipy.playlist_items(playlist_id)
    print(type(playlist_items))
    playlist_tracks = [sub['track'] for sub in playlist_items['items']]
    playlist_items_dataframe = pd.DataFrame.from_dict(playlist_tracks)

    return playlist_items_dataframe

