from filmConnection import *
import sqlite3 as sql 

def add_films():
    filmdbCon = sql.connect('PYTHON PROJECT/filmFlix.db')
    filmdbCursor = filmdbCon.cursor()

    filmTitle = input("Enter a Film Title: ")
    filmYearReleased = input("Enter Release Year: ")
    filmRating = input("Enter Film rating: ")
    filmDuration = input("Enter Film duration time: ")
    filmGenre = input("Enter Film Genre: ")

    filmdbCursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
                         (filmTitle, filmYearReleased, filmRating, filmDuration, filmGenre))
    filmdbCon.commit()
    print(f"{filmTitle} inserted into the tblfilms table")

if __name__ == "__main__":
    add_films()
