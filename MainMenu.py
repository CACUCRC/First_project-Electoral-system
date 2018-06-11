from Gameboard import *
from random import *
import pygame

num = 0


class Menu():  # This is the class used fot the main menu, it contains the necesary method to start a game, see the
    # leaderboards with the highest scores gotten by players and also check the history, which shows the outcomes(sta-
    # tistics) of all the games that have been played before
    def __init__(self):  # Defines the basic characteristics of the class, thus, the
        self.back = pygame.image.load("Assets/Menu.png")

    def menu(self, player1, player2):  # This method defines the window for the main menu tiself, with all the buttons
        # that go into it and what they do, it can be used to access the leaderboards or the history, or start a game
        pygame.init()
        ven = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Main Menu")
        play1 = pygame.image.load("Assets/PlayCla.png")
        play2 = pygame.image.load("Assets/PlayOsc.png")
        score1 = pygame.image.load("Assets/ScoCla.png")
        score2 = pygame.image.load("Assets/ScoOsc.png")
        history1 = pygame.image.load("Assets/HistoCla.png")
        history2 = pygame.image.load("Assets/HistoOsc.png")
        boton1 = Button(0, play1, play2, 150, 150)
        boton2 = Button(0, score1, score2, 125, 270)
        boton3 = Button(0, history1, history2, 125, 390)
        cursor1 = Cursor()
        places = []
        self.player1 = player1
        self.player2 = player2
        while len(places) < 16:
            num = randint(1, 16)
            while num in places:
                num = randint(1, 16)
            places.append(num)

        exiter = False
        while exiter == False:
            ven.fill((255, 255, 255))
            ven.blit(self.back, (0, 0))
            cursor1.update()
            boton1.update(ven, cursor1)
            boton2.update(ven, cursor1)
            boton3.update(ven, cursor1)
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton1.rect):
                        game = Board(self.player1, self.player2)
                        game.addtokes()
                        game.addbuttons()
                        game.addscores()
                        game.gamenumber()
                        game.printer(places)
                    if cursor1.colliderect(boton2):
                        leader = Menu()
                        leader.leaderboards(self.player1, self.player2)
                    if cursor1.colliderect(boton3):
                        history = Menu()
                        history.record(self.player1, self.player2)
                if evento.type == QUIT:
                    exiter = True
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def leaderboards(self, player1,
                     player2):  # This method makes up the leaderboards window, where the user can see the
        # highest scores and the player who got them, it also allows them to go back to the main menu
        ven1 = pygame.display.set_mode((300, 700))
        pygame.display.set_caption("Leaderboards")
        back1 = pygame.image.load("Assets/BackCla.png")
        back2 = pygame.image.load("Assets/BackOsc.png")
        fondo = pygame.image.load("Assets/leader.png")
        backbutt = Button(0, back1, back2, 75, 615)
        cursor1 = Cursor()
        fuente = pygame.font.Font(None, 50)
        exiter = False

        file1 = open("Leaderboards.txt", "r")
        pts = []
        for lines in file1.readlines():
            point = lines.split("/")
            point[6] = "0"
            pts.append(int(point[2]))
        pts.sort(reverse=True)
        file1.close()

        while exiter == False:
            ven1.blit(fondo, (0, 0))

            x = 30
            y = 100
            l = 0
            used = []
            while l < len(pts):
                file = open("Leaderboards.txt", "r")
                for line in file.readlines():
                    info = line.split("/")
                    if info[5] not in used:
                        if info[2] == str(pts[l]):
                            gamer = fuente.render(info[0] + ":... " + info[2], 1, (68, 75, 42))
                            used.append(info[5])
                            ven1.blit(gamer, (x, y))
                            y += 40
                    file.close()
                l += 1

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exiter = True
                if evento.type == MOUSEBUTTONDOWN:
                    if cursor1.colliderect(backbutt.rect):
                        main = Menu()
                        main.menu(player1, player2)

            backbutt.update(ven1, cursor1)
            cursor1.update()

            pygame.display.update()

        pygame.quit()
        sys.exit()

    def record(self, player1, player2):  # This method defines the history window, where the user can see the statistics
        # of all the games that have been played, including who won, who lost, the amount of turns the winner used and
        # the total turns that took place during the game. Users can go back to the main menu from here as well
        ven1 = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("History")
        back1 = pygame.image.load("Assets/BackCla.png")
        back2 = pygame.image.load("Assets/BackOsc.png")
        fondo = pygame.image.load("Assets/historial.png")
        backbutt = Button(0, back1, back2, 225, 515)
        cursor1 = Cursor()
        fuente = pygame.font.Font(None, 25)
        exiter = False

        while exiter == False:
            ven1.blit(fondo, (0, 0))

            y = 150
            file1 = open("Leaderboards.txt", "r")
            for lines in file1.readlines():
                point = lines.split("/")
                record = fuente.render(
                    "The player " + point[0] + " won the game #" + str(point[5]) + " against " + point[
                        1] + ", with " + str(point[3]) + " moves out of " + str(point[4] + "."), 1, (84, 48, 28))
                ven1.blit(record, (10, y))
                y += 20
            file1.close()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exiter = True
                if evento.type == MOUSEBUTTONDOWN:
                    if cursor1.colliderect(backbutt.rect):
                        main = Menu()
                        main.menu(player1, player2)

            backbutt.update(ven1, cursor1)
            cursor1.update()

            pygame.display.update()

        pygame.quit()
        sys.exit()
