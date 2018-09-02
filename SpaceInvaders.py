import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
black = (0, 0, 0)
white = (255, 255, 255)
pos_x = 300
pos_y = 150
pos_x_m = 0
pos_y_m = 0
exit = False
player = pygame.image.load("SpaceShip.png")
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit = True
        if (event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                pos_x_m = 0
            if (event.key == pygame.K_UP):
                pos_y_m = 0
            if (event.key == pygame.K_DOWN):
                pos_y_m = 0
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                pos_x_m = 10
            if(event.key == pygame.K_LEFT):
                pos_x_m = -10
            if (event.key == pygame.K_UP):
                pos_y_m = -10
            if (event.key == pygame.K_DOWN):
                pos_y_m= 10
    pos_x += pos_x_m
    pos_y += pos_y_m
    clock.tick(30)
    screen.fill(white)
    screen.blit(player, [pos_x, pos_y])
    pygame.display.update()
pygame.quit()
quit()