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