# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    '''
    print("S tarting Asteroids!")
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

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable)

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroid_field = AsteroidField()

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

        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    #asteroid.kill()
                    asteroid.split()
                    with open("debug_log.txt", "a") as log_file:
                        log_file.write("split called\n")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()