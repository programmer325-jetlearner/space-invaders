import pygame
import os

pygame.init()
WIDTH=900
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders")

BORDER=pygame.Rect(445,0,10,HEIGHT)
HEALTH_FONT=pygame.font.SysFont("Times New Roman",40)
WINNER_FONT=pygame.font.SysFont("Times New Roman",40)
FPS=60
VEL=5
BUL_VEL=7
MAX_BULS=3
SPACESHIP_WIDTH=55
SPACESHIP_HEIGHT=40

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","yellow_spaceship.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","red_spaceship.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE_IMG=pygame.image.load(os.path.join("assets","bg.png"))
SPACE=pygame.transform.scale(SPACE_IMG,(900,500))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(SPACE,(0,0))




