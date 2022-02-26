import tweepy
import lyricsgenius
import random

# Insert API keys and info here
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''
genius_token = ''
genius = lyricsgenius.Genius(genius_token)

# The songs + artist 
artist_name = ''
songs = []

# Use this to get all known songs from an Artist in the Genius database
def get_song_names():
    artist = genius.search_artist(artist_name)
    print(artist.songs)

# Get lyrics for the songs you selected and place them in .txt
# files in the current directory
def get_lyrics(songs):
    for i in range(len(songs)):
        title = songs[i]
        lyrics = genius.search_song(title, artist_name).lyrics.split('\n')
        f = open(str(i) + '.txt', 'w', encoding='utf-8')
        new_lyrics = []
        for i in range(len(lyrics) - 1):
            valid = True
            if '[' in lyrics[i]:
                valid = False
            if valid == True:
                new_lyrics.append(lyrics[i])
        f.write('\n'.join(new_lyrics))
        f.close()

# Chooses random song, and 2-3 random lines within a song to be tweeted
def tweet_format():
    unvalid = True
    while unvalid is True:
        song = random.randint(0, len(songs) - 1)
        tweet_len = random.randint(0,4)
        filename = str(song) + '.txt'
        file = open(filename, 'r', encoding='utf-8')
        filelist = list(file)
        line = random.randint(1, len(filelist) - 2)
        if tweet_len < 4:
            if filelist[line] != '\n' and filelist[line+1] != '\n':
                unvalid = False
        elif tweet_len == 4:
            if filelist[line] != '\n' and filelist[line+1] != '\n' and filelist[line+2] != '\n':
                unvalid = False
    if tweet_len < 4:
        return(filelist[line] + filelist[line+1])
    if tweet_len == 4:
        return(filelist[line] + filelist[line+1] + filelist[line+2])

# Handles tweeting the lyrics through AWS Lambda
def handler(event, context):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(tweet_format())