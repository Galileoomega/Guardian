# BACK-END : Will detect if the mouse is hovering Input bar or buttons and will change his skin
import pygame, os
pygame.init()

tempIClicked = False

xScreen = 450
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

resizeCursorPNG = os.path.join(THIS_FOLDER, 'Resources\\cursor.png')
RESIZE_CURSOR = pygame.image.load(resizeCursorPNG).convert_alpha()

# -----------------------FUNCTION-----------------------

# Detect when the mouse hovering an area
def flyDetector(xMouse, yMouse, xLeft, xRight, yTop, yBottom):
  if xMouse < xRight + 20:
    if xMouse > xLeft - 5:
      if yMouse < yBottom:
        if yMouse > yTop - 5:
          pygame.mouse.set_visible(False)
          screen.blit(RESIZE_CURSOR, (xMouse - 1, yMouse - 2)) 
          mouseSkinChanged = True
        else:
          pygame.mouse.set_visible(True)
          mouseSkinChanged = False
      else:
        pygame.mouse.set_visible(True)
        mouseSkinChanged = False
    else:
      pygame.mouse.set_visible(True)
      mouseSkinChanged = False
  else:
    pygame.mouse.set_visible(True)
    mouseSkinChanged = False
  
  return mouseSkinChanged

# Detect when the mouse click on an area
def clickDetect(xMouse, yMouse, xLeft, xRight, yTop, yBottom, tempIClicked):
  iClicked = False
  if xMouse < xRight + 20:
    if xMouse > xLeft - 5:
      if yMouse < yBottom:
        if yMouse > yTop - 5:
          if tempIClicked:
              if pygame.mouse.get_pressed() == (0,0,0):
                iClicked = True 
                tempIClicked = False
                #print("iClicked")

          if pygame.mouse.get_pressed() == (1,0,0):
            tempIClicked = True
            #print("TempPresdd")
        else:
          tempIClicked = False
      else:
        tempIClicked = False
    else:
      tempIClicked = False
  else:
    tempIClicked = False

  if not(iClicked):
    iPressedMyButton = False
  else:
    iPressedMyButton = True
  
  return iPressedMyButton, tempIClicked