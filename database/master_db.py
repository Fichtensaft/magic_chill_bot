import sqlite3
import os
from db_funcs import sorting_hat

da_base = sqlite3.connect('songs.db')
cur = da_base.cursor()

# cur.execute("""CREATE TABLE kaj_songs (
# id integer PRIMARY KEY,
# a_song TEXT,
# blue_button BOOLEAN NOT NULL CHECK (blue_button IN (0, 1)),
# red_button BOOLEAN NOT NULL CHECK (red_button IN (0, 1)),
# green_button BOOLEAN NOT NULL CHECK (green_button IN (0, 1)),
# orange_button BOOLEAN NOT NULL CHECK (orange_button IN (0, 1)),
# violet_button BOOLEAN NOT NULL CHECK (violet_button IN (0, 1)),
# pink_button BOOLEAN NOT NULL CHECK (pink_button IN (0, 1)),
# pot_button BOOLEAN NOT NULL CHECK (pink_button IN (0, 1)),
# count_button BOOLEAN NOT NULL CHECK (pink_button IN (0, 1)),
# black_button BOOLEAN NOT NULL CHECK (black_button IN (0, 1))
#
# )""")


# cur.execute("""CREATE TABLE stat_songs (
# song_tab TEXT PRIMARY Key,
# blue_button integer DEFAULT 0,
# red_button integer DEFAULT 0,
# green_button integer DEFAULT 0,
# orange_button integer DEFAULT 0,
# violet_button integer DEFAULT 0,
# pink_button integer DEFAULT 0,
# pot_button integer DEFAULT 0,
# count_button integer DEFAULT 0,
# black_button integer DEFAULT 0
#
# )""")

cur.execute("""INSERT INTO stat_songs (song_tab) VALUES ('kaj_songs')""")


#
# with open(r'C:\Me\Coding\КняZz\count_songs.txt', 'r', encoding='utf-8') as songs_file:
#     songs = songs_file.readlines()
#     for i_song in songs:
#         format_song = i_song.rstrip('\n')
#         format_song = 'КняZz - ' + format_song
#
#         insertion = """INSERT INTO kaj_songs
#                    (a_song, blue_button, red_button, green_button, orange_button, violet_button, pink_button, pot_button, count_button, black_button)
#                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
#         button_tuple = (format_song, True, False, False, False, False, False, False, True, False)
#
#         cur.execute(insertion, button_tuple)
#         da_base.commit()
#
# sorting_hat(songs_list=songs, db_connection=da_base, db_cursor=cur)

da_base.commit()

# req = """SELECT a_song FROM kaj_songs WHERE black_button=1 ORDER BY RANDOM() LIMIT 1"""
# exec = cur.execute(req)
# print(exec.fetchall()[0][0])

da_base.close()
