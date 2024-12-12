import pygame
import random
import math
import sys

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rogeri gridshot')

clock = pygame.time.Clock()
start = 60  
game_start_time = pygame.time.get_ticks() 

ringi_pos = (1280/2, 720/2)

font = pygame.font.Font(None, 30)

skoor = 0

def tsekka_kas_ring_klikiti() -> bool:
    hiire_pos = pygame.mouse.get_pos()
    
    if math.sqrt((hiire_pos[0] - ringi_pos[0])**2 + (hiire_pos[1] - ringi_pos[1])**2) <= 50:
        return True
    return False
                

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if tsekka_kas_ring_klikiti():
                    skoor += 1
                    ringi_pos = (random.randint(0, 1280), random.randint(0, 720))
    
    elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000
    remaining_time = start - elapsed_time
    
    if remaining_time <= 0:
        remaining_time = 0
        print("Sa said skoori ", skoor)
    
    
    score_surface = font.render(f'Skoor: {skoor}', True, "black")
    timer_surface = font.render(f'Aeg: {remaining_time}', True, "black")
    
    screen.fill('lightblue')
    
    pygame.draw.circle(screen, "yellow", ringi_pos, 50)
    
    screen.blit(score_surface, (50, 50))
    screen.blit(timer_surface, (50, 100))
    
    pygame.display.update()
    
    if remaining_time == 0:
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    clock.tick(60)
    
