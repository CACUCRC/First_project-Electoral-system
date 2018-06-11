from tkinter import *
from MainMenu import Menu, num


def Open(play, text1, text2):  # This method opens the window where the user can input the names of the players
    play.withdraw()
    player1 = text1.get()
    player2 = text2.get()
    Game = Menu()
    Game.menu(player1, player2, )


def Quarto():  # This method defines the characteristics of the winddow that is used to input the names of the players
    window = Tk()
    window.geometry("500x100+100+100")
    window.title("Players")
    user = Label(text="Player 1: ", font=("SHOWCARD GOTHIG", 15)).place(x=10, y=10)
    entry = StringVar()
    BoxText = Entry(window, textvariable=entry).place(x=100, y=17)
    user2 = Label(text="Player 2: ", font=("SHOWCARD GoTHIG", 15)).place(x=10, y=40)
    entry2 = StringVar()
    BoxText2 = Entry(window, textvariable=entry2).place(x=100, y=47)
    quarto = Button(window, text="Launch", command=lambda: Open(window, entry, entry2),
                    font=("SHOWCARD GOTHIG", 15)).place(x=300, y=20)
    window.mainloop()


Quarto()
