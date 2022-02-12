from sqlite3 import connect as db_connect

from db_config import (
    DB_NAME,
    SQL_CREATE_TABLE, SQL_INSERT_NEW_CHANNEL,
    SQL_SELECT_CHANNELS, SQL_DELETE_CHANNEL,
    SQL_SELECT_LINK
)


class DBManager:
    def __init__(self):
        """ Opens database and cursor. """
        self.db = db_connect(DB_NAME)
        self.curs = self.db.cursor()
        self.curs.execute(SQL_CREATE_TABLE) # Create table if not exists

    
    def __del__(self):
        """ Closes database and cursor. """
        self.curs.close()
        self.db.close()


    def add_channel(self, name: str, ch_hash: str) -> None:
        """ Adds new channel into table. """
        self.curs.execute(SQL_INSERT_NEW_CHANNEL, (name, ch_hash))
        self.db.commit()
    

    def remove_channel(self, name: str) -> None:
        """ Removes channel from table by name. """
        self.curs.execute(SQL_DELETE_CHANNEL, (name,))
        self.db.commit()


    def show_channels(self) -> list:
        """ Returns list of tuples with channel's names. """
        self.curs.execute(SQL_SELECT_CHANNELS)
        return self.curs.fetchall()


    def get_channel_link(self, name: str) -> str:
        """ Returns URL to channel. """
        self.curs.execute(SQL_SELECT_LINK, (name,))
        return self.curs.fetchone()[0]