from filmConnection import *

# Function to delete a film by ID
def delete_film():
       filmdbCon = sql.connect('PYTHON PROJECT/filmFlix.db')
       filmdbCursor= filmdbCon.cursor()
       deleteFilm = input("Type in the ID of film you want deleted: ")
       filmdbCursor.execute('DELETE FROM tblFilms WHERE FilmId = ?', (deleteFilm,))
       filmdbCon.commit()
       
       print(f"film no. {deleteFilm} is now deleted from the tblfilms table")


if __name__ == "__main__":
     delete_film()