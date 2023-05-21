# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pickle


def get_credentials(port_number = 8080):
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    client_secrets_file = "client_secret_145667257242-aeg2fu6n661qg277k0c8sjsb7kub5m64.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    
    # Try different ports starting from 8080 until you find an available one.
    success = False
    while not success:
        try:
            credentials = flow.run_local_server(port=port_number)
            success = True
            print("Succesfully connected to port " + str(port_number))
        except PermissionError:
            port_number += 1

    return credentials

#store credentials in a pickle file

def store_credentials():
    credentialsx = get_credentials()
    with open('credentials.pickle', 'wb') as f:
        pickle.dump(credentialsx, f)
        
# store_credentials()

def load_credentials():
    with open('credentials.pickle', 'rb') as f:
        credentials = pickle.load(f)
    return credentials    

def get_youtube_object():
    credentials = load_credentials()
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    return youtube

def get_video_info(video_id):
    youtube = get_youtube_object()

    #https://www.youtube.com/watch?v=gh2RXE9BIN8&ab_channel=LowLevelLearning
    #id="Ks-_Mh1QhMc"
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id = video_id
    )
    response = request.execute()
    video_title = response['items'][0]['snippet']['title']
    video_description = response['items'][0]['snippet']['description']
    video_publishedAt = response['items'][0]['snippet']['publishedAt']
    video_viewCount = response['items'][0]['statistics']['viewCount']
    
    dict_info =  {'title': video_title, 
                  'publishedAt': video_publishedAt, 
                  "video_viewCount": video_viewCount }
    
    return dict_info

def get_info_of_channel_last_playlist(id_channel, maxim_res = 1):
    youtube = get_youtube_object()
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId=id_channel,
        maxResults= maxim_res,
    )
    response = request.execute()

    total_playlists_of_channel = response['pageInfo']['totalResults']
    playlist_first_name = response['items'][0]['snippet']['title']
    playlist_video_count = response['items'][0]['contentDetails']['itemCount']
    playlist_name = response['items'][0]['snippet']['title']
    dict_info_playlist = {"playlist_name": playlist_name,
                          "total_playlists_of_channel": total_playlists_of_channel,
                          "playlist_video_count": playlist_video_count
                          }
    return dict_info_playlist



def get_video_id_from_url(url_video):
    #ex 
    id = url_video.split("watch?v=")[1].split("&")[0]
    return id
    
    
if __name__ == "__main__":
    id_video = "2ybLD6_2gKM"
    video_details = get_info_of_channel_last_playlist(maxim_res= 5)
    import json
    print(json.dumps(video_details, indent=2, sort_keys=False))