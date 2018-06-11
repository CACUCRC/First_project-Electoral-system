class Button:  # This class is used for the button in the diferent screens, used to choose options from the menus or
    # place pieces in the game boards
    def __init__(self, number, image1, image2, x=150, y=160, full=False):  # Defines the basic characteristics of the
        # uttons, such as the images the used in the UI or their ability to detect when tey are being pressed
        self.normal = image1
        self.select = image2
        self.number = number
        self.actual = self.normal
        self.used = full
        self.rect = self.actual.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, pantalla, cursor):  # Makes the buttons constantly check if there is a cursor over them, so they
        # react accordingly
        if cursor.colliderect(self.rect):
            self.actual = self.select
        else:
            self.actual = self.normal
        pantalla.blit(self.actual, self.rect)
