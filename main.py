import pygame 
import os

pygame.init()
# init width and height with values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Changin a caption to Lunga Games 
pygame.display.set_caption('Lunga Games')

# Creating a white variable of white color rgb
WHITE =(255,255,255)
FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

def draw_window():
     WIN.fill((WHITE))
     WIN.blit(YELLOW_SPACESHIP_IMAGE, ())
     WIN.blit(RED_SPACESHIP_IMAGE, ())
     pygame.display.update()
     
     


#  Function called Main with variable  run that is set to True while true.
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

if __name__ == "__main__":
    main()