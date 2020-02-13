# FRONT END but call some BACK-END function
import pygame, os
import mouseChanger
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
widthBar = 270
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

# Path List
lengthListPath = 100
widthListBar = 400
xPathList = (xScreen / 2) - (widthListBar / 2)
yPathList = yFileBar + 60

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

# Add Button
xAddButton = xFileBar + widthBar + 35
yAddButton = yFileBar
widthAddButton = 26
lengthAddButton = 26

# Dialog Browser
widthDialogBrowser = 340
lengthDialogBrowser = 330
xDialogBrowser = (xScreen / 2) - (widthDialogBrowser / 2)
yDialogBrowser = 100

# Blue Circle
xCloseCircle = xDialogBrowser + widthDialogBrowser - 30
yCloseCircle = yDialogBrowser + 2

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)
red = (189, 11, 11)
lavanda = (0, 115, 210)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey, black, black]

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
imageEyePath = os.path.join(THIS_FOLDER, 'Resources\\eyeBall.png')
imageCirclePath = os.path.join(THIS_FOLDER, 'Resources\\circle.png')

# DEFINE FONT
fontTitle = pygame.font.Font(robotoRegularTTF, 16)
fontText = pygame.font.Font(robotoLightTTF, 13)
fontWelcome = pygame.font.Font(robotoRegularTTF, 13)
fontError = pygame.font.Font(robotoRegularTTF, 13)

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
lblDialogBrowser = fontText.render(str("Browser..."), True, halfWhite)

# IMAGE 
imageUser = pygame.image.load(imageUserPath)
imageLock = pygame.image.load(imageLockPath)
imageUnlock = pygame.image.load(imageUnlockPath)
imageEye = pygame.image.load(imageEyePath)
imageCircle = pygame.image.load(imageCirclePath)

# -----------------------FUNCTION-----------------------

# First render when program is open (WINDOW LOGIN)
def loginWindow(xMouse, yMouse, tempIClicked):
  focusOnPasswordBar = False
  focusOnUsernameBar = False

  # BACKGROUND BLIT
  pygame.draw.rect(screen, listOfColor[5], (xLoginWindow, yLoginWindow, widthLoginWindow, lengthLoginWindow))

  # UserName Field BLIT
  pygame.draw.rect(screen, listOfColor[6], (xLoginWindow + 20, yUsernameBar, 250, 25))
  screen.blit(lblUsername, (xLoginWindow + 20, yUsernameBar - 30))

  # Password Field BLIT
  pygame.draw.rect(screen, listOfColor[7], (xLoginWindow + 20, yPasswordBar, 250, 25))
  screen.blit(lblPassword, (xLoginWindow + 20, yPasswordBar - 30))

  # The eye
  #screen.blit(imageEye, (xLoginWindow + 240, yPasswordBar + 1))

  # ------------Username Bar------------
  # Change the mouse appearance and call the click detector
  mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yUsernameBar, yUsernameBar + 25)
  if mouseSkinChanged:
    focusOnUsernameBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yUsernameBar, yUsernameBar + 25, tempIClicked)
  # CHANGE COLOR IF FOCUSED
  if focusOnUsernameBar:
    pygame.draw.rect(screen, lavanda, (xLoginWindow + 19, yUsernameBar - 1, 252, 27))
    pygame.draw.rect(screen, grey, (xLoginWindow + 20, yUsernameBar, 250, 25))
  
  mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yUsernameBar, yUsernameBar + 25)
  # ------------------------------------

  # ------------Password bar------------
  if not(mouseSkinChanged):
    mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yPasswordBar, yPasswordBar + 25)
    if mouseSkinChanged:
      focusOnPasswordBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yPasswordBar, yPasswordBar + 25, tempIClicked)
  # CHANGE COLOR IF FOCUSED
  if focusOnPasswordBar:
    pygame.draw.rect(screen, lavanda, (xLoginWindow + 19, yPasswordBar - 1, 252, 27))
    pygame.draw.rect(screen, grey, (xLoginWindow + 20, yPasswordBar, 250, 25))
    mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xLoginWindow + 20, xLoginWindow + 250, yPasswordBar, yPasswordBar + 25)
    #mouseSkinChanged = False
  # ------------------------------------
  
  # LOGIN Button
  pygame.draw.rect(screen, listOfColor[8], (xButtonLogin, yButtonLogin, 70, 30))
  screen.blit(lblButtonLogin, (xButtonLogin + 16, yButtonLogin + 5))
  if not(mouseSkinChanged):
    # Detect click button
    iPressedMyLoginButton, tempIClicked = mouseChanger.clickButtonDetect(xMouse, yMouse, xButtonLogin, xButtonLogin + 55, yButtonLogin, yButtonLogin + 30, tempIClicked)
    # Change button color
    mouseChanger.flyDetectorButtons(tempIClicked, listOfColor, 8, grey)

  else:
    iPressedMyLoginButton = False

  return iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked


# Draw all UI container
def drawUiBox(listOfColor):
  # File Bar Input
  pygame.draw.rect(screen, listOfColor[0], (xFileBar, yFileBar, widthBar, lengthBar))
  # Path list background
  pygame.draw.rect(screen, listOfColor[1], (xPathList, yPathList, widthListBar, lengthListPath))
  # Legend of Path List
  pygame.draw.rect(screen, listOfColor[2], (xPathList, yPathList, widthListBar, lengthListPath - 80))
  # Encrypt Button
  pygame.draw.rect(screen, listOfColor[3], (xEncryptButton, yEncrypButton, widthEncryptButton, lengthEncryptButton))
  # Decrypt Button
  pygame.draw.rect(screen, listOfColor[4], (xDecryptButton, yDecryptButton, widthDecryptButton, lengthDecryptButton))
  # Add Button
  pygame.draw.rect(screen, grey, (xAddButton, yAddButton, widthAddButton, lengthAddButton))
  # Arrow Of "Add Button"
  pygame.draw.rect(screen, listOfColor[9], (xFileBar + widthBar + 37, yFileBar + 12, 21, 2))
  pygame.draw.rect(screen, listOfColor[10], (xFileBar + widthBar + 47, yFileBar + 2.5, 2, 21))
  

def browserDialog(xDialogBrowser, yDialogBrowser):
  xCloseCircle = xDialogBrowser + widthDialogBrowser - 30
  yCloseCircle = yDialogBrowser + 2

  # Little grey border
  pygame.draw.rect(screen, grey, (xDialogBrowser - 1, yDialogBrowser - 1, widthDialogBrowser + 2, lengthDialogBrowser + 2))
  # Main Background
  pygame.draw.rect(screen, darkBlack, (xDialogBrowser, yDialogBrowser, widthDialogBrowser, lengthDialogBrowser))
  # Head Legend
  pygame.draw.rect(screen, whiteGrey, (xDialogBrowser, yDialogBrowser, widthDialogBrowser, 25))
  # Label : "Browser..."
  screen.blit(lblDialogBrowser, (xDialogBrowser + 3, yDialogBrowser + 3))
  # Close Circle
  screen.blit(imageCircle, (xCloseCircle, yCloseCircle))

  return xCloseCircle, yCloseCircle
  

# Draw main Title
def drawMainTitle():
  screen.blit(lblMainTitle, (xMainTitle, yMainTitle))


# Draw all Label
def drawUiLabel():
  # FILE label
  screen.blit(lblFile, (xFilelbl, yFilelbl))
  screen.blit(lblDecryptButton, (xDecryptButton + 14, yDecryptButton + 10))
  screen.blit(lblCryptButton, (xEncryptButton + 14, yEncrypButton + 10))
  screen.blit(lblAwaiting, (xPathList + 5, yFileBar + 60))
  screen.blit(lblStatus, (xPathList + 300, yFileBar + 60))


def showErrorMessage(myText):
  lblError = fontError.render(str(myText), True, red)
  screen.blit(lblError, (190, 400))

def drawImages():
  # USER ICON
  #screen.blit(imageUser, (10, 10))
  screen.blit(imageLock, (xEncryptButton + 25, yEncrypButton + 45))
  screen.blit(imageUnlock, (xDecryptButton + 25, yDecryptButton + 45))
  
# ------------------------------------------------------