import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        #player1.draw(screen)
        #player1.update(dt)
        
        updatable.update(dt)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        
        #clock.tick(60) # pauses game loop until 1/60th of a second passed, is called in next line
        dt = clock.tick(60) / 1000 # returns dt, divide by 1000 to convert milliseconds to seconds
    
    
if __name__ == "__main__":
    main()