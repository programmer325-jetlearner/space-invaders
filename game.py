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
    pygame.draw.rect(screen,"red",BORDER)
    red_health_text=HEALTH_FONT.render(f"health: {red_health}",1,"white")
    yellow_health_text=HEALTH_FONT.render(f"health: {yellow_health}",1,"white")
    screen.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text,(10,10))
    screen.blit(RED_SPACESHIP,(red.x,red.y))
    screen.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen,"red",bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,"yellow",bullet)
    
    pygame.display.update()


def yellow_spaceship_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL+yellow.width<BORDER.x:
        yellow.x+=VEL
    if keys_pressed[pygame.K_w] and yellow.y-VEL>0:
        yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL+yellow.height<HEIGHT-15:
        yellow.y+=VEL

def red_spaceship_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x+BORDER.width:
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x+VEL+red.width<WIDTH:
        red.x+VEL
    if keys_pressed[pygame.K_UP] and red.y-VEL>0:
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red.y+VEL+red.height<HEIGHT-15:
        red.y+=VEL


YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2

def handling_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=BUL_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x-=BUL_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,"white")
    screen.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

#main game function
def main():
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(300,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets=[]
    yellow_bullets=[]
    red_health=10
    yellow_health=10
    clock=pygame.time.Clock()   
    run=True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<MAX_BULS:
                    bullet=pygame.Rect(yellow.x+SPACESHIP_WIDTH,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                
                if event.key==pygame.K_RCTRL and len(red_bullets)<MAX_BULS:
                    bullet=pygame.Rect(red.x+SPACESHIP_WIDTH,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
                
            if event.type==RED_HIT:
                red_health-=1
            if event.type==YELLOW_HIT:
                yellow_health-=1
        winner_txt=""
        if yellow_health<=0:
            winner_txt="RED WINS!"
        if red_health<=0:
            winner_txt="YELLOW WINS!"
        
        keys_pressed=pygame.key.get_pressed()
        yellow_spaceship_movement(keys_pressed,yellow)
        red_spaceship_movement(keys_pressed,red)
        handling_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        if winner_txt!="":
            draw_winner(winner_txt)
            break
    main()

main()
        
    
                    
        
        


    
    
    
        






    



