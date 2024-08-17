import requests
import json
from datetime import date

# To use this algorithm, first create an account using Spotify API. Find your client ID, client secret, and use these to gain access to your refresh token
client_id = # Fill in with your Spotify account's client ID
client_secret = # Fill in with your Spotify account's client secret

# Use an online encoder for the combined client ID and client secret
base_64_encoded = # Fill this with the returned encoding

# This is for your Spotify user ID
user_id = # Put your Spotify user ID here

# This uses the above variables to make things easier to format in the class below
auth_header = "Basic " + base_64_encoded
headers = {"Authorization": auth_header}

# Find your refresh token so that you can run this program automatically without having to manually find your access token
# To bypass this, change "self.access_token" inside of the class to what your Spotify API shows, then remove "a.new_token()" from the call in main() at the bottom
endpoint = "https://accounts.spotify.com/api/token"
# Use this simple guide to find your refresh token: https://dev.to/sabareh/how-to-get-the-spotify-refresh-token-176
refresh_token = # Fill this with your Spotify account's refresh token

class recent_songs_playlist:
    def __init__(self): # All the variables saved inside the instance of the class to continue to be used throughout the call in main() at the bottom
        self.base_64_encoded = base_64_encoded
        self.refresh_token = refresh_token
        self.auth_header = auth_header
        self.user_id =user_id
        self.endpoint = endpoint
        self.access_token = ""
        self.playlist_id = ""
        self.specified_artist = ""
        self.artist_id = ""  
        self.related_artists_ids = []
        self.related_tracks = []
    def new_token(self): # This method finds your current access token using your already known refresh token 
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query, 
                                data={"grant_type": "refresh_token", 
                                "refresh_token": refresh_token},
                                headers={"Authorization": auth_header})
        
        data = response.json()
        self.access_token = data["access_token"]
        return self.access_token
    def create_playlist(self):  # This method creates
        today = date.today()
        todayFormatted = today.strftime("%d/%m/%Y") 
        # This following line allows you to change the title and description to whatever you prefer
        request_body = json.dumps({
                "name": todayFormatted + " A Playlist Worth Listening To", "description": "A playlist of one of your favorite artist's related tracks.", "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            user_id)
        
        response = requests.post(query, data=request_body, headers={
                                    "Content-Type": "application/json",
                                    "Authorization": "Bearer {}".format(self.access_token)
        })
        response_json = response.json()
        self.playlist_id = response_json["id"]
        return self.playlist_id
    def ask_for_artist(self): # Asks for a user's input on what artist they want to find similar artists to
        self.specified_artist = input("Enter an artist you like so we can find songs you may like:\n")
        return self.specified_artist
    def search_for_artist(self): # Searches the artist in the Spotify directory and returns the artist ID
        query = "https://api.spotify.com/v1/search"
        response = requests.get(query, headers={
            "Authorization": "Bearer {}".format(self.access_token)
        }, params = {
                        "q": self.specified_artist,
                        "type": "artist",
                        "limit": "1"
        })
        response_json = response.json()
        response_indexed = response_json["artists"]["items"]
        for e in response_indexed:
            self.artist_id = str(e["id"])
            return self.artist_id
    def get_related_artists(self): # Uses the artist ID that was asked for to find the related artists to your previously specified artist
        query = "https://api.spotify.com/v1/artists/{}/related-artists".format(
            self.artist_id
        )
        response = requests.get(query, headers={
            "Authorization": "Bearer {}".format(self.access_token)
        })   
        response_json = response.json()
        for e in response_json["artists"]:
            self.related_artists_ids += [e['id']]
        return(self.related_artists_ids)
      
    def get_artist_top_tracks(self): # Gets the top tracks for each related artist and saves them in 
        for e in range(len(self.related_artists_ids)):
            query = "https://api.spotify.com/v1/artists/{}/top-tracks".format(
                self.related_artists_ids[e]
            )
            response = requests.get(query, headers={
                "Authorization": "Bearer {}".format(self.access_token)
            }, params = {
                "market": "US"
            })
            response_json = response.json()
            for e in response_json['tracks']:
                self.related_tracks += [(e['uri'])]
        self.related_tracks = self.related_tracks[:100] # Spotify only allows 100 requests to be made at a time so can only add first 100 songs, could make a 200 song playlist by slicing into separate lists
        return self.related_tracks
    
    def add_songs_to_playlist(self): # This uses the related tracks returned and adds them to the previously created playlist
        self.get_playlist = self.create_playlist()
        for e in range(len(self.related_tracks)):
            query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
                self.get_playlist, self.related_tracks[e])
            response = requests.post(query, headers={
                "Authorization": "Bearer {}".format(self.access_token)
            })
            response_json = response.json()

def main():
    a = recent_songs_playlist()
    a.new_token()
    a.ask_for_artist()
    a.search_for_artist()
    a.get_related_artists()
    a.get_artist_top_tracks()
    a.add_songs_to_playlist()

main()
