import pygame
import os


pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("shooter game")

BORDER=pygame.Rect(445,0,10,HEIGHT)
HEALTH_FONT=pygame.font.SysFont("Times New Roman",40)
WINNER_FONT=pygame.font.SysFont("Times New Roman",40)
FPS=60
VEL=5
BUL_VEL=7
MAX_BULS=3
STICKPERSON_WIDTH=55
STICKPERSON_HEIGHT=40

STICKMAN1_IMAGE=pygame.image.load(os.path.join("images","sticko.png"))
STICKMAN1=pygame.transform.rotate(pygame.transform.scale(STICKMAN1_IMAGE,(STICKPERSON_WIDTH,STICKPERSON_HEIGHT)),90)
STICKMAN2_IMAGE=pygame.image.load(os.path.join("images","sticky.png"))
STICKMAN2=pygame.transform.rotate(pygame.transform.scale(STICKMAN2_IMAGE,(STICKPERSON_WIDTH,STICKPERSON_HEIGHT)),270)
CITY_IMG=pygame.image.load(os.path.join("images","bg.png"))
CITY=pygame.transform.scale(CITY_IMG,(900,500))

def draw_window(stick2,stick1,stick2_bullets,stick1_bullets,stick2_health,stick1_health):
    screen.blit(CITY,(0,0))
    pygame.draw.rect(screen,"red",BORDER)
    stick1_health_text=HEALTH_FONT.render(f"health: {stick1_health}",1,"white")
    stick2_health_text=HEALTH_FONT.render(f"health: {stick2_health}",1,"white")
    screen.blit(stick1_health_text,(WIDTH-stick1_health_text.get_width()-10,10))
    screen.blit(stick2_health_text,(10,10))
    screen.blit(STICKMAN1,(stick1.x,stick1.y))
    screen.blit(STICKMAN2,(stick2.x,stick2.y))

    for bullet in stick1_bullets:
        pygame.draw.rect(screen,"stick1",bullet)
    
    for bullet in stick2_bullets:
        pygame.draw.rect(screen,"stick2",bullet)
    
    pygame.display.update()


def stick2_movement(keys_pressed,stick2):
    if keys_pressed[pygame.K_a] and stick2.x-VEL>0:
        stick2.x-=VEL
    if keys_pressed[pygame.K_d] and stick2.x+VEL+stick2.width<BORDER.x:
        stick2.x+=VEL
    if keys_pressed[pygame.K_w] and stick2.y-VEL>0:
        stick2.y-=VEL
    if keys_pressed[pygame.K_s] and stick2.y+VEL+stick2.height<HEIGHT-15:
        stick2.y+=VEL

STICKMAN1_HIT=pygame.USEREVENT+1
STICKMAN2_HIT=pygame.USEREVENT+2

def handling_bullets(stick1_bullets,stick2_bullets,stick1,stick2):
    for bullet in stick1_bullets:
        bullet.x+=BUL_VEL
        if stick2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(STICKMAN2_HIT))
            stick1_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            stick1_bullets.remove(bullet)
    
    for bullet in stick2_bullets:
        bullet.x-=BUL_VEL
        if stick1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(STICKMAN1_HIT))
            stick2_bullets.remove(bullet)
        elif bullet.x<0:
            stick2_bullets.remove(bullet)



def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,"black")
    screen.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

        



pygame.quit()