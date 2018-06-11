import pygame


class Cursor(pygame.Rect):  # This class is used to created cursors in the game, that correspond to the cursor of the
    # computer, this to allow the user to interact with the elements of the UI
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):  # Constaly alignes the cursor with the computers cursor, so the player can have areal time
        # interaction with the UI
        self.left, self.top = pygame.mouse.get_pos()
