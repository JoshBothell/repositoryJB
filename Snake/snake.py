import pygame

pygame.init()

right = pygame.image.load('right.png')
left = pygame.image.load('left.png')
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')
direction = "right"

screen_width = 1000
screen_height = 800
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snek")
class snake(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

def redrawGameWindow():
    global direction
    win.fill((0, 0, 0,))
    if direction == "left":
        win.blit(left, (snake.x, snake.y))
    if direction == "right":
        win.blit(right, (snake.x, snake.y))
    if direction == "up":
        win.blit(up, (snake.x, snake.y))
    if direction == "down":
        win.blit(down, (snake.x, snake.y))
    pygame.display.update()

snake = snake(50, 50, 50, 50)
run = True
while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if snake.x < 1:
        run = False
    elif snake.x > screen_width - snake.width - 1:
        run = False
    elif snake.y < 1:
        run = False
    elif snake.y > screen_height - snake.height - 1:
        run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake.x > 0:
        direction = "left"
    elif keys[pygame.K_RIGHT] and snake.x < screen_width - snake.width:
        direction = "right"
    elif keys[pygame.K_UP] and snake.y > 0:
        direction = "up"
    elif keys[pygame.K_DOWN] and snake.y < screen_height - snake.height:
        direction = "down"

    if direction == "left" and snake.x > 0:
        snake.x -= snake.vel
    elif direction == "right" and snake.x < screen_width - snake.width:
        snake.x += snake.vel
    elif direction == "up" and snake.y > 0:
        snake.y -= snake.vel
    elif direction == "down" and snake.y < screen_height - snake.height:
        snake.y += snake.vel
    redrawGameWindow()


pygame.quit()
    
