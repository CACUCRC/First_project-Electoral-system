class Counter:  # This clas is used to create the scores for the players, as well as save the outcomes of every finished
    #  game
    def __init__(self, play):  # Defines the basic attributes of the class, such as the name of the player, the points
        # they have and the moves they have made
        self.name = play
        self.amount = 0
        self.plays = 0
        self.save = "Leaderboards.txt"

    def modpoint(self, mod):  # Changes the amount of points the player has
        self.amount += mod

    def savescores(self, winner, losser, score, moves, turns, numgame):  # Saves the statistics of each finished game,
        # to be viewable in the history or leaderboads screen
        file = open(self.save, "a")
        file.write(winner + "/" + losser + "/" + str(score) + "/" + str(moves) + "/" + str(turns) + "/" + str(
            numgame) + "/" + "\n")
