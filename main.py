import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
