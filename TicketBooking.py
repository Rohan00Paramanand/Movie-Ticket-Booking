from random import sample

Cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Chandigarh', 'Shimla']
Movies_by_theatre = {
    'PVR': ['Bahubali 1', 'Bahubali 2', 'RRR', 'The Kashmir Files'],
    'INOX': ['RRR', 'Bhool Bhulaiyaa', 'Singham'],
    'US Cinemas': ['Bahubali 2', 'Dabangg', 'Bajarangi Bhaijaan'],
    'JAM': ['URI: The Surgical Strike', 'RRR', 'Life of Pi', 'English Medium'],
}

def choose_city():
    while True:
        print ("Choose your city.")
        for idx, city in enumerate(Cities):
            print (f"{idx + 1}: {city}")

        try:
            city_choice = int(input("Pick your city (1-6) ")) - 1
            if 0 <= city_choice < len(Cities):
                show_theatres(Cities[city_choice])
                break
            else:
                print ("Invalid choice. Please try again.")
        except ValueError:
            print ("Please enter only number.")

def show_theatres(city):
    while True:
        print (f"List of theatres in {city}.")
        theatres = list(Movies_by_theatre.keys())
        for idx, theatre in enumerate(theatres):
            print (f"{idx + 1}: {theatre}")

        try:
            theatre_choice = int(input("Pick your theatre (1-4) ")) - 1
            if 0 <= theatre_choice < len(theatres):
                show_movies(theatres[theatre_choice])
                break
            else:
                print ("Invalid choice. Please try again.")
        except ValueError:
            print ("Please enter only number.")

def show_movies(theatre):
    while True:
        available_movies = sample(Movies_by_theatre[theatre], k=min(3, len(Movies_by_theatre[theatre])))
        print (f"Available movies in {theatre}:")
        for idx, movie in enumerate(available_movies):
            print (f"{idx + 1}: {movie}")

        try:
            movie_choice = int(input(f"Pick your movie (1-{len(available_movies) + 1}) ")) - 1
            if 0 <= movie_choice < len(available_movies):
                book_tickets(available_movies[movie_choice])
                break
            else:
                print ("Invalid choice. Please try again.")
        except ValueError:
            print ("Please enter only number.")

def book_tickets(movie):
    while True:
        try:
            tickets = int(input(f"How many tickets for {movie}? "))
            if tickets > 0:
                print (f"Successfully purchased {tickets} tickets for {movie}!")
                break
            else:
                print ("Please enter a positive number.")
        except ValueError:
            print ("Please enter only number.")

choose_city()