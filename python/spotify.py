import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import utils.spotify_utils

#extract credentials from environment variabes and instantiate session
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

myPlaylists = utils.spotify_utils.get_user_playlists_dataframe(sp, "ben.doan4366")
ids = myPlaylists.loc[:, ["id", "name"]]

id_dict = ids.to_dict()
print(id_dict)