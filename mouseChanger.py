# BACK-END : Will detect if the mouse is hovering Input bar or buttons and will change his skin
import pygame, os
from module import timeVar
pygame.init()

tempIClicked = False

xScreen = 450
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))

black = (40, 40, 43)
grey = (67, 67, 70)
lavanda = (0, 115, 210)

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
          #pygame.mouse.set_visible(False)
          pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
          screen.blit(RESIZE_CURSOR, (xMouse - 1, yMouse - 2)) 
          mouseSkinChanged = True
        else:
          pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))
          mouseSkinChanged = False
      else:
        pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))
        mouseSkinChanged = False
    else:
      pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))
      mouseSkinChanged = False
  else:
    pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))
    mouseSkinChanged = False
  
  return mouseSkinChanged


# Can Change the color of a button (similar to flyDetector())
def flyDetectorButtons(permissionToChange, listOfColor, index, baseColor):
  if permissionToChange:
    listOfColor[index] = lavanda
  else:
    listOfColor[index] = baseColor


# Detect when the mouse click on an BUTTON
def clickButtonDetect(xMouse, yMouse, xLeft, xRight, yTop, yBottom, tempIClicked):
  iClicked = False
  if xMouse < xRight + 20:
    if xMouse > xLeft - 5:
      if yMouse < yBottom:
        if yMouse > yTop - 5:
          if tempIClicked:
            if pygame.mouse.get_pressed() == (0,0,0):
              iClicked = True 
              tempIClicked = False

          if pygame.mouse.get_pressed() == (1,0,0):
            tempIClicked = True
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


# Detect when the mouse click on an FILE FIELD
def clickFileDetect(xMouse, yMouse, xLeft, xRight, yTop, yBottom, tempIClicked, time):
  iClicked = False
  if xMouse < xRight + 20:
    if xMouse > xLeft - 5:
      if yMouse < yBottom:
        if yMouse > yTop - 5:
          if tempIClicked:
            if pygame.mouse.get_pressed() == (0,0,0):
              iClicked = True 
              #tempIClicked = False

          if pygame.mouse.get_pressed() == (1,0,0):
            tempIClicked = True

            #if (timeVar.time - timeVar.oldTime) <= 500:
            #  print("time : ", time, "oldTime : ", timeVar.oldTime)
            # print(timeVar.time - timeVar.oldTime)
            #else:
           #   timeVar.oldTime = pygame.time.get_ticks()

            now = timeVar.time
            
            if now - timeVar.oldTime <= timeVar.double_click_duration:
              timeVar.clickState = "double"
            else:
              timeVar.clickState = "single"
            timeVar.oldTime = pygame.time.get_ticks()
            pygame.time.delay(50)

        else:
          if pygame.mouse.get_pressed() == (1,0,0):
            tempIClicked = False
      else:
        if pygame.mouse.get_pressed() == (1,0,0):
          tempIClicked = False
    else:
      if pygame.mouse.get_pressed() == (1,0,0):
        tempIClicked = False
  else:
    if pygame.mouse.get_pressed() == (1,0,0):
      tempIClicked = False

  if not(iClicked):
    iPressedMyButton = False
  else:
    iPressedMyButton = True
    
  return iPressedMyButton, tempIClicked


# Detect when the mouse click on an INPUT BAR
def clickBarDetect(xMouse, yMouse, xLeft, xRight, yTop, yBottom, tempIClicked):
  iClicked = False
  if xMouse < xRight + 20:
    if xMouse > xLeft - 5:
      if yMouse < yBottom:
        if yMouse > yTop - 5:
          if tempIClicked:
            iClicked = True

          if pygame.mouse.get_pressed() == (1,0,0):
            tempIClicked = True

        else:
          iClicked = False
          tempIClicked = False
      else:
        iClicked = False
        tempIClicked = False
    else:
      iClicked = False
      tempIClicked = False
  else:
    iClicked = False
    tempIClicked = False

  if not(iClicked):
    iPressedMyButton = False
  else:
    iPressedMyButton = True

  if iClicked:
    iPressedMyButton = True
  else:
    iPressedMyButton = False
    
  return iPressedMyButton, tempIClicked