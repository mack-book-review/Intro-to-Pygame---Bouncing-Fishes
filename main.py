import pygame, random
from pygame.locals import *

pygame.init()

size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



def move_fish():
  global speed, fish_rect, fish_image
  fish_rect.move_ip(speed)

  if fish_rect.left < 0 or fish_rect.right > width:
    speed[0] *= -1 
    fish_image = pygame.transform.flip(fish_image,True,False)
    fish_rect.move_ip(speed)

  if fish_rect.top < 0 or fish_rect.bottom > height:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image,False,True)
    fish_rect.move_ip(speed)

def main():
  global fish_rect,fish_image
  global speed
  print("Starting game...")
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
      if event.type == KEYDOWN:
        if event.key == K_DOWN:
          pass 
        if event.key == K_UP: 
          pass
        if event.key == K_LEFT:
          pass
        if event.key == K_RIGHT: 
          pass
      if event.type == MOUSEBUTTONDOWN:
        pass
    

    move_fish()
    
    screen.fill(WHITE)

    screen.blit(fish_image,fish_rect)
    
    pygame.display.flip()



if __name__ == "__main__":
  main()

