music = []
"""
    {"title" : "Star Boy", "genre":"international","year":2023,"artists":("blinding lights")}
    {"title" : "Bones", "genre":"international","year":2022,"artists":("Imagine Dragons")}
"""
with open("music.txt",'r') as music_file:
    for song in music_file:
        music.append(eval(song))

MENU_PROMPT = "\n'a' to add Song\n'd' to Display Music\n's' to Search a song\n'q' to Quit\nEnter Your Choice: "

def add_song():
    title = input("Enter Music title: ").title()
    genre = input("Enter Music genre: ").title()
    year = input("Enter Released Year: ")
    artists = input("Enter Artists (seperated by comma','): ").title()
    if ',' in artists:
        artists = tuple(artists.split(","))

    music.append({
        "title": title,
        "genre":genre,
        "year":year,
        "artists":artists 
    })
    pass


def display():
    for song in music:
        display_song(song)
    pass


def display_song(song):
    print(f"""
    Title   : {song['title']}
    Genre   : {song['genre']}
    Year    : {song['year']}
    Artists : {song['artists']}
    """)
    pass


def find_song():
    print(music[0].keys())
    find_key = input("What property of Song you looking for: ")
    if find_key not in music[0].keys():
        print("Invalid term")
        return
    find_term = input("What are you searching for: ")
    find_term = find_term.lower().replace(" ","")
    found_flag = True
    for song in music:
        if song[find_key].lower().replace(" ","")==find_term:
            print(f"\nSong Found:")
            display_song(song)
            found_flag = False
            continue
    if found_flag:
        print("Song not found")
    pass


user_options = {
    'a':add_song,
    'd':display,
    's':find_song
}


def main():
    while(True):
        choice = input(MENU_PROMPT)
        if choice in user_options.keys():
            user_options[choice]()
        elif choice == 'q':
            break
        else:
            print("Invalid Choice")
    with open('music.txt','w') as music_file:
        for song in music:
            music_file.write(str(song)+"\n")
        pass


if (__name__ == "__main__"):
    main()