import pygame, sys
from pygame.locals import *
import random

# ===================== INIT =====================
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COINS = 0
COINS_FOR_SPEED = 5 

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Assets
background = pygame.image.load("Practice 11/images/road.png")

# Sound 
crash_sound = pygame.mixer.Sound("Practice 11/sounds/crash.mp3")

# Display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# ===================== ENEMY =====================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Practice 11/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# ===================== COIN =====================
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()
        self.value = random.choice([1, 2, 3])

        if self.value == 1:
            img= pygame.image.load("Practice 11/images/Coin1.png")
        elif self.value == 2:
            img = pygame.image.load("Practice 11/images/Coin2.png")
        else:
            img = pygame.image.load("Practice 11/images/Coin3.png")

        self.image = pygame.transform.scale(img, (60, 50))
        self.rect = self.image.get_rect()
        self.enemies = enemies
        self.spawn()

    def spawn(self):
        # check spawn of the coin 10 times
        for _ in range(10):
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if not pygame.sprite.spritecollideany(self, self.enemies):
                return
        #otherwise just put it
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Practice 11/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        #moving on x-ase only and scheking screen boarders

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# declarying objects
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
C1 = Coin(enemies)
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #loading bacrkground
    DISPLAYSURF.blit(background, (0, 0))

    # UI
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))

    # movement
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.time.delay(500)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        pygame.time.delay(2000)

        pygame.quit()
        sys.exit()

    collected_coins = pygame.sprite.spritecollide(P1, coins, True)

    for coin in collected_coins:
        COINS += coin.value

        #getting speed 
        if COINS % COINS_FOR_SPEED == 0:
            SPEED += 1

        # new coin
        new_coin = Coin(enemies)
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)