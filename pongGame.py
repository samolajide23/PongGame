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
scoreA = 0
scoreB = 0

font_style = pygame.font.SysFont("bahnschrift", 25)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width/20, display_height/3])


def gameLoop(scoreA, scoreB):
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
    pygame.time.wait(200)

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
            scoreA += 1
            pygame.time.wait(500)
            gameLoop(scoreA, scoreB)
        if ball.rect.x <= 0:
            scoreB += 1
            pygame.time.wait(500)
            gameLoop(scoreA, scoreB)
        if ball.rect.y > 390:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()

        dis.fill(BLACK)
        pygame.draw.line(dis, WHITE, [300, 0], [300, 800], 5)
        sprites_list.draw(dis)

        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        dis.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        dis.blit(text, (420, 10))

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
    quit()


gameLoop(scoreA, scoreB)
