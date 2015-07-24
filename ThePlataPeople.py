import pygame
from pygame.locals import *  #These imports get basic pygame commands

window_x = 800
window_y = 600

frames = 0
FPS = 60

#Initializing requirements
pygame.init()
clock = pygame.time.Clock()
running = True

#Creating window properties and backgroudn color.
window = pygame.display.set_mode((window_x,window_y),pygame.RESIZABLE)
background = pygame.Surface(window.get_size())
background.fill((0,0,0))
background = background.convert();
window.blit(background,(0,0))

#Creating a wall
class wall:
    def __init__(self):
        self.pos = [100,300]
        self.width = 100
        self.length = 200
    def draw(self):
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness) **This is for my refernce**
        pygame.draw.rect(window, (180,255,4), (0,590,800,10), 10) #Temporary floor


#Creating the temporary player and movement
class Player:
    def __init__(self):
        self.pos = [25,575]
        self.radius = 20
        self.speed = 5
	self.weight = 3
	self.jumpspeed = 10
    def movement(self):
        KeyList = pygame.key.get_pressed()
        #if KeyList[K_UP]:
            #self.pos[1] -= self.speed
        if KeyList[K_DOWN]:
            self.pos[1] += self.speed
        if KeyList[K_LEFT]:
            self.pos[0] -= self.speed
        if KeyList[K_RIGHT]:
            self.pos[0] += self.speed
        pygame.draw.circle(window,(0,0,255),self.pos,self.radius)
    def gravity(self):
	if self.pos[1] > 10:
	    self.pos[1] += self.weight
    def jump(self):
	KeyList = pygame.key.get_pressed()	
	if KeyList[K_UP] == True:
	    self.weight = 0
	    self.pos[1] += self.jumpspeed
	else:
	    self.weight = 3


#Calling everything
wall = wall()
player = Player()


#This makes sure the game can quit correctly on a website
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #This makes sure the player cant move off screen
    if player.pos[0] < 5:
        player.pos[0] = 5
    if player.pos[0] > 795:
        player.pos[0] = 795
    if player.pos[1] < 10:
        player.pos[1] = 10
    if player.pos[1] > 595:
        player.pos[1] = 595
    #Calling more things
    window.fill((0,0,0))
    wall.draw()
    player.movement()
    player.gravity()
    player.jump()
    clock.tick(FPS)
    frames += 1
    print frames #To check if anything freezes / check for performance drops on webserver
    #pygame.display.flip() ---Might use this in the future
    pygame.display.update()
pygame.exit()
