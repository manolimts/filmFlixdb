from filmConnection import *

def update_films():
    filmdbCon = sql.connect('PYTHON PROJECT/filmFlix.db')
    filmdbCursor = filmdbCon.cursor()

    filmId = input("UPDATE FILM No.: ")
    userField = input("What field do you want to change?: ")
    userValue = input("Type the updated value: ")

    if userField == "yearReleased":
        userValue = int(userValue)
    elif userField == "duration":
        userValue = int(userValue)
    else:
        userValue = str(userValue)



    filmdbCursor.execute(
        f"UPDATE tblFilms SET '{userField}' = '{userValue}' WHERE filmID = '{filmId}'"
    )
    filmdbCon.commit()

if __name__ == "__main__":
    update_films()
