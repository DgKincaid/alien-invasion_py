"""Test Doc string"""

import sys

import pygame

from game_settings import GameSettings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

  """Overall class for alien Invasion"""

  def __init__(self):
    pygame.init()
    self.settings = GameSettings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    # self.settings.screen_width = self.screen.get_rect().width
    # self.settings.screen_height = self.screen.get_rect().height

    pygame.display.set_caption('Alien Invasion')

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()

    self._create_fleet()

  def run_game(self):

    """ Run game function """
    while True:

      self._check_events()
      self.ship.update()

      self._update_bullets()

      self._update_screen()


  def _create_fleet(self):
    alien = Alien(self)

    alien_width = alien.rect.width
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2*alien_width)

    for alien_number in range(number_aliens_x):
      alien = Alien(self)
      alien.x = alien_width + 2 * alien_width * alien_number
      alien.rect.x = alien.x
      self.aliens.add(alien)

  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup(event)

  def _check_keydown(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()

  def _check_keyup(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _fire_bullet(self):
    if(len(self.bullets) < 3):
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)


  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    for bullet in self.bullets.sprites():
      bullet.draw_bullet()

    self.aliens.draw(self.screen)
    pygame.display.flip()

  def _update_bullets(self):
    self.bullets.update()

    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

if __name__ == '__main__':
  print('main')
  ai = AlienInvasion()
  ai.run_game()

print('test')