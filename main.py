import pygame 
from pygame.locals import *

pygame.init()

size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

fish_image = pygame.image.load("fish.png")
fish_rect = fish_image.get_rect()

def main():
  print("Starting game...")
  while True:
    clock.tick(60)
    print("Running game")
    
    screen.fill(WHITE)

    screen.blit(fish_image,fish_rect)
    
    pygame.display.flip()



if __name__ == "__main__":
  main()

