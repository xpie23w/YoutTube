'''
Provided to YouTube by Triple Vision Record Distribution

My World (Original) · Noisia

Split the Atom (Special Edition)

℗ Vision Recordings

Released on: 2012-04-09

Artist: Noisia

Auto-generated by YouTube.
------
Provided to YouTube by Triple Vision Record Distribution

Alpha Centauri · Noisia

Split the Atom (Special Edition)

℗ Vision Recordings

Released on: 2012-04-09

Artist: Noisia

Auto-generated by YouTube.

'''
import pygame
import sys

GAME = True
frame = pygame.display.set_mode([640, 420])

pygame.init()

tiles = []

x = 0
y = 0

player_img = pygame.image.load("sprite1.png")
player_img = pygame.transform.scale(player_img, (40, 40))

obj_rect = pygame.Rect(100, 100, 40, 40)

tiles.append(obj_rect)

class Player:
	def __init__(self):
		self.img = pygame.image.load("sprite.png")
		self.img = pygame.transform.scale(self.img, (40, 40))
		self.rect = pygame.Rect(0, 0, 40, 40)
		pass

	def render(self, Frame):
		Frame.blit(self.img, [self.rect.x, self.rect.y])
		pass

	def move(self, vx, vy):
		if vx != 0:
			self.rect.x += vx
		if vy !=0 :
			self.rect.y += vy

		self.bumped(vx, vy)
		pass

	def bumped(self, vx, vy):
		for tile in tiles:
			if self.rect.colliderect(tile):
				if vx > 0:
					self.rect.right = tile.left
				if vx < 0:
					self.rect.left = tile.right
				if vy > 0:
					self.rect.bottom = tile.top
				if vy < 0:
					self.rect.top = tile.bottom
		pass

player = Player()

while GAME:
	frame.fill((0,0,0))
	k = pygame.key.get_pressed()
	player.render(frame)
	rect = frame.blit(player_img, [obj_rect.x, obj_rect.y])

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			GAME = False
			sys.exit()
	if k[pygame.K_LEFT]:
		player.move(-1, 0)
	if k[pygame.K_RIGHT]:
		player.move(1, 0)
	if k[pygame.K_UP]:
		player.move(0, -1)
	if k[pygame.K_DOWN]:
		player.move(0, 1)

	pygame.display.flip()
