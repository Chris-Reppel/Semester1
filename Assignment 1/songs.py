"""
Chris Reppel
Due Date: 9/4/20
Songs to Learn 1.0
"""

MENU = """Menu:
L - List songs
A - Add a new Song
C - Complete a Song
Q - Quit"""


def main():
    print("Songs to Learn 1.0 - by Chris Reppel")
    song_list = load_songs()
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "L":
            list_songs(song_list)
        elif user_choice == "A":
            add_new_song(song_list)
        elif user_choice == "C":
            print('Enter the number of a song to mark as learned')
            check_unlearned_song(song_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        user_choice = input(">>> ").upper()
    save_songs(song_list)
    print("Have a nice day :)")


def load_songs():
    song_list = []
    for song in open('songs.csv', 'r'):
        song = song.rstrip('\n').split(",")
        song_list.append(song)
    for song in song_list:
        song[2] = int(song[2])
    print('{} songs loaded from songs.csv'.format(len(song_list)))
    return song_list


def list_songs(song_list):
    unlearned_songs = 0
    longest_title = 0
    longest_artist = 0
    song_index = 0

    for song in song_list:
        if len(song[0]) > longest_title:
            longest_title = len(song[0])
        if song[3] == 'u':
            unlearned_songs += 1
        if len(song[1]) > longest_artist:
            longest_artist = len(song[1])
    for song in song_list:
        print(("*" if (song[3] is 'u') else " "), " {}.".format(song_index), song[0],
              " " * (longest_title - len(song[0])), "-", song[1], " " * (longest_artist - len(song[1])),
              "({})".format(song[2]))
        song_index += 1
    if unlearned_songs == 0:
        print("No more songs to learn!")
    else:
        print(song_index - unlearned_songs, "songs learned,", unlearned_songs, "songs still to learn")


def add_new_song(song_list):
    title = record_user_input("Title: ")
    artist = record_user_input("Artist: ")
    year = record_user_input("Year: ")
    new_song = [title, artist, year, 'u']
    song_list.append(new_song)
    print(title, 'by', artist, '({})'.format(year), 'added to song list')


def record_user_input(input_type):
    if input_type == "Year: " or input_type == 'song_index':
        data_type = int
    else:
        data_type = str
    if input_type == 'song_index':
        input_type = '>>>'
    user_input = input("{}".format(input_type))
    while verify_user_input(user_input, data_type) == 0:
        user_input = input("{}".format(input_type))
    if data_type == int:
        user_input = int(user_input)
    return user_input


def verify_user_input(user_input, data_type):
    if data_type == str:
        if not user_input.strip():
            print("Input can not be blank")
            return False
        else:
            return True
    else:
        try:
            user_input = int(user_input)
            if user_input < 0:
                print("Number must be >= than 0")
                return False
            else:
                return True
        except ValueError:
            print("Invalid input; enter a valid number")
            return False


def check_unlearned_song(song_list):
    unlearned = 0
    for song in song_list:
        if song[3] == 'u':
            unlearned += 1
            check_learned_song(song_list)
            break
    if unlearned == 0:
        print("No songs left to learn!")


def check_learned_song(song_list):
    user_input = record_user_input('song_index')
    if user_input > len(song_list) - 1:
        print('Invalid song number')
        check_learned_song(song_list)
    elif song_list[user_input][3] == 'l':
        print('You have already learned', song_list[user_input][0])
    else:
        print(song_list[user_input][0], "by", song_list[user_input][1], " learned")
        song_list[user_input][3] = 'l'


def save_songs(song_list):
    for song in song_list:
        song[2] = str(song[2])
    output_file = open('songs.csv', 'w')
    for song in song_list:
        print(','.join(song), file=output_file)
    output_file.close()
    print(len(song_list), " songs saved to songs.csv")


main()

