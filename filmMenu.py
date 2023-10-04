#  CRUD:   CREATE      READ     UPDATE      DELETE
from filmConnection import *
import filmReports 
import addFilm  
import deleteFilms  
import updateFilms  
import showFilms 

def get_filmMenu_file():
    with open("PYTHON PROJECT/filmsMenu.txt", "r") as mainMenu:
        readMenuContents = mainMenu.read()
    return readMenuContents

def get_film_reportMenu():
    with open("PYTHON PROJECT/filmReports.txt") as menuReportFile:
        reportMenuContents = menuReportFile.read()
    return reportMenuContents

def display_film_report_menu():
    reportMenuChoice = get_film_reportMenu()
    print(reportMenuChoice)
    return input("Enter an option from the Film Report Menu above: ")

def film_menu():
    option = 0
    optionList = ["1", "2", "3", "4", "5", "6"]

    filmMenuChoice = get_filmMenu_file()

    while option not in optionList:
        print(filmMenuChoice)

        option = input("Enter an option from the Films Menu Above!: ")
        if option not in optionList:
            print(f"{option} is not a valid choice in the Films Menu")

    if option == "5":
        reportOption = display_film_report_menu()

        
        if reportOption == "1":
            filmReports.get_filmReportAll()
            input("Press ENTER to go back to REPORTS MENU: ")

        elif reportOption == "2":
            filmReports.get_reportGenreChoice()
            input("Press ENTER to go back to REPORTS MENU: ")

        elif reportOption == "3":
            filmReports.get_reportYearChoice()
            input("Press ENTER to go back to REPORTS MENU: ")

        elif reportOption == "4":
            filmReports.get_reportRatingChoice()
            input("Press ENTER to go back to REPORTS MENU: ")

        else:
            print("Go back to Main Menu")
            
    return option

mainFilmProgram = True

while mainFilmProgram:

    mainFilmsMenu = film_menu()

    if mainFilmsMenu == "1":
        addFilm.add_films()
        input("Press ENTER to go back to MAIN MENU: ")

    elif mainFilmsMenu == "2":
        deleteFilms.delete_film()
        input("Press ENTER to go back to MAIN MENU: ")

    elif mainFilmsMenu == "3":
        updateFilms.update_films()
        input("Press ENTER to go back to MAIN MENU: ")

    elif mainFilmsMenu == "4":
        showFilms.getFilms()
        input("Press ENTER to go back to MAIN MENU: ")

    elif mainFilmsMenu == "5":
        pass 

    else:
        input("Press Enter if you want to exit the Program")
        filmdbCon.close()

if __name__ == "__main__":
    get_filmMenu_file()

    