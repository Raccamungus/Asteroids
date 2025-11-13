import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField_1 = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while 1 > 0:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for ast in asteroids:
            if ast.collides_with(Player_1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if ast.collides_with(bullet):
                    log_event("asteroid_shot")
                    ast.kill()
                    bullet.kill()

        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
