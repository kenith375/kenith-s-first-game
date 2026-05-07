# 
# 
#
import pygame as pg #pygame is what allows the creation of the screen. every instance of "pg" refers to pygame
import os
filepath=os.path.dirname(__file__)
screen = pg.display.set_mode((0, 0)) #This makes the pygame window
pg.display.set_caption('Anime style game') #This changes the pygame window name

#Distance is measured in either milimetes (none) or pixels (px)
pixWidth=10 #Each pixel on the screen is pixWidth mm wide and tall. This doesn't change the resolution. Each pixel on screen represents pixWidth in game mm.


class playr: #This is only used for player code, this may change in future. It's used to make the player object "player=playr(400,0,0,-10)"
  def __init__(self,x,y,spdX,spdY,height=48): #Some details about the player
    self.height=height
    self.x=x
    self.y=y
    self.spdX=spdX
    self.spdY=spdY

  def physics(self,keys): #All the code for player physics as well as movement here pls
    self.spdY-=0.5
    self.y+=self.spdY
    can_jump=False #Local variable e.g. doesn't exist after the end of the physics function so removing it won't break anything apart from jumping
    for i in floors:
      if self.x>i[0] and self.x<i[2]:
        if self.y-self.height<i[1] and self.y>i[1]:
          self.y=i[1]+self.height
          self.spdY=max(0,self.spdY)
          can_jump=True #This is where can_jump can change
    if keys[pg.K_LEFT]:
      self.spdX-=2
    if keys[pg.K_RIGHT]:
      self.spdX+=2
    self.x+=self.spdX
    self.spdX*=.75

    if keys[pg.K_SPACE] and can_jump: #The placeholder for jumpinge placeholder for jumping, (the last use of can_jump)
      player.spdY=20
  def display(self,screen,cam_pos,scale): #This is what draws the player, change this to make the player look diffrent, it won't break the game
    img=pg.image.load(os.path.join(filepath, "assets", "a.png")) #Place holder image
    screen.blit(img,(self.x,-self.y)) #Puts the image on the screen, the screen being the object defined on line 5

#player=obj(x position, y position, x speed, y speed) #because height is not specified here, it is defaulted to height=48 since that's the height of the first placeholder image
player=playr(400,0,0,-10) #Makes the player object, obj is just the name of the class, not a fuction called obj #btw this is calling the "__init__" function.
#The player's y pos for example is player.y, to perform functions with player, use player.function(), for example, player.display() 






floors=[[-1000,-500,1000],#A 2d array representing the various floor surfaces. floors[i], is 1 of these floors containing ["start x pos", "y level", "end x pos"]
        [1000,-800,2000]] 








class state:
  def __init__(self,gameplay,menutype,cutscene):
    self.gameplay=gameplay
    self.menutype=menutype
    self.cutscene=cutscene

gameplay_state=state(True,"main","none")

clock=pg.time.Clock()


running=True
while running:
  screen.fill((0,0,0))
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
      print("exited with y value of: ",player.y)
  #Here it's checked whether the game is in a menu, cutscene or gameplay
  if gameplay_state.gameplay:
    keys=pg.key.get_pressed()
    #executes regular physics
    player.physics(keys)
    player.display(screen,(0,0),pixWidth)
  elif gameplay_state.cutscene=="none":
    print("delete this line")
    #executes menu
  else:
    print("replace line")
    #does cutscene
  pg.display.flip()
  clock.tick(60)
