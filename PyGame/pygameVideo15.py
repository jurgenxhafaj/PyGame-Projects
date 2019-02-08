import pygame
import time
import random


pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
# blue=(0,0,255)

bright_red=(255,0,0)
bright_green=(0,255,0)

block_color = (53, 115, 255)

car_width = 180


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('a bit racey')

clock = pygame.time.Clock()

carImg=pygame.image.load('eddy.jpg')

def things_dodged(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text=font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (10,10))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

    # you can add color argument to text objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(3)

    game_loop()
    

    
    
    #message, x, y, width, height, inactive color, active color
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
#             if action == "play":
#                 game_loop()
#             elif action == "quit":
#                 pygame.quit()
#                 quit()
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
            
    smallText=pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center=((x+(w/2)), (y+(h/2) ))
    gameDisplay.blit(textSurf, textRect)
    
    
def quitgame():
    pygame.quit()
    quit()
    
    
    
def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            #print(event) 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects("A bit racey", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        
        
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        
        
        
        pygame.display.update()
        clock.tick(15)
    
def crash():
    message_display('You messed up!')
    
    
    
    
    
    
def game_loop():
    
    # starts from top left

    x = (display_width * 0.4)
    y = (display_height * 0.7)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    
    dodged=0
    
    gameExit = False

    
    
    #loop starts here

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        #put the FILL first, then the car/other stuff
        gameDisplay.fill(white)
        
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        
        car(x,y)    
        things_dodged(dodged)

        if x > display_width-car_width or x < 0:
            crash()
        
        #once the objects passes down the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5
            thing_width += (dodged * 1.2)
        
        if y < thing_starty + thing_height:
            #print('y crossover')
            
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width: 
                #print('x crossover')
                crash()
        
        pygame.display.update()

        clock.tick(30)
    
    
game_intro()
    
game_loop()
    
pygame.quit()

quit()
