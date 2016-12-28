#!/usr/bin/python2.7
import sys, pygame, random,  math
from Player import Player

boolean = True

pygame.init()

WIDTH  = 400
HEIGHT = 400


def get_placement_x():
	
	x = random.randint(0, math.floor(((WIDTH-15)/15)))

	return x * 15
	

def get_placement_y():
	y = random.randint(0, math.floor(((HEIGHT-15)/15)))

	return y * 15






windowSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek")


# colors
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
RED   = (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE  = (0  ,0  ,255)

# grid-like platingfield
space  = 15


# directions

# 1 - UP
# 2 - RIGHT
# 3 - DOWN
# 4 - LEFT
# random direction
rand_dir = random.randint(1, 4)
dirs = rand_dir

# PLAYER
# create snake head
startx = get_placement_x()
starty = get_placement_y()
snake = Player(startx, starty)



food_x = get_placement_x()
food_y = get_placement_y()

# score
score = 0



# clock for fps
clock = pygame.time.Clock()

def set_food():
	# set out random food
	food_x = get_placement_x()
	food_y = get_placement_y()

def game_over():
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)

	windowSurface.fill(BLACK)

	# create font
	myfont = pygame.font.SysFont("monospace", 40)
	play_again_font = pygame.font.SysFont("monospace", 30)

	# render text
	label = myfont.render("GAME OVER!", 1, GREEN)
	windowSurface.blit(label, (120, 100))

	label_2 = play_again_font.render("Press enter to play again!", 1, GREEN)
	windowSurface.blit(label_2, (80, 200))

	score_font = pygame.font.SysFont("monospace", 20)
	score_label = score_font.render("Score: " + str(score), 1, GREEN)
	windowSurface.blit(score_label, (180, 250))

def death():
	
	for item in snake.tail:
		if snake.x == item[0] and snake.y == item[1]:
			return True


	

def update_tail():
	# move every position down by one if possible
	if len(snake.tail) > 1:
		for i in range(len(snake.tail) - 1):
			snake.tail[i] = snake.tail[i+1]

		snake.tail[len	(snake.tail)-1] = (snake.x, snake.y)

		for pos in snake.tail:
			pygame.draw.rect(windowSurface, RED, (pos[0], pos[1], space, space))

	if len(snake.tail) == 1:
		array = []
		array.append((snake.x, snake.y))
		pygame.draw.rect(windowSurface, RED, (array[0][0], array[0][1], space, space))



set_food()

GAME_STATE = True
GAME_OVER  = False

while boolean == True:

	if GAME_STATE == True and GAME_OVER == False:

		clock.tick(10)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit(0)

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP and dirs != 3:
					dirs = 1

				if e.key == pygame.K_RIGHT and dirs != 4:
					dirs = 2

					
				if e.key == pygame.K_DOWN and dirs != 1:
					dirs = 3

									
				if e.key == pygame.K_LEFT and dirs != 2:
					dirs = 4


		# update player
		windowSurface.fill(BLACK)

		update_tail()
		snake.update(snake.speed, dirs, space)

		foodBox = pygame.draw.rect(windowSurface, BLUE, (food_x, food_y, space, space))

		snakeBox = pygame.draw.rect(windowSurface, RED, (snake.x, snake.y, space, space))

		if snake.eat(foodBox, snakeBox):
			snake.total += 1
			if dirs == 1:
				snake.tail.append((snake.x, snake.y+15))

			elif dirs == 2:
				snake.tail.append((snake.x-15, snake.y))

			elif dirs == 3:
				snake.tail.append((snake.x, snake.y-15))

			elif dirs == 4:
				snake.tail.append((snake.x+15, snake.y))

			# change food location
			food_x = get_placement_x()
			food_y = get_placement_y()
		
			# add one to score
			score += 1

		# check bounds
		if snake.x > WIDTH:
			GAME_STATE = False
			GAME_OVER = True
		if snake.x < 0:
			GAME_STATE = False
			GAME_OVER = True
		if snake.y > HEIGHT:
			GAME_STATE = False
			GAME_OVER = True
		if snake.y < 0:
			GAME_STATE = False
			GAME_OVER = True


		if death() == True:
			GAME_STATE = False
			GAME_OVER = True


		pygame.display.update()

	elif GAME_OVER == True and GAME_STATE == False:
		clock.tick(10)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit(0)

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_RETURN:
					windowSurface.fill(BLACK)
					GAME_OVER  = False
					GAME_STATE = True
					startx = get_placement_x()
					starty = get_placement_y()
					snake = Player(startx, starty)
					score = 0


					pygame.display.update()


		windowSurface.fill(BLACK)
		game_over()
		pygame.display.update()

	

