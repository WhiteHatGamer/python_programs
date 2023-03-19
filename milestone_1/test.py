test_dict = [
    {"title" : "The Shawshank Redemption", "year":1994, "genre":("Drama", ), "director":"Frank Darabont"},
    {"title" : "The Godfather", "year":1972, "genre":("Crime", "Drama"), "director":"Francis Ford Coppola"}
]
MOVIE_TEMPLATE = {'title' : str, 'year':int, 'genre': tuple, 'director':str}


def display():
    for i in test_dict:
        display_movie(i)


def display_movie(movie):
    print("")
    for key in list(MOVIE_TEMPLATE.keys()):
        if MOVIE_TEMPLATE[key]==tuple:
            tuple_string = ', '.join(movie[key])
            print(f"\t{key.title()}\t: {tuple_string}")
            continue
        print(f"\t{key.title()}\t: {movie[key]}")
    pass


#def display_movie(movie):
#    print(f"""
#    Title    : {movie['title']}
#    Year     : {movie['year']}
#    Genre    : {movie['genre']}
#    """)
#    pass
 
# accessing 2nd element using keys()
print("Movie Properties: " + ", ".join(list(MOVIE_TEMPLATE.keys())).title())



#prop_dict = {}
#for key in list(test_dict[0].keys()):
#    if(type(test_dict[0][key])==type(tuple())):
#        prop_dict.update({key:input(f"Enter Movie {key.title()}(seperated by comma','): ").title()})
#        prop_dict[key] = tuple(prop_dict[key].split(","))
#        continue    
#    prop_dict.update({key:input(f"Enter Movie {key.title()}: ").title()})
#test_dict.append(prop_dict)
#num = int(325)
#print(int())
#hello = "aeg"
#prop_dict = {}
#for key in list(MOVIE_TEMPLATE.keys()):
#    #checking if property is multiple as MOVIE_TEMPLATE
#    if(MOVIE_TEMPLATE[key] == tuple):
#        prop_dict.update({key:input(f"Enter Movie {key.title()}(seperated by comma','): ").title()})
#        prop_dict[key] = tuple(prop_dict[key].split(","))
#        continue
#    prop_dict.update({key:MOVIE_TEMPLATE[key](input(f"Enter Movie {key.title()}: ").title())})
#test_dict.append(prop_dict)
display()