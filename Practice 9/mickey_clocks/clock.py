import pygame
from datetime import datetime


class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (550, 400)

        # Load images
        self.base_img = pygame.image.load("Practice 9/mickey_clocks/images/micky_clocks.png").convert_alpha()
        self.sec_hand = pygame.image.load("Practice 9/mickey_clocks/images/minut.png").convert_alpha() 
        self.min_hand = pygame.image.load("Practice 9/mickey_clocks/images/hour.png").convert_alpha() 

        self.base_img = pygame.transform.scale(self.base_img, (1100, 800))

    def rotate(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=self.center)
        return rotated, rect

    def draw(self):
        now = datetime.now()

        seconds = now.second
        minutes = now.minute + seconds / 60

        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        self.screen.blit(self.base_img, (0, 0))
    
        sec_img, sec_rect = self.rotate(self.sec_hand, sec_angle)
        min_img, min_rect = self.rotate(self.min_hand, min_angle)

        self.screen.blit(min_img, min_rect)
        self.screen.blit(sec_img, sec_rect)