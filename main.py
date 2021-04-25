#install packages
import pygame
import time
import random

#initialize
pygame.init()

#screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cvoid stimulation game")
clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (123,123,123)

player_width = 56

#load images
human = pygame.image.load("human.png")
opening = pygame.image.load("opening.png")
crashed = pygame.image.load("crash.png")
risk = pygame.image.load("risk.png")
rock = pygame.image.load("rock.png")

#player position 
def player(x,y):
  screen.blit(human, (x, y))

#start screen
def game_opening():
    screen.blit(opening,(0,0))
    pygame.display.update()
    time.sleep(1)    

#game loop    
def game_loop():

    game_opening()


    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)

    x_change = 0
      
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()      