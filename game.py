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


