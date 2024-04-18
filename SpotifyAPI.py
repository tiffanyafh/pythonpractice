import requests

def search_albums():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

url = 'https://api.spotify.com/v1/albums?ids=2qo8j9yZIsx66yDuUho2jp,4wVrfNzE3Dab7EB1Xn6SHo,3wOG84RkmoSoeN3LKkxXga,3HWlgRjxW0H7fWm1n2LBbE,4i5b4YWuMtneUSvQPONwzK,4kS7bSuU0Jm9LYMosFU2x5'
headers = {
    "Authorization" : "Bearer BQA8u2y7vJaL9y-L_QDz9rFP-7rIEG1qo4FA8lrAACVvS_uIvHeXX5ZvxJNa8PeIRmZQJA9kkZDi-hq-h54hSvzWCrdisw_c5EXwtOsxyPhrDWpJjy8",
    "content_type" : "application/json"
}

albums_data = search_albums()


if albums_data:
    print("Which album do you want to listen to?")
    for index, album in enumerate(albums_data['albums']):
        print(f"{index+1}. {album['name']} by {album['artists'][0]['name']}")

    choice = input("Enter the number of the album you want to listen to: ")
    choice = int(choice) - 1

    if 0 <= choice < len(albums_data['albums']):
        selected_album = albums_data['albums'][choice]
        album_name = selected_album['name']
        artist_name = selected_album['artists'][0]['name']
        album_id = selected_album['id']
        album_link = f"https://open.spotify.com/album/{album_id}"
        print(f"You selected: {album_name} by {artist_name}")
        print("Listen to it here:", album_link)
    else:
        print("Invalid choice. Please select a valid number.")
else:
    print("No albums found.")



#remember: to request another "access token" because it expires every hour (just go to Postman, under Spotify API, select tab: POST NEW REQUEST and SEND. Updated access token will appear on the bottom.
#make sure to update the "access token" under the specific task (EX. go to tab GET access to several albums and update code under Authorization tab" IF NOT CODE WILL NOT RUN BC ITS 400 NOT FOUND