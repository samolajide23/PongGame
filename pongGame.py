import pygame
from paddle import Paddle

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

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 570
paddleB.rect.y = 100

sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)

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

    dis.fill(BLACK)
    pygame.draw.line(dis, WHITE, [300, 0], [300, 800], 5)
    sprites_list.draw(dis)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
