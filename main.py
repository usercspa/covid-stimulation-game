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
    time.sleep(2)    

#end screen
def game_ending():
    pygame.time.delay(500)
    screen.blit(crashed,(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    
  
#obstacles
def obstacles(obx, oby, obw, obh, color):
    pygame.draw.rect(screen, color, [obx, oby, obw, obh])     

#score
def obstacle_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    screen.blit(text,(350,50))    

     
#game loop    
def game_loop():

    game_opening()


    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)

    x_change = 0

    ob_startx = random.randrange(0, WIDTH)
    ob_starty = -600
    ob_speed = 7
    ob_width = 100
    ob_height = 100

    obCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(grey)

        obstacles(ob_startx, ob_starty, ob_width, ob_height, white)
        ob_starty += ob_speed
        player(x,y)
        obstacle_dodged(dodged)

        if x > WIDTH - player_width or x < 0:
            game_ending()

        if ob_starty > HEIGHT:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0,WIDTH)
            dodged += 1
            ob_speed += 1
            ob_width += (dodged * 1.2)


        if y < ob_starty+ob_height:
            
            if x > ob_startx and x < ob_startx + ob_width or x+player_width > ob_startx and x + player_width < ob_startx+ob_width:
                
          
              game_ending()

        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
 