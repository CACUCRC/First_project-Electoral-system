class Token:  # This class coresponds with the pieces of the game, it contains their atributes as pieces, as well as
    # allows them to detect when a player has selected them
    def __init__(self, image, color, mark, shape, size, x, y):  # Defines the attributes of the pieces ( as used in the
        # game), as well as the place where they are printed
        self.image = image
        self.color = color
        self.size = size
        self.shape = shape
        self.mark = mark
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def getchara(self):  # This method returns the characteristic of the pieces, needed to check every winnig play
        return [self.color, self.mark, self.shape, self.size]

    def setpos(self, pieza, tokens):  # Moves the position of the piece to the winting box in the game board, meaning
        # that the piece has been selected to be sed in the next move
        i = 0
        while i < len(tokens):
            if pieza == tokens[i]:
                self.rect.left = 313
                self.rect.top = 718
                return i
            i += 1
