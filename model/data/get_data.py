"""
A short script to collect data from geniuslyrics
"""
# imports
import lyricsgenius
import json

# sign up for a free account at Genius.com to access the API - http://genius.com/api-clients
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# A small library based on the above API - https://github.com/johnwmillr/LyricsGenius
genius = lyricsgenius.Genius(token, skip_non_songs=False)

# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True
# remove certain terms
genius.excluded_terms = ["(Remix)", "(Live)", "[Live]", "(Radio Edit)", "(Clean)", "(Clean Version)"] 
# get the full Tenacious D discography! 
td = genius.search_artist("Tenacious D", max_songs=150, sort="title")
# save to a json file
td.save_lyrics(overwrite=True)

# open the json and extract the lyrics as a list of songs
with open('Lyrics_TenaciousD.json') as f:
    d = json.load(f)
lyrics = [x["lyrics"].split("Lyrics")[-1] for x in d["songs"]]

# write all the lyrics to a single txt file
with open('lyrics.txt', 'w') as f:
    for song in lyrics:
        f.write(f"{song}\n")
