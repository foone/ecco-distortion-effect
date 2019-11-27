import pygame, sys
from pygame.locals import *
from generate import generate_for_offset

pygame.init()

windowSurface = pygame.display.set_mode((320, 224), 0, 32)
pygame.display.set_caption('Eccotime')
background = pygame.image.load('background.png').convert()

def draw(frame):
	adjusts = generate_for_offset(frame)
	for y in range(224):
		x=adjusts[y]
		windowSurface.blit(background, (-x,y), (0,y,384,1))
	pygame.display.update()

clock = pygame.time.Clock()

frame_count=0
while True:
	draw(frame_count)
	frame_count+=1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	clock.tick_busy_loop(60)