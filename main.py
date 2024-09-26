import pygame
from constants import *
from player import *
def main():
    pygame.init()
    clock= pygame.time.Clock()
    dt=0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = (SCREEN_WIDTH/2)
    y = (SCREEN_HEIGHT/2)
    p1= Player(x,y,PLAYER_RADIUS)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60)/1000
        p1.draw(screen)
        p1.update(dt) 
        pygame.display.flip()
        clock.tick(60)
                  
if __name__ == "__main__":
    main()