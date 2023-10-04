from filmConnection import *

# Create a films table
filmdbCursor.execute('''
    CREATE TABLE IF NOT EXISTS tblfilms(
        FilmId INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        yearReleased INTEGER,
        Rating TEXT,
        Duration INTEGER,
        Genre TEXT
    )
''')

# Commit changes and close the connection
filmdbCon.commit()
filmdbCon.close()

