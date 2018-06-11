import sys
from pygame.locals import *
from Buttons import *
from Cursors import *


class Wincheck:  # This class is used to check the game every time the players press the "Win" button, it determines
    # weather or not a winning play has been made and acts accordingly. Should a player have won, it sets the winnihg
    # sreen, or should a draw take place, it shows the draw screen
    def __init__(self, matriz):
        self.check = matriz

    def Winhor(self):  # This method is used to determine wether or not the game has been won, it if has, it returns the
        #  row/column/diagonal in wich the winnig play took place and the reason why it was a valid winig play
        #  (the characteristic of the pieces that won the line)
        x = ''
        y = ''
        row = ''
        colum = ''
        line = ''
        win = False
        c = 0
        while c < 4:
            i = 0
            while i < len(self.check):
                j = 0
                while j < len(self.check[i]):
                    r = 0
                    while self.check[i][r][c] == True and r < 4:
                        r += 1
                        if r == 4:
                            win = True
                            x = c
                            row = i
                            break
                    j += 1
                i += 1
            c += 1
        c = 0
        while c < 4:
            g = 0
            while g < len(self.check):
                n = 0
                while self.check[n][g][c] == True and n < 4:
                    n += 1
                    if n == 4:
                        win = True
                        x = c
                        colum = g
                        break
                g += 1
            c += 1
        c = 0
        while c < 4:
            f = 0
            while self.check[f][f][c] == True and f < 4:
                f += 1
                if f == 4:
                    win = True
                    x = c
                    line = 0
                    break
            c += 1
        c = 0
        while c < 4:
            if self.check[0][3][c] == True:
                if self.check[1][2][c] == True:
                    if self.check[2][1][c] == True:
                        if self.check[3][0][c] == True:
                            win = True
                            x = c
                            line = 1

            c += 1
        b = 0
        while b < 4:
            i = 0
            while i < len(self.check):
                j = 0
                while j < len(self.check[i]):
                    r = 0
                    while self.check[i][r][b] == False and r < 5:
                        r += 1
                        if r == 4:
                            win = True
                            y = b
                            row = i
                            break
                    j += 1
                i += 1
            b += 1
        b = 0
        while b < 4:
            g = 0
            while g < len(self.check):
                n = 0
                while self.check[n][g][b] == False and g < 5:
                    n += 1
                    if n == 4:
                        win = True
                        y = b
                        colum = b
                        break
                g += 1
            b += 1
        b = 0
        while b < 4:
            f = 0
            while self.check[f][f][b] == False and f < 5:
                f += 1
                if f == 4:
                    win = True
                    line = 0
                    y = b
                    break
            b += 1
        b = 0
        while b < 4:
            if self.check[0][3][b] == False:
                if self.check[1][2][b] == False:
                    if self.check[2][1][b] == False:
                        if self.check[3][0][b] == False:
                            win = True
                            line = 1
                            y = b
            b += 1
        return [win, x, y, row, colum, line]

    def Winscreen(self, player, x, y, row, colum, line):  # This method is used to display the winnig player, the line
        # where they won and why tey won, based on the data returned from the method that determines victories, players
        #  can also use this screen to return back to the  main menu as the game has ended
        ven = pygame.display.set_mode((500, 300))
        pygame.display.set_caption("Winner")
        fuente1 = pygame.font.Font(None, 75)
        win = fuente1.render("Winner: ", 1, (117, 78, 27))
        fuente2 = pygame.font.Font(None, 100)
        cursor1 = Cursor()
        back1 = pygame.image.load("Assets/BackCla.png")
        back2 = pygame.image.load("Assets/BackOsc.png")
        backbutt = Button(0, back1, back2, 10, 215)
        winner = fuente2.render(player, 1, (117, 78, 27))
        back = pygame.image.load("Assets/Menu.png")
        chara = " "
        winline = " "
        if x != '':
            if x == 0:
                chara = "Color: Clear"
            if x == 1:
                chara = "Mark: Marked"
            if x == 2:
                chara = "Shape: Cicles"
            if x == 3:
                chara = "Size: Big"
        elif y != '':
            if y == 0:
                chara = "Color: Dark"
            if y == 1:
                chara = "Mark: No Marked"
            if y == 2:
                chara = "Shape: Squares"
            if y == 3:
                chara = "Size: Small"
        if row != '':
            if row == 0:
                winline = "First Row"
            if row == 1:
                winline = "Second Row"
            if row == 2:
                winline = "Third Row"
            if row == 3:
                winline = "Fourth Row"
        if colum != '':
            if colum == 0:
                winline = "First Column"
            if colum == 1:
                winline = "Second Column"
            if colum == 2:
                winline = "Tird Column"
            if colum == 3:
                winline = "Fourth Column"
        if line != '':
            if line == 0:
                winline = "Shrinking Diagonal"
            if line == 1:
                winline = "Growing Diagonal"

        charact = fuente1.render(chara, 1, (117, 78, 27))
        winingline = fuente1.render(winline, 1, (117, 78, 27))

        exiter = False
        while exiter == False:

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exiter = True
                if evento.type == MOUSEBUTTONDOWN:
                    if cursor1.colliderect(backbutt):
                        return

            ven.blit(back, (0, -175))
            ven.blit(win, (10, 10))
            ven.blit(winner, (10, 50))
            ven.blit(charact, (10, 110))
            ven.blit(winingline, (10, 150))
            backbutt.update(ven, cursor1)
            cursor1.update()
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def Drawscreen(self):  # This method creates the sceen for when the game ends in a drawm, giving the players the
        # option to go back to the main menu
        ven = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("Draw")
        fuente1 = pygame.font.Font(None, 75)
        draw = fuente1.render("Draw", 1, (117, 78, 27))
        back1 = pygame.image.load("Assets/BackCla.png")
        back2 = pygame.image.load("Assets/BackOsc.png")
        backbutt = Button(0, back1, back2, 10, 115)
        cursor1 = Cursor()
        back = pygame.image.load("Assets/Menu.png")
        exiter = False
        while exiter == False:

            ven.blit(back, (-290, -290))
            ven.blit(draw, (10, 10))
            backbutt.update(ven, cursor1)
            cursor1.update()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exiter = True
                if evento.type == MOUSEBUTTONDOWN:
                    if cursor1.colliderect(backbutt):
                        return
            pygame.display.update()
        pygame.quit()
        sys.exit()
