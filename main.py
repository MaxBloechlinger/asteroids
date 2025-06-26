import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group() # all the objects that can be updated
    drawable = pygame.sprite.Group() # all the objects that can be drawn
    Player.containers = (updatable, drawable) # set as player group containers

    player = Player(x, y) # init Player object

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)


    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #close game window

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen) # Draw the player

        updatable.update(dt) # update the player position

        for obj in asteroids:
            if player.collision(obj):
                print("Game Over!")
                return
        for asteroid in asteroids: 
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
