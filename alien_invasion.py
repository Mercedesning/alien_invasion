import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.settings=Settings()

		self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width=self.screen.get_rect().width
		self.settings.screen_height=self.screen.get_rect().height
		self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasin")
		self.ship=Ship(self)


		""bullet""
		self.bullet_speed=1.0
		self.bullet_width=3
		self.bullst.height=5
		self.bullet_color=(60,60,60)

	def run_game(self):
		while True:
			self._check_evetns()
			self.ship.update()
			self._update_ecreen()


	def _check_evetns(self):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				elif event.type==pygame.KEYDOWN:
					self._ckeck_keydown_events(event)
				elif event.type==pygame.KEYUP:
					self._ckeck_keyup_events(event)			
	def _check_keydown_events(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=True
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False
		elif event.key==pygame.K_q:
			sys.exit()

	def _checkt_keyup_event(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=False
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False


	def _update_ecreen(self):
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			pygame.display.flip()

if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()

