import pygame
from paddle import paddle

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

game_over = False

clock = pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_over == True

    dis.fill(BLACK)
    pygame.draw.line(dis, WHITE, [300, 0], [300, 800], 5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
