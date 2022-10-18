import sqlite3

da_base = sqlite3.connect('songs.db')
cur = da_base.cursor()

da_base.close()
