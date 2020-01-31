# FRONT END but call some BACK-END function
import pygame, os, mouseChanger
pygame.init()

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# -------------------VARIABLE-------------------
# Position And Size
xScreen = 500
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))

# File Input Bar
lengthBar = 25
widthBar = 250
xFileBar = (xScreen / 2) - (widthBar / 2)
yFileBar = 100

# Main LABEL
xMainTitle = (xScreen / 2) - 90
yMainTitle = 20
#File Label
xFilelbl = 60
yFilelbl = 103

# WELCOME USER label
xWelUSer = 10
yWelUser = 30

# Login Window
lengthLoginWindow = 240
widthLoginWindow = 300
xLoginWindow = (xScreen / 2) - (widthLoginWindow / 2)
yLoginWindow = 150

yUsernameBar = yLoginWindow + 70
yPasswordBar = yLoginWindow + 140

yButtonLogin = (yLoginWindow + lengthLoginWindow) - 50
xButtonLogin = xLoginWindow + (widthLoginWindow / 2) - 35

lengthListPath = 100
widthListBar = 300
xPathList = (xScreen / 2) - (widthListBar / 2)

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
white = (255,255,255)
grey = (67, 67, 70)

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
# ----------------------------------------------

# PATH
robotoRegularTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Regular.ttf')
robotoLightTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Light.ttf')
imageUserPath = os.path.join(THIS_FOLDER, 'Resources\\8-513.png')

# DEFINE FONT
fontTitle = pygame.font.Font(robotoRegularTTF, 16)
fontText = pygame.font.Font(robotoLightTTF, 13)
fontWelcome = pygame.font.Font(robotoRegularTTF, 13)

# DEFINE TEXT
lblMainTitle = fontTitle.render(str("GUARDIAN ENCRYPTING"), True, white)
lblFile = fontText.render(str("File"), True, white)
lblUsername = fontText.render(str("Username"), True, white)
lblPassword = fontText.render(str("Password"), True, white)
lblButtonLogin = fontText.render(str("Login"), True, white)
# IMAGE 
imageUser = pygame.image.load(imageUserPath)

# -----------------------FUNCTION-----------------------

# First render when program is open (WINDOW LOGIN)
def loginWindow(xMouse, yMouse, tempIClicked):
  focusOnPasswordBar = False
  focusOnUsernameBar = False
  pygame.draw.rect(screen, darkBlack, (xLoginWindow, yLoginWindow, widthLoginWindow, lengthLoginWindow))

  # UserName Field
  pygame.draw.rect(screen, grey, (xLoginWindow + 20, yUsernameBar, 250, 25))
  screen.blit(lblUsername, (xLoginWindow + 20, yUsernameBar - 20))

  # Password Field
  pygame.draw.rect(screen, grey, (xLoginWindow + 20, yPasswordBar, 250, 25))
  screen.blit(lblPassword, (xLoginWindow + 20, yPasswordBar - 20))

  # Change the mouse appearance and call the click detector
  # Username Bar
  mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yUsernameBar, yUsernameBar + 25)
  if mouseSkinChanged:
    focusOnUsernameBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yUsernameBar, yUsernameBar + 25, tempIClicked)
  # Password bar
  if not(mouseSkinChanged):
    mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yPasswordBar, yPasswordBar + 25)
    if mouseSkinChanged:
      focusOnPasswordBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yPasswordBar, yPasswordBar + 25, tempIClicked)
  
  # LOGIN Button
  pygame.draw.rect(screen, grey, (xButtonLogin, yButtonLogin, 70, 30))
  screen.blit(lblButtonLogin, (xButtonLogin + 15, yButtonLogin + 5))
  if not(mouseSkinChanged):
    iPressedMyLoginButton, tempIClicked = mouseChanger.clickButtonDetect(xMouse, yMouse, xButtonLogin, xButtonLogin + 70, yButtonLogin, yButtonLogin + 30, tempIClicked)
  else:
    iPressedMyLoginButton = False

  return iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked


# Draw all UI container
def drawUiBox():
  pygame.draw.rect(screen, grey, (xFileBar,yFileBar,widthBar, lengthBar))
  pygame.draw.rect(screen, grey, (xPathList,yFileBar + 60,widthListBar, lengthListPath))


# Draw main Title
def drawMainTitle():
  screen.blit(lblMainTitle, (xMainTitle, yMainTitle))


# Draw all Label
def drawUiLabel(userName):
  # FILE label
  screen.blit(lblFile, (xFilelbl, yFilelbl))

def drawImages():
  # USER ICON
  screen.blit(imageUser, (10, 10))
  
# ------------------------------------------------------