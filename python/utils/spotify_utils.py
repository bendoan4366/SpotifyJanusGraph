import pandas as pd


def get_user_playlists_dataframe(spotipy, user):
    user_playlists = spotipy.user_playlists(user)
    playlist_dataframe = pd.DataFrame.from_dict(user_playlists['items'])

    return playlist_dataframe


def get_playlist_items(spotipy, playlist_id):
    playlist_items = spotipy.playlist_items(playlist_id)
    playlist_tracks = [sub['track'] for sub in playlist_items['items']]
    playlist_items_dataframe = pd.DataFrame.from_dict(playlist_tracks)

    return playlist_items_dataframe


def get_playlist_items_from_list(spotipy, user):
    playlist_dataframe = get_user_playlists_dataframe(spotipy, user)
    playlist_id_list = playlist_dataframe["id"].tolist()

    playlist_item_ids_dataframe = pd.DataFrame(columns=["id", "name"])

    for playlist_id in playlist_id_list:
        playlist_items_dataframe = get_playlist_items(spotipy, playlist_id)
        playlist_item_ids_dataframe = playlist_item_ids_dataframe.append(playlist_items_dataframe[["id", "name"]])

    return playlist_item_ids_dataframe


def get_track_audio_features(spotipy, track_id):
    track_audio_features = spotipy.audio_features(track_id)

    return track_audio_features


def get_playlist_tracks_audio_features(spotipy, user):
    playlist_items_dataframe = get_playlist_items_from_list(spotipy, user)

    playlist_track_ids_list = playlist_items_dataframe["id"].tolist()
    print(playlist_track_ids_list)
    playlist_audio_features = get_track_audio_features(spotipy, playlist_track_ids_list)

    playlist_audio_features_dataframe = pd.DataFrame.from_dict(playlist_audio_features)

    return playlist_audio_features_dataframe