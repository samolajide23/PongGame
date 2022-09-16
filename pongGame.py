import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 102)

display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong Game')
# Paddle Code
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 570
paddleB.rect.y = 100

ball = Ball(YELLOW, 10, 10)
ball.rect.x = 295
ball.rect.y = 125

sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)
sprites_list.add(ball)


game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_over == True

    if pygame.key.get_pressed()[pygame.K_w]:
        paddleA.moveUp(5)
    if pygame.key.get_pressed()[pygame.K_s]:
        paddleA.moveDown(5)
    if pygame.key.get_pressed()[pygame.K_UP]:
        paddleB.moveUp(5)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        paddleB.moveDown(5)

    sprites_list.update()

    if ball.rect.x >= 590:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 390:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1] 

    dis.fill(BLACK)
    pygame.draw.line(dis, WHITE, [300, 0], [300, 800], 5)
    sprites_list.draw(dis)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
