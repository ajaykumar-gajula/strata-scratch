"""You're tasked with analyzing a Spotify-like dataset that captures user listening habits.
For each user, calculate the total listening time and the count of unique songs they've listened to. In the database duration values are displayed in seconds. Round the total listening duration to the nearest whole minute.


The output should contain three columns: 'user_id', 'total_listen_duration', and 'unique_song_count'.
Dataframe: listening_habits
user_id:int
song_id:int
listen_duration:float
"""

# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
gdf = listening_habits.groupby(['user_id']).agg({'song_id':'nunique','listen_duration':'sum'}).reset_index()
gdf['listen_duration'] = round(gdf['listen_duration']/60)
gdf.rename(columns={'listen_duration':'total_listen_duration','song_id':'unique_song_count'},inplace=True)
gdf
