import sqlite3 as sql

# Create a new SQLite database or connect to an existing one
filmdbCon = sql.connect("PYTHON PROJECT/filmFlix.db")

# create a variable dbcursor and initialise it with the cursor method
filmdbCursor = filmdbCon.cursor()




