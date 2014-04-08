import pygame

class PygameWrapper(object):

	def __init__(self, width_, height_, title_):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screenWidth = width_
		self.screenHeight = height_
		self.screen = pygame.display.set_mode((width_, height_))
		pygame.display.set_caption(title_)
		

	def close():
		print("closing...")
		pygame.quit()
