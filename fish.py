import pygame 
import random 

class Fish():

  def __init__(self,x,y):
    self.image = pygame.image.load("fish.png")
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)


    self.speed = pygame.math.Vector2(0,5)
    rotation = random.randint(0,360)
    self.speed.rotate_ip(rotation)
    self.image = pygame.transform.rotate(self.image,180-rotation)


  def update(self):
    pass

  def draw(self,screen):
    pass
