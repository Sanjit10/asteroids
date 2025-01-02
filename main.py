import sys
from time import sleep

import pygame
from constants import *
from player import Player
from Asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    score = 0
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        [item.draw(screen) for item in drawable]
        [item.update(dt) for item in updatable]
        for asteroid in asteroids:
            if asteroid.collides(player):
                screen.fill("#000000")
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(f'GameOver  Score :{score}', True, '#ffffff')
                textRect = text.get_rect()
                textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

                screen.blit(text, textRect)
                pygame.display.flip()
                sleep(2)
                sys.exit()
            for shot in shots:
                if asteroid.collides(shot):
                    score +=1
                    asteroid.split()

        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000

if __name__ == "__main__":
    main()