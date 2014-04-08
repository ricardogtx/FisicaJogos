import pygame

class Sprite(object):

	def __init__(self, path_):
		self.image = pygame.image.load(path_)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
