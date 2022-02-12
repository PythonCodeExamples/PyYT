DB_NAME = "follows.db"

SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS follows (name TEXT, path TEXT)
"""

SQL_INSERT_NEW_CHANNEL = """
INSERT INTO follows VALUES (?, ?)
"""

SQL_SELECT_CHANNELS = """
SELECT name FROM follows
"""
SQL_DELETE_CHANNEL = """
DELETE FROM follows WHERE name=?
"""

SQL_SELECT_LINK = """
SELECT path FROM follows WHERE name=?
"""