from commands.base_command import BaseCommand
from pymongo import MongoClient
from pprint import pprint

import sqlite3
import dbConnect

#client = MongoClient("mongodb+srv://Admin:Yseb4mas@cluster0.a5nzn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client.admin

#serverStatusResult=db.command("listDatabases")



class Connect(BaseCommand):

    def __init__(self):
        description = "Connects to the Database"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        from message_handler import COMMAND_HANDLERS
        msg = message.author.mention + "\n"

        # Displays all descriptions, sorted alphabetically by command name
        dbConnect.connect_and_creating_table()

        msg = "test"

        await message.channel.send(msg)