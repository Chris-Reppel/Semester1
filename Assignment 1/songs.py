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
            list_songs(songs_list)
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
    return  song_list


def list_songs(song_list):


main()

