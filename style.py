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
xFilelbl = 90
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
widthListBar = 400
xPathList = (xScreen / 2) - (widthListBar / 2)

# ENCRYPT Button
widthEncryptButton = 90
lengthEncryptButton = 40
xEncryptButton = ((xScreen / 2) - (widthEncryptButton / 2)) - 100
yEncrypButton = 400

# DECRYPT Button
widthDecryptButton = 90
lengthDecryptButton = 40
yDecryptButton = 400
xDecryptButton = ((xScreen / 2) - (widthDecryptButton / 2)) + 100

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey]

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
# ----------------------------------------------

# PATH
robotoRegularTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Regular.ttf')
robotoLightTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Light.ttf')
imageUserPath = os.path.join(THIS_FOLDER, 'Resources\\8-513.png')
imageLockPath = os.path.join(THIS_FOLDER, 'Resources\\lock.png')
imageUnlockPath = os.path.join(THIS_FOLDER, 'Resources\\unlock.png')

# DEFINE FONT
fontTitle = pygame.font.Font(robotoRegularTTF, 16)
fontText = pygame.font.Font(robotoLightTTF, 13)
fontWelcome = pygame.font.Font(robotoRegularTTF, 13)

# DEFINE TEXT
lblMainTitle = fontTitle.render(str("GUARDIAN ENCRYPTION"), True, white)
lblFile = fontText.render(str("File"), True, halfWhite)
lblCryptButton = fontWelcome.render(str("ENCRYPT"), True, white)
lblDecryptButton = fontWelcome.render(str("DECRYPT"), True, white)
lblUsername = fontText.render(str("Username"), True, white)
lblPassword = fontText.render(str("Password"), True, white)
lblButtonLogin = fontText.render(str("Login"), True, white)
lblAwaiting = fontText.render(str("Awaiting files"), True, halfWhite)
lblStatus = fontText.render(str("Status"), True, halfWhite)

# IMAGE 
imageUser = pygame.image.load(imageUserPath)
imageLock = pygame.image.load(imageLockPath)
imageUnlock = pygame.image.load(imageUnlockPath)

# -----------------------FUNCTION-----------------------

# First render when program is open (WINDOW LOGIN)
def loginWindow(xMouse, yMouse, tempIClicked):
  focusOnPasswordBar = False
  focusOnUsernameBar = False
  pygame.draw.rect(screen, listOfColor[5], (xLoginWindow, yLoginWindow, widthLoginWindow, lengthLoginWindow))

  # UserName Field
  pygame.draw.rect(screen, listOfColor[6], (xLoginWindow + 20, yUsernameBar, 250, 25))
  screen.blit(lblUsername, (xLoginWindow + 20, yUsernameBar - 20))

  # Password Field
  pygame.draw.rect(screen, listOfColor[7], (xLoginWindow + 20, yPasswordBar, 250, 25))
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
  pygame.draw.rect(screen, listOfColor[8], (xButtonLogin, yButtonLogin, 70, 30))
  screen.blit(lblButtonLogin, (xButtonLogin + 15, yButtonLogin + 5))
  if not(mouseSkinChanged):
    # Detect click button
    iPressedMyLoginButton, tempIClicked = mouseChanger.clickButtonDetect(xMouse, yMouse, xButtonLogin, xButtonLogin + 70, yButtonLogin, yButtonLogin + 30, tempIClicked)
    # Change button color
    mouseChanger.flyDetectorButtons(tempIClicked, listOfColor, 8)

  else:
    iPressedMyLoginButton = False

  return iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked


# Draw all UI container
def drawUiBox(listOfColor):
  pygame.draw.rect(screen, listOfColor[0], (xFileBar, yFileBar, widthBar, lengthBar))
  pygame.draw.rect(screen, listOfColor[1], (xPathList, yFileBar + 60, widthListBar, lengthListPath))
  pygame.draw.rect(screen, listOfColor[2], (xPathList, yFileBar + 60, widthListBar, lengthListPath - 80))
  pygame.draw.rect(screen, listOfColor[3], (xEncryptButton, yEncrypButton, widthEncryptButton, lengthEncryptButton))
  pygame.draw.rect(screen, listOfColor[4], (xDecryptButton, yDecryptButton, widthDecryptButton, lengthDecryptButton))
  


# Draw main Title
def drawMainTitle():
  screen.blit(lblMainTitle, (xMainTitle, yMainTitle))


# Draw all Label
def drawUiLabel(userName):
  # FILE label
  screen.blit(lblFile, (xFilelbl, yFilelbl))
  screen.blit(lblDecryptButton, (xDecryptButton + 14, yDecryptButton + 10))
  screen.blit(lblCryptButton, (xEncryptButton + 14, yEncrypButton + 10))
  screen.blit(lblAwaiting, (xPathList + 5, yFileBar + 60))
  screen.blit(lblStatus, (xPathList + 300, yFileBar + 60))


def drawImages():
  # USER ICON
  #screen.blit(imageUser, (10, 10))
  screen.blit(imageLock, (xEncryptButton + 25, yEncrypButton + 45))
  screen.blit(imageUnlock, (xDecryptButton + 25, yDecryptButton + 45))
  
# ------------------------------------------------------