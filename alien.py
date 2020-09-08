import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  def __init__(self, ai_game):
    super().__init__()
    self.screen = ai_game.screen

    image = pygame.image.load('images/ufo_ship.png')

    self.image = pygame.transform.scale(image, (50, 25))
    self.rect = self.image.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.x = float(self.rect.x)

