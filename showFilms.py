from filmConnection import *
def getFilms():
    filmdbCursor.execute("SELECT * FROM tblfilms")

    allRecords = filmdbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

if __name__== "__main__":
    print("-----LIST OF ALL FILMS-----")
    getFilms()