# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    
    '''
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    '''
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    #gameloop starts
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0)) #RGB Black, also "black" works
        
        ''' pre-groups
        ship.draw(screen)
        ship.update(dt)
        '''
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()