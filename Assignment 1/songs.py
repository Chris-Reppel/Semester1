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

import csv


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
            list_songs(song_list)
            print('Enter the number of a song to mark as learned')
            check_learnt_song(song_list)
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
    unlearnt_songs = 0
    longest_title = 0
    longest_artist = 0
    song_index = 1

    for song in song_list:
        if len(song[0]) > longest_title:
            longest_title = len(song[0])
        if song[3] == 'u':
            unlearnt_songs += 1
        if len(song[1]) > longest_artist:
            longest_artist = len(song[1])
    for song in song_list:
        print(("*" if (song[3] is 'u') else " "), " {}.".format(song_index), song[0],
              " " * (longest_title - len(song[0])), "-", song[1], " " * (longest_artist - len(song[1])),
              "({})".format(song[2]))
        song_index += 1
    song_total = song_index - 1
    if unlearnt_songs == 0:
        print("No more songs to learn!")
    else:
        print(song_total - unlearnt_songs, "songs learned,", unlearnt_songs, "songs still to learn")


main()

