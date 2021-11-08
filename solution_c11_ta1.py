import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()

groundx=0
speed=0
# Creating 'Bird' class
class Bird:
    # Creating 'bird' rectangle
    bird=pygame.Rect(100,250,30,30)
    # Defining 'movedown()' function to make the bird move down
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
     # Defining 'moveup()' function to make the bird move up
    def moveup(self):
        global speed
        speed=speed-10
    # Defining 'display()' function to display the bird image
    def display(self):
        screen.blit(images["bird"],self.bird)


# Creating an object for 'Bird' class and naming it 'bird1'      
bird1=Bird()

while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  # Calling the function 'movedown()' using the object 'bird1'
  bird1.movedown()
  # Calling the function 'display()' using the object 'bird1'
  bird1.display()
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            # Calling the function 'moveup()' using the object 'bird1'
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
