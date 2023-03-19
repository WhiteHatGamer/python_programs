import sys

#For easing Condition checking and First Operation
MOVIE_TEMPLATE = {'title' : str, 'year':int, 'genre': tuple, 'director':str}

#initialising empty list for storing temporary
movies = []
"""
    {"title" : "The Shawshank Redemption", "year":1994, "genre":("Drama", ), "director":"Frank Darabont"}
    {"title" : "The Godfather", "year":1972, "genre":("Crime", "Drama"), "director":"Francis Ford Coppola"}
"""

#storing the local txt file to variable as list of dictionaries
with open("movies.txt",'r') as movie_file:
    for movie in movie_file:
        movies.append(eval(movie))

#constant Menu prompt
MENU_PROMPT = "\n'a' to add Movie\n'd' to Display Movies\n's' to Search a Movie\n'q' to Quit\nEnter Your Choice: "

#Function For adding New Movies to list
def add_movie():
    if (sys._getframe(1).f_code.co_name) == "test":   #Test Block - Fold Block for better Understanding 
        print("\nEnter Movie title : Forrest Gump")
        print("Enter Released Year : 1994")
        print("Enter Movie Genre (seperated by comma','): Drama,Romance")
        print("Enter Director : Robert Zemeckis")
        title = "Forrest Gump"
        year = 1994
        genre = "Drama,Romance"
        director = "Robert Zemeckis"
        genre = tuple(genre.split(","))
        movies.append({
        "title": title,
        "year":year,
        "genre":genre,
        "director":director 
        })
        print("Movie Added: ")
        display_movie(movies[-1])
        return
    #Asking for Movie Properties - 
    #initialising new dictionary
    prop_dict = {}
    for key in list(MOVIE_TEMPLATE.keys()):
        #checking if property is multiple as MOVIE_TEMPLATE
        if(MOVIE_TEMPLATE[key] == tuple):
            property = input(f"Enter Movie {key.title()}(seperated by comma','): ").title()
            property = tuple(property.split(",")) #Changing the input string type to Match Template
            prop_dict.update({key:property})
            continue
        #converting input string as Template
        property = MOVIE_TEMPLATE[key](input(f"Enter Movie {key.title()}: ").title())
        prop_dict.update({key:property})
    movies.append(prop_dict)
    #Displaying Last added Movie
    print("Movie Added: ")
    display_movie(movies[-1])
    pass


#Function For Displaying Entire Movies
def display():
    for movie in movies:
        display_movie(movie)
    pass


#Function for Displaying One Given Movie Dictionary
def display_movie(movie):
    print('')
    for key in list(MOVIE_TEMPLATE.keys()):
        if MOVIE_TEMPLATE[key]==tuple:
            #To Print Tuples Like Joined String for User Friendlyness
            tuple_string = ', '.join(movie[key])
            print(f"\t{key.title()}\t: {tuple_string}")
            continue
        print(f"\t{key.title()}\t: {movie[key]}")
    print('')
    pass


#Function For Finding Movies Accoriding to Keys of movie
def find_movie():
    if not any(movies):
        print("No Movies Available In Data. Exiting...")
        return
    
    #Listing Available Keys of the data
    print("Movie Properties: " + ", ".join(list(MOVIE_TEMPLATE.keys())).title())
    if (sys._getframe(1).f_code.co_name) == "test": #Test Block Fold for better Understanding
        find_key = "TiTlE"
        print(f"What property of Movie you looking for: {find_key}")
        find_key = find_key.lower().replace(" ","")
        find_term = "ThE SHaWsHaNkReDeMpTiOn"
        print(f"What are you searching for: {find_term}")
        find_term = find_term.lower().replace(" ","")
        found_flag = True
        for movie in movies:
            if movie[find_key].lower().replace(" ","")==find_term:
                print(f"\nMovie Found with {find_key.title()} - {movie[find_key]} :")
                display_movie(movie)
                found_flag = False
                continue
        print("Movie Properties: " + ", ".join(list(movies[0].keys())).title())
        find_key = "year"
        print(f"What property of Movie you looking for: {find_key}")
        find_term = "1994"
        print(f"What are you searching for: {find_term}")
        find_term = find_term.lower().replace(" ","")
        found_flag = True
        for movie in movies:
            if str(movie[find_key]).lower().replace(" ","")==find_term:
                print(f"\nMovie Found with {find_key} - {movie[find_key]} :")
                display_movie(movie)
                found_flag = False
                continue
        return
    find_key = input("What property of Movie you looking for: ").lower()
    if find_key not in MOVIE_TEMPLATE.keys():
        print("Invalid term. Exiting...")
        return
    
    find_term = input("What are you searching for: ")
    #Changing the string to Not be case sensitive and removing spaces
    find_term = find_term.lower().replace(" ","")
    found_flag = True
    for movie in movies:
        if str(movie[find_key]).lower().replace(" ","")==find_term:
            print(f"\nMovie Found with {find_key} - {movie[find_key]} :")
            display_movie(movie)
            found_flag = False
            continue

    #Checking If no movies found with given terms
    if found_flag:
        print("Movie not found")
    pass


#Adding the user options as Dictionaries and functions as its values
user_options = {
    'a':add_movie,
    'd':display,
    's':find_movie,
}


#Main Function
def main():
    while(True):
        choice = input(MENU_PROMPT)
        if choice in user_options.keys():
            user_options[choice]()
        elif choice == 'q':
            print("Saving File...")
            break
        else:
            print("Invalid Choice")
    #Saving the file opening as Write mode
    with open('movies.txt','w') as movies_file:
        for movie in movies:
            movies_file.write(str(movie)+"\n")
        pass


#Test Function for Automated Testing. Saved in output.txt
def test():
    for choice in user_options.keys():
        print(MENU_PROMPT + choice)
        user_options[choice]()
    print(MENU_PROMPT + 'q')
    print("Saving File...")


if (__name__ == "__main__"):
    main()
    #Uncomment Test function to automate complete options
    #test()