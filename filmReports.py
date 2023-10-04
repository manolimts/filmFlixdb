from filmConnection import *


def get_filmReportAll():
    
    print("-----INFORMATION FROM ALL OUR FILMS-----")
    filmdbCursor.execute("SELECT * FROM tblFilms ORDER BY filmId ASC")
    allRecords = filmdbCursor.fetchall() 

    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    get_filmReportAll()


def get_reportGenreChoice():
    userGenreinput = input("Which genre are you looking for (Comedy, Action, Crime, Fantasy, Fighting or Animation): ")
    filmQuery = "SELECT * FROM tblFilms WHERE genre = ?"
    filmdbCursor.execute(filmQuery, (userGenreinput,))
    filmsByGenre = filmdbCursor.fetchall()

    if filmsByGenre:
        print(f"There are no other films of the genre '{userGenreinput}':")
    for film in filmsByGenre:
        print(film)
    else:
        print(f"No films found for the genre '{userGenreinput}'.")


if __name__ == "__main__":
    get_reportGenreChoice()




def get_reportYearChoice():
    userYearinput = input("Select a year of your choice: ")
    filmQuery2 = "SELECT * FROM tblFlms WHERE yearReleased = ?"
    filmdbCursor.execute(filmQuery2, (userYearinput,))
    filmsByYearReleased = filmdbCursor.fetchall()

    if filmsByYearReleased:
        print(f"These are the films of the year '{userYearinput}':")
    for film2 in filmsByYearReleased:
        print(film2)
    else:
        print(f"No films found for the year '{userYearinput}'.")


if __name__ == "__main__":
    get_reportYearChoice()



def get_reportRatingChoice():
    userRatinginput = input("Type what rating you'd want your film to be: ")
    filmQuery3 = "SELECT * FROM tblFilms WHERE rating = ?"
    filmdbCursor.execute(filmQuery3, (userRatinginput,))
    filmsByRating = filmdbCursor.fetchall()

    if filmsByRating:
        print(f"These are the films that are rated '{userRatinginput}':")
    for film2 in filmsByRating:
        print(film2)
    else:
        print(f"There are no other films that are rated '{userRatinginput}'.")


if __name__ == "__main__":
    get_reportRatingChoice()

    