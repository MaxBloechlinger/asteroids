import pygame
import random
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from doublexpitem import DoubleXPItem

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()

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

    powerups = pygame.sprite.Group()
    DoubleXPItem.containers = (powerups, updatable, drawable)

    score = 0
    double_xp_active = False
    double_xp_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #close game window

        screen.fill("black")

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        if double_xp_active:
            xp_text = font.render("DOUBLE XP!", True, "yellow")
            screen.blit(xp_text, (10, 50))


        for obj in drawable:
            obj.draw(screen) # Draw the player

        updatable.update(dt) # update the player position

        #player asteroid collision
        for obj in asteroids:
            if player.collision(obj):
                print("Game Over!")
                print(f"Total Score: {score}")
                return
            
        #player item collision  
        for item in powerups:
            if player.collision(item):
                double_xp_active = True
                double_xp_timer = DOUBLE_XP_DURATION
                item.kill()

        if double_xp_active:
            double_xp_timer -= dt
            if double_xp_timer <= 0:
                double_xp_active = False

        #shot asteroid collision
        for asteroid in asteroids: 
            for shot in shots:
                if asteroid.collision(shot):
                    points = int(asteroid.radius * SCORE_MULTIPLIER) 
                    if double_xp_active:
                        points *= 2
                    score += points
                    # 20% chance to spawn powerup at asteroid's position
                    if random.random() < 0.1:
                        powerup = DoubleXPItem()
                        print("Powerup spawned!")
                        powerup.position = asteroid.position.copy()
                    asteroid.split()
                    shot.kill()
                     

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
