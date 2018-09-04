import pygame
import random
pygame.init()

HEIGHT = 800
WIDTH = 800

screen = pygame.display.set_mode((HEIGHT, WIDTH))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pos_x = 20
pos_y = 700
pos_x_m = 0
pos_y_m = 0
kills1 = 0
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
    def shoot(self):
        bullet = Bullets(self.rect.x, self.rect.y)
        sprites.add(bullet)
        bullets.add(bullet)



class Mobs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -30)
        self.speedx = random.randrange(3, 8)
    def update(self):
        self.rect.y += self.speedx
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -30)
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -10
    def update(self):
        self.rect.y += self.speedx
sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
sprites.add(player)
for i in range(8):
    mob = Mobs()
    sprites.add(mob)
    mobs.add(mob)
while not exit:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.shoot()
    kills = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if kills:
        mob = Mobs()
        mobs.add(mob)
        sprites.add(mob)
        kills1 += 1
        print(kills1)
    kills  = pygame.sprite.spritecollide(player, mobs, False)
    if kills:
        player.kill()
        exit = True
    pos_x += pos_x_m
    pos_y += pos_y_m
    clock.tick(30)
    sprites.update()
    screen.fill(white)
    sprites.draw(screen)
    sprites.update()
    pygame.display.update()
pygame.quit()
quit()
