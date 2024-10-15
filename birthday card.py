import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday card")

img = pygame.image.load("birthdaycake.webp")
image = pygame.transform.scale(img,(WIDTH, HEIGHT))

while (True):
    font = pygame.font.SysFont("Times New Roman", 72)

    t1 = font.render("Happy Birthday", True, (0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(t1,(50,50))
    pygame.display.update()
    
    time.sleep(2)

    image2 = pygame.image.load("gift.png")
    image3 = pygame.transform.scale(image,(WIDTH,HEIGHT))
    font2 = pygame.font.SysFont("Berlin Sans FB", 72)
    t2 = font2.render("Wish you all the best", True, (255,255,0))
    screen.fill(255,255,255)
    screen.blit(t2,(50,50))
    screen.blit(image3,(0,0))
    pygame.display.update()
    
    time.sleep(2)











