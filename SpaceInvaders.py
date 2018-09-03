import pygame
pygame.init()

HEIGHT = 800
WIDTH = 800

screen = pygame.display.set_mode((HEIGHT, WIDTH))
black = (0, 0, 0)
white = (255, 255, 255)
pos_x = 300
pos_y = 150
pos_x_m = 0
pos_y_m = 0
exit = False
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("SpaceShip.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speedx = 0
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)
while not exit:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit = True
    pos_x += pos_x_m
    pos_y += pos_y_m
    clock.tick(30)
    screen.fill(white)
    sprites.draw(screen)
    sprites.update()
    pygame.display.update()
pygame.quit()
quit()
