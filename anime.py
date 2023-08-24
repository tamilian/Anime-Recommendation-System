import requests

from sklearn.neighbors import NearestNeighbors

def main():
    print("Welcome to Harsh's Anime Recommendation System!\n")
    proceed = input("Would you like to receive anime recommendations? (yes/no): \n")
    
    if proceed.lower() == 'yes':
        print("Okay, let's proceed!")
    else:
        print("Okay, Bye!")
        quit()


    print("Are you an experienced anime viewer or someone who has just started watching?\n")
    user_input = input("Please enter 'yes' if you are an experienced viewer, or 'no' if you are new to anime: \n")

    
    if user_input.lower() == 'yes':
        recommend_anime() 
    elif user_input.lower() == 'no':
        newer_viewer()
    else:
        print("This is an invalid input. You will be taken to the start of the program.")
        main()




        
def newer_viewer(): # call this function when the user says this is their first time 
    print("I understand you are newer to anime or this is your first time.")
    genres = ['Action', 'Adventure', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Sports']
    
    print("Here are the genres below: ")
    
    for count, genre in enumerate(genres, 1):
        print(f"{count}. {genre}")
        
    
    genres = ['Action', 'Adventure', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Sports' ]
    
    genre_recommendations = {  # store it as a dictionary and we can call the dictionatry
    1: ['Attack on Titan', 'Fullmetal Alchemist: Brotherhood', 'Gintama', 'Hunter x Hunter', 'Bleach'],
    2: ['Fullmetal Alchemist: Brotherhood', 'Bleach', 'Hunter x Hunter', 'Vinland Saga', 'One Piece'],
    3: ['Sword Art Online', 'Re:Zero', 'No Game No Life', 'Fairy Tail', 'The Rising of the Shield Hero'],
    4: ['Tokyo Ghoul', 'Parasyte', 'Another', 'Higurashi no Naku Koro ni', 'Elfen Lied'],
    5: ['Death Note', 'Steins;Gate', 'The Promised Neverland', 'Durarara!!', 'Erased'],
    6: ['Toradora!', 'Your Lie in April', 'Clannad', 'Golden Time', 'My Little Monster'],
    7: ['Steins;Gate', 'Cowboy Bebop', 'Ghost in the Shell', 'Neon Genesis Evangelion', 'Psycho-Pass'],
    8: ['Haikyuu!!', 'Kuroko no Basket', 'Hajime No Ippo', 'Ping Pong the Animation', 'Free!'],
    }

    while True:
        genre_input = input("What genres are you most interested in? Enter the number correlated with the genre (1-8): ")
        
        if genre_input.isdigit() and 1 <= int(genre_input) <= 8:
            selected_genre_index = int(genre_input)
            selected_recommendations = genre_recommendations[selected_genre_index]
            
            print(f"You have selected {genres[selected_genre_index - 1]}. Here are some recommendations:")
            for index, anime in enumerate(selected_recommendations, 1):
                print(f"{index}. {anime}")
        
            break
        else:
            print("Your input was not recognized. Please enter a number between 1 and 8.")
    
    summary_input = input("Would you like to get a summary of any of the recommended anime (Yes or No)? ")

    if summary_input.lower() == 'yes':
        anime_summary()

    else:
        secondary_user_input = input('''If not, would you like to get more anime or would you like to exit the program \n
                                        Type 1 for new genre and 2 to exit the program. (1 or 2)?''')

        if secondary_user_input == 1:
            newer_viewer()
        else:
            quit()

def recommend_anime(): # k nearest neighbor algorithm 
    # Sample anime titles
    anime_titles = [
        "Attack on Titan", "Death Note", "One Piece", "Naruto", "My Hero Academia",
        "Sword Art Online", "Tokyo Ghoul", "Fullmetal Alchemist: Brotherhood",
        "Dragon Ball Z", "Demon Slayer", "Hunter x Hunter", "Neon Genesis Evangelion",
        "Cowboy Bebop", "Dragon Ball", "Black Clover", "Fairy Tail", "One Punch Man",
        "Steins;Gate", "JoJo's Bizarre Adventure", "The Promised Neverland",
        "Fullmetal Alchemist", "Bleach", "Code Geass", "Attack on Titan: Junior High",
        "Naruto: Shippuden", "Fruits Basket", "Dragon Ball Super", "Death Parade",
        "Soul Eater", "AoT: No Regrets"
    ]

    genres = ['Action', 'Adventure', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Sports']

    # Sample anime genre data (binary: 1 for present, 0 for absent)
    anime_features = [
        [1, 0, 0, 0, 0, 0, 0, 0],  # Attack on Titan: Action
        [0, 0, 0, 1, 1, 0, 0, 0],  # Death Note: Horror, Mystery
        [1, 1, 1, 0, 0, 0, 0, 0],  # One Piece: Action, Adventure, Fantasy
        [1, 1, 0, 0, 0, 0, 0, 0],  # Naruto: Action, Adventure
        [1, 0, 0, 0, 0, 1, 0, 0],  # My Hero Academia: Action, Romance
        [1, 1, 1, 0, 0, 1, 1, 0],  # Sword Art Online: Action, Adventure, Fantasy, Romance, Sci-Fi
        [1, 1, 0, 1, 1, 0, 0, 0],  # Tokyo Ghoul: Action, Adventure, Horror, Mystery
        [1, 0, 0, 0, 0, 0, 0, 0],  # Fullmetal Alchemist: Brotherhood: Action
        [1, 0, 0, 0, 0, 0, 0, 0],  # Dragon Ball Z: Action
        [0, 1, 0, 0, 0, 0, 0, 0],  # Demon Slayer: Adventure
        [1, 0, 0, 0, 0, 0, 0, 0],  # Hunter x Hunter: Action
        [0, 1, 0, 1, 0, 0, 0, 0],  # Neon Genesis Evangelion: Adventure, Fantasy
        [1, 0, 0, 0, 0, 0, 0, 0],  # Cowboy Bebop: Action
        [1, 0, 0, 0, 0, 0, 0, 0],  # Dragon Ball: Action
        [1, 1, 0, 0, 0, 0, 0, 0],  # Black Clover: Action, Adventure
        [1, 0, 0, 0, 0, 0, 0, 0],  # Fairy Tail: Action
        [1, 0, 0, 0, 0, 0, 0, 0],  # One Punch Man: Action
        [0, 0, 0, 1, 1, 0, 1, 0],  # Steins;Gate: Horror, Mystery, Sci-Fi
        [0, 1, 0, 0, 0, 0, 0, 0],  # JoJo's Bizarre Adventure: Adventure
        [1, 0, 0, 1, 0, 0, 0, 0],  # The Promised Neverland: Action, Horror
        [1, 0, 0, 0, 0, 0, 0, 0],  # Fullmetal Alchemist: Action
        [0, 1, 0, 0, 0, 0, 0, 0],  # Bleach: Adventure
        [1, 0, 0, 0, 0, 0, 0, 0],  # Code Geass: Action
        [1, 0, 0, 0, 0, 1, 0, 0],  # Attack on Titan: Junior High: Action, Romance
        [1, 0, 0, 1, 0, 0, 0, 0],  # Naruto: Shippuden: Action, Adventure
        [0, 0, 0, 1, 1, 0, 1, 0],  # Fruits Basket: Horror, Mystery, Sci-Fi
        [1, 0, 0, 0, 0, 0, 0, 0],  # Dragon Ball Super: Action
        [0, 1, 0, 0, 0, 0, 0, 0],  # Death Parade: Adventure
        [1, 0, 0, 0, 0, 0, 0, 0],  # Soul Eater: Action
        [1, 0, 0, 0, 0, 0, 0, 0],  # AoT: No Regrets: Action
    ]

    # Create a NearestNeighbors model
    model = NearestNeighbors(n_neighbors=3)
    model.fit(anime_features)

    anime_titles_input = input("Enter the names of the anime you have watched (separated by commas): ")
    anime_titles_input = anime_titles_input.split(",")

    anime_titles_input = [title.strip() for title in anime_titles_input]

    for anime_title in anime_titles_input:
        if anime_title not in anime_titles:
            print(f"{anime_title} is not currently in our database. Please try again.")
            recommend_anime()
        else:
            continue


    # Get the indices of the user's input anime titles
    anime_indices = [anime_titles.index(title) for title in anime_titles_input]

    # Get the corresponding anime features based on the indices
    anime_features_input = [anime_features[index] for index in anime_indices]

    # Perform k-nearest neighbors algorithm to get similar anime recommendations
    distances, indices = model.kneighbors(anime_features_input)

    # Print recommended anime for each input title
    for i, anime_title in enumerate(anime_titles_input):
        recommended_anime_indices = indices[i][1:]  # Exclude the input anime itself
        recommended_anime = [anime_titles[idx] for idx in recommended_anime_indices]

        print(f"For anime '{anime_title}', recommended similar anime:")
        print(", ".join(recommended_anime))

    summary_input = input("Would you like to get a summary of any of the recommended anime (Yes or No)?")

    if summary_input.lower() == 'yes':
        anime_summary()

    else:
        proceed_input = input("Would you like to get more recommendations? Type 'yes' for more and 'no' to exit the program. \n")

        if proceed_input == 'yes':
            recommend_anime()

        else:
            quit()

def anime_summary():
    anime_summary = input("Enter the name of the anime: ")  # Take user input for the anime name
    url = 'https://graphql.anilist.co' # this is endpoint to which we will send url

    query = f'''
    query {{
      Media(search: "{anime_summary}", type: ANIME) {{
        title {{
          english
          romaji
        }}
        description
      }}
    }}
    '''
    # Send the request to the API
    response = requests.post(url, json={"query": query})

    # Check if the request was successful
    if response.status_code == 200:  # evaluates to true
        data = response.json()
        anime = data.get("data", {}).get("Media")

        if anime:
            title = anime["title"]["english"] or anime["title"]["romaji"]
            summary = anime["description"]
            print("Title:", title)
            print("Summary:", summary)
        else:
            print("Anime not found.")
    else:
        print("Error:", response.status_code)
    


main()