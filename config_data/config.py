import os
from dotenv import load_dotenv, find_dotenv


"""Checking environment variable"""

if not find_dotenv():
    exit('The variable of virtual environment have not been found')
else:
    load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
# some_other_api too

TUPLE_OF_COMMANDS = (
    ('start', "Launch bot"),
    ('help', "Send help")
)
