from Pieces import *
from Players import *
from Win import *


class Board:  # This class is the game board itself, it contains all the necesary code fot the game to be playable, as
    # well as all the UI for the players during the game

    def __init__(self, player1, player2):  # This sets the basic data for the game, such as the locations in the screen
        # of all the necesary UI elements and other factors needed for the flow of the game such as turns and number of plays
        self.backcircle = [[315, 0], [205, 25], [111, 85], [47, 180], [25, 290], [47, 403], [111, 497], [205, 560],
                           [316, 582], [427, 560], [520, 497], [584, 403], [606, 290], [584, 180], [520, 85], [427, 25]]
        self.backboard = [(182, 158), (269, 158), (358, 158), (445, 158), (182, 245), (269, 245), (358, 245),
                          (445, 245),
                          (182, 334), (269, 334), (358, 334), (445, 334), (182, 420), (269, 420), (358, 420),
                          (445, 420)]
        self.moves = [[315, 0], [205, 25], [111, 85], [47, 180], [25, 290], [47, 403], [111, 497], [205, 560],
                      [316, 582], [427, 560], [520, 497], [584, 403], [606, 290], [584, 180], [520, 85], [427, 25]]
        self.box = [313, 718]
        self.matrix = [[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],
                       [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],
                       [[9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12]],
                       [[13, 13, 13, 13], [14, 14, 14, 14], [15, 15, 15, 15], [16, 16, 16, 16]]]
        self.tokens = []
        self.places = []
        self.buttons = []
        self.players = [player1, player2]
        self.scores = []
        self.background = pygame.image.load("Assets/TableroG.png")
        self.game = 0
        self.turn = False
        self.tk = False
        self.turns = 1

    def addtokes(self):  # This method creates all the pieces of the game, then add them to the list of pieces in the
        # game for later printing in the UI
        ima1 = pygame.image.load("Assets/ClaMarCirGra.png")
        piece1 = Token(ima1, True, True, True, True, 0, 0)
        self.tokens.append(piece1)

        ima2 = pygame.image.load("Assets/ClaMarCirPeq.png")
        piece2 = Token(ima2, True, True, True, False, 0, 0)
        self.tokens.append(piece2)

        ima3 = pygame.image.load("Assets/ClaMarCuaGra.png")
        piece3 = Token(ima3, True, True, False, True, 0, 0)
        self.tokens.append(piece3)

        ima4 = pygame.image.load("Assets/ClaMarCuaPeq.png")
        piece4 = Token(ima4, True, True, False, False, 0, 0)
        self.tokens.append(piece4)

        ima5 = pygame.image.load("Assets/ClaNoMCirGra.png")
        piece5 = Token(ima5, True, False, True, True, 0, 0)
        self.tokens.append(piece5)

        ima6 = pygame.image.load("Assets/ClaNoMCirPeq.png")
        piece6 = Token(ima6, True, False, True, False, 0, 0)
        self.tokens.append(piece6)

        ima7 = pygame.image.load("Assets/ClaNoMCuaGra.png")
        piece7 = Token(ima7, True, False, False, True, 0, 0)
        self.tokens.append(piece7)

        ima8 = pygame.image.load("Assets/ClaNoMCuaPeq.png")
        piece8 = Token(ima8, True, False, False, False, 0, 0)
        self.tokens.append(piece8)

        ima9 = pygame.image.load("Assets/OscMarCirGra.png")
        piece9 = Token(ima9, False, True, True, True, 0, 0)
        self.tokens.append(piece9)

        ima10 = pygame.image.load("Assets/OscMarCirPeq.png")
        piece10 = Token(ima10, False, True, True, False, 0, 0)
        self.tokens.append(piece10)

        ima11 = pygame.image.load("Assets/OscMarCuaGra.png")
        piece11 = Token(ima11, False, True, False, True, 0, 0)
        self.tokens.append(piece11)

        ima12 = pygame.image.load("Assets/OscMarCuaPeq.png")
        piece12 = Token(ima12, False, True, False, False, 0, 0)
        self.tokens.append(piece12)

        ima13 = pygame.image.load("Assets/OscNoMCirGra.png")
        piece13 = Token(ima13, False, False, True, True, 0, 0)
        self.tokens.append(piece13)

        ima14 = pygame.image.load("Assets/OscNoMCirPeq.png")
        piece14 = Token(ima14, False, False, True, False, 0, 0)
        self.tokens.append(piece14)

        ima15 = pygame.image.load("Assets/OscNoMCuaGra.png")
        piece15 = Token(ima15, False, False, False, True, 0, 0)
        self.tokens.append(piece15)

        ima16 = pygame.image.load("Assets/OscNoMCuaPeq.png")
        piece16 = Token(ima16, False, False, False, False, 0, 0)
        self.tokens.append(piece16)

    def gamenumber(self):  # This method checks the number of the game, meaning, it checks how many games have been
        # played before
        file = open("Leaderboards.txt")
        number = 0
        for line in file.readlines():
            number += 1
        self.game = number

    def addbuttons(self):  # This method cretes all the buttons in the game board, needed to move the pieces from the
        # waiting box to the board itself
        n = 1
        for places2 in self.backboard:
            back1 = pygame.image.load("Assets/fondo claro.png")
            back2 = pygame.image.load("Assets/fondo oscuro.png")
            fondo = Button(n, back1, back2, places2[0], places2[1])
            self.buttons.append(fondo)
            n += 1

    def addscores(self):  # This method creates the score counters for both of the players, usd to track the poins after
        #  each move
        for player in self.players:
            score = Counter(player)
            self.scores.append(score)

    def printer(self, places):  # This method creates the UI itself, incluidng all of the game objects, such as peices,
        # board buttons and texts used to display the statistics of the game. It also keeps track of every move each
        # player does, changing turns, scores and positions of graphic elements as needed
        ven = pygame.display.set_mode((700, 800))
        pygame.display.set_caption("Quarto")
        win1 = pygame.image.load("Assets/WInCla.png")
        win2 = pygame.image.load("Assets/WinOsc.png")
        winbutt = Button(0, win1, win2, 100, 715)
        back = pygame.image.load("Assets/fondo claro.png")
        cursor1 = Cursor()
        fuente = pygame.font.Font(None, 50)
        gameNumber = fuente.render("Game N°: " + str(self.game), 1, (141, 91, 72))

        for but in self.buttons:
            but.update(ven, cursor1)

        exiter = False
        while exiter == False:

            score1 = self.scores[0].name + ": " + str(self.scores[0].amount)
            score2 = self.scores[1].name + ": " + str(self.scores[1].amount)
            counter1 = fuente.render(score1, 1, (141, 91, 72))
            counter2 = fuente.render(score2, 1, (141, 91, 72))
            turn = " "
            if self.turn == False:
                turn = fuente.render("Turn " + str(self.turns) + ": " + self.players[0], 1, (141, 91, 72))
            elif self.turn == True:
                turn = fuente.render("Turn " + str(self.turns) + ": " + self.players[1], 1, (141, 91, 72))

            for place in self.backcircle:
                ven.blit(back, place)

            for butto in self.buttons:
                butto.update(ven, cursor1)

            ven.blit(self.background, (0, 0))
            ven.blit(counter1, (400, 705))
            ven.blit(counter2, (400, 740))
            ven.blit(gameNumber, (75, 675))
            ven.blit(turn, (400, 675))
            winbutt.update(ven, cursor1)

            i = 0
            for num in places:
                self.tokens[i].rect.left = self.moves[num - 1][0]
                self.tokens[i].rect.top = self.moves[num - 1][1]
                ven.blit(self.tokens[i].image, (self.moves[num - 1][0], self.moves[num - 1][1]))
                i += 1

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    exiter = True
                if evento.type == MOUSEBUTTONDOWN:
                    for piece in self.tokens:
                        if self.tk == False:
                            if cursor1.colliderect(piece):
                                if (piece.rect.left, piece.rect.top) not in self.backboard:
                                    j = (places[(piece.setpos(piece, self.tokens))] - 1)
                                    self.moves[j] = self.box
                                    self.tk = True
                                    if self.turn == False:
                                        self.turn = True
                                    elif self.turn == True:
                                        self.turn = False
                    for butt in self.buttons:
                        if self.tk == True:
                            if cursor1.colliderect(butt):
                                if butt.used == False:
                                    self.moves[j] = [butt.rect.left, butt.rect.top]
                                    r = 0
                                    while r < len(self.matrix):
                                        c = 0
                                        while c < len(self.matrix[r]):
                                            if self.matrix[r][c][0] == butt.number:
                                                p = 0
                                                while p < len(self.tokens):
                                                    if [self.tokens[p].rect.left, self.tokens[p].rect.top] == self.box:
                                                        self.matrix[r][c] = self.tokens[p].getchara()
                                                    p += 1
                                            c += 1
                                        r += 1
                                    if self.turn == False:
                                        self.scores[1].modpoint(3)
                                        self.scores[1].plays += 1
                                    else:
                                        self.scores[0].modpoint(3)
                                        self.scores[0].plays += 1
                                    butt.used = True
                                    self.turns += 1
                                    self.tk = False
                    if cursor1.colliderect(winbutt):
                        checker = Wincheck(self.matrix)
                        win = checker.Winhor()
                        if win[0] == True:
                            if self.turn == False:
                                self.scores[1].modpoint(self.scores[1].amount)
                                self.scores[1].savescores(self.scores[0].name, self.scores[1].name,
                                                          self.scores[0].amount, self.scores[0].plays, self.turns,
                                                          self.game)
                                checker.Winscreen(self.players[0], win[1], win[2], win[3], win[4], win[5])
                                pygame.display.set_mode((500, 500))
                                return
                            else:
                                self.scores[0].modpoint(self.scores[0].amount)
                                self.scores[0].savescores(self.scores[1].name, self.scores[0].name,
                                                          self.scores[1].amount, self.scores[1].plays, self.turns,
                                                          self.game)
                                checker.Winscreen(self.players[1], win[1], win[2], win[3], win[4], win[5])
                                pygame.display.set_mode((500, 500))
                                return
                        else:
                            if self.turns == 16:
                                checker.Drawscreen()

                            else:
                                if self.turn == False:
                                    if self.scores[1].amount > 1:
                                        self.scores[1].modpoint(-2)
                                    elif self.scores[1].amount == 1:
                                        self.scores[1].amount = 0
                                else:
                                    if self.scores[0].amount > 0:
                                        self.scores[0].modpoint(-2)
                                    elif self.scores[0].amount == 1:
                                        self.scores[0].amount = 0
            cursor1.update()
            pygame.display.update()
        pygame.quit()
        sys.exit()
