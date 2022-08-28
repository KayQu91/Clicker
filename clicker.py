import pygame
import random
import math

# Define Screen and initialize pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Globals
clock = pygame.time.Clock()

# Color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
target_color = (r, g, b)


# draw target as circle
target_x = random.randint(20, width - 20)
target_y = random.randint(20, height - 20)
target_width = random.randint(14, 20)
target = pygame.draw.circle(screen, target_color, (target_x, target_y), target_width)

# main Loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]

	click = pygame.mouse.get_pressed()
	sq_x = (x - target_x)**2
	sq_y = (y - target_y)**2

	if math.sqrt(sq_x + sq_y) < target_width and click[0] == 1:
		target_x = random.randint(20, width - 20)
		target_y = random.randint(20, height - 20)
		target_width = random.randint(14, 20)
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		target_color = (r, g, b)
		target = pygame.draw.circle(screen, target_color, (target_x, target_y), target_width)


	pygame.display.update()
	clock.tick(144)