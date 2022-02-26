## Twitter Lyrics Bot
Python program that gets songs and lyrics from artist of user choice, randomly chooses a song then a lyric and chooses a random couplet or triplet, then uses AWS Lambda automatically to tweet lyrics

Example with MF Doom, a rapper known for his incredible rhyme schemes:
https://twitter.com/mf_doom_lyric

# Usage 
1- Install tweepy and lyricsgenius modules using 
```
pip install tweepy
pip install lyricsgenius
```
2- Enter in artist name and specific songs

3- Create genius account and get API key

4- If you want a list of all songs from an artist, call the get_song_names function

5- Set up a Twitter developer account and get API keys


# Deployment
1- Create a virtual environment and install tweepy and lyricsgenius

2- Deploy to AWS Lambda as a ZIP file

3- Use CloudWatch events to automatically tweet lyrics in a timely pattern

