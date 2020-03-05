# FRONT END but call some BACK-END function
from pygame import *
import os, mouseChanger, pygame, re
from module import gradient
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

# FILE BROWSER: Arrows
leftArrow = xFileBar + 385
rightArrow = xFileBar + 415

xHouseIcon = xFileBar + 400

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
imageFolderPath = os.path.join(THIS_FOLDER, 'Resources\\folder-invoices.png')
imageFilePath = os.path.join(THIS_FOLDER, 'Resources\\file-image.png')
imageHousePATH = os.path.join(THIS_FOLDER, 'Resources\\house.png')
imageRightArrowPath = os.path.join(THIS_FOLDER, 'Resources\\right-arrow.png')
imageLeftArrowPath = os.path.join(THIS_FOLDER, 'Resources\\left-arrow.png')


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
imageFolder = pygame.image.load(imageFolderPath)
imageFile = pygame.image.load(imageFilePath)
imageHouse = pygame.image.load(imageHousePATH)
imageRightArrow = pygame.image.load(imageRightArrowPath)
imageLeftArrow = pygame.image.load(imageLeftArrowPath)


# OTHER
separator = 10

# -----------------------FUNCTION-----------------------

# Draw rounded box
def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

def loginLoading(xCycleAdding, xCycleRemoval, xLoginWindow, alpha, xScreen, yScreen, yLoginWindow):

  if not(int(xCycleAdding) == widthLoginWindow / 2 - 42):
    pygame.draw.line(screen, lavanda, (xLoginWindow + (widthLoginWindow / 2), yLoginWindow), (xCycleAdding, yLoginWindow), 3)
    pygame.draw.line(screen, lavanda, (xLoginWindow + (widthLoginWindow / 2), yLoginWindow), (xCycleRemoval, yLoginWindow), 3)

    if xCycleAdding > xLoginWindow + 10:
      if xCycleAdding > xLoginWindow + widthLoginWindow / 2 - 50:
        xCycleAdding -= 0.9
      else:
        xCycleAdding -= 2
    
    if xCycleRemoval < xLoginWindow + widthLoginWindow - 10:
      if xCycleRemoval < xLoginWindow + widthLoginWindow / 2 + 50:
        xCycleRemoval += 0.9
      else:
        xCycleRemoval += 2

    makingAnimation = True

  if xCycleAdding < xLoginWindow + widthLoginWindow / 2 - 50:
    alpha += 3
    s = pygame.Surface((320, 300))  # the size of your rect
    s.set_alpha(alpha)              # alpha level
    s.fill(black)           # this fills the entire surface
    screen.blit(s, (xLoginWindow - 10, yLoginWindow - 10)) # NEED TO BE CHANGED

    if alpha >= 300:
      makingAnimation = False
    else:
      makingAnimation = True

  return makingAnimation, xCycleAdding, xCycleRemoval, xLoginWindow, alpha

# First render when program is open (WINDOW LOGIN)
def loginWindow(xMouse, yMouse, tempIClicked, xLoginWindow, yLoginWindow):
  focusOnPasswordBar = False
  focusOnUsernameBar = False

  # BACKGROUND BLIT
  AAfilledRoundedRect(screen, (xLoginWindow, yLoginWindow, widthLoginWindow, lengthLoginWindow), listOfColor[5], 0.1)

  # UserName Field BLIT
  AAfilledRoundedRect(screen, (xLoginWindow + 20, yUsernameBar, 250, 25), listOfColor[6], 0.2)
  screen.blit(lblUsername, (xLoginWindow + 20, yUsernameBar - 30))

  # Password Field BLIT
  AAfilledRoundedRect(screen, (xLoginWindow + 20, yPasswordBar, 250, 25), listOfColor[7], 0.2)
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
  
  # ---------------LOGIN Button---------------
  xButtonLogin = xLoginWindow + (widthLoginWindow / 2) - 35
  AAfilledRoundedRect(screen, (xButtonLogin, yButtonLogin, 70, 30), listOfColor[8], 0.2)
  screen.blit(lblButtonLogin, (xButtonLogin + 16, yButtonLogin + 5))
  if not(mouseSkinChanged):
    # Detect click button
    iPressedMyLoginButton, tempIClicked = mouseChanger.clickButtonDetect(xMouse, yMouse, xButtonLogin, xButtonLogin + 55, yButtonLogin, yButtonLogin + 30, tempIClicked)
    # Change button color
    mouseChanger.flyDetectorButtons(tempIClicked, listOfColor, 8, grey)
  else:
    iPressedMyLoginButton = False
  # ------------------------------------------

  return iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked

# Draw all UI container
def drawUiBox(listOfColor, xScreen, yScreen):
  # --------Update Var Location--------
  xFileBar = 90
  xPathList = (xScreen / 2) - (widthListBar / 2)

  xEncryptButton = 70
  yEncrypButton = yScreen - lengthEncryptButton - 80

  xDecryptButton = 40 + widthEncryptButton + 190
  yDecryptButton = yScreen - lengthDecryptButton - 80

  xAddButton = xFileBar + widthBar + 35
  # -----------------------------------

  # File Bar Input
  AAfilledRoundedRect(screen, (xFileBar, yFileBar, widthBar, lengthBar), listOfColor[0], 0.4)
  # Vertical Separator
  pygame.draw.aaline(screen, grey, (xFileBar + 380, 30), (xFileBar + 380, yScreen - 30), 2)
  # Encrypt Button
  AAfilledRoundedRect(screen, (xEncryptButton, yEncrypButton, widthEncryptButton, lengthEncryptButton), listOfColor[3], 0.2)
  # Decrypt Button
  AAfilledRoundedRect(screen, (xDecryptButton, yDecryptButton, widthDecryptButton, lengthDecryptButton), listOfColor[4], 0.2)
  # Add Button
  AAfilledRoundedRect(screen, (xAddButton, yAddButton, widthAddButton, lengthAddButton), grey, 0.5)
  # Arrow Of "Add Button"
  pygame.draw.rect(screen, listOfColor[9], (xFileBar + widthBar + 37, yFileBar + 12, 21, 2))
  pygame.draw.rect(screen, listOfColor[10], (xFileBar + widthBar + 47, yFileBar + 2.5, 2, 21))

  return xFileBar, xPathList, xEncryptButton, xDecryptButton, xAddButton, yDecryptButton, yEncrypButton
  
# Draw main Title
def drawMainTitle(xScreen, loginIsOk, xMainTitle):
  # Main LABEL
  yMainTitle = 20
  if loginIsOk:
    xMainTitle = 150
  else:
    xMainTitle = (xScreen / 2) - 90

  screen.blit(lblMainTitle, (xMainTitle, yMainTitle))
  return xMainTitle

# Draw all Label
def drawUiLabel(xScreen, xFilelbl, xDecryptButton, xEncryptButton, xPathList, yEncrypButton, yDecryptButton):
  # --------Update Var Location--------
  # -----------------------------------

  # FILE label
  screen.blit(lblFile, (xFilelbl - 40, yFilelbl))
  screen.blit(lblDecryptButton, (xDecryptButton + 16, yDecryptButton + 11))
  screen.blit(lblCryptButton, (xEncryptButton + 16, yEncrypButton + 11))
  screen.blit(lblAwaiting, (xFileBar - 50, yFileBar + 80))
  screen.blit(lblStatus, (xFileBar + 250, yFileBar + 80))

# Draw the TOP PATH
def drawPath(myPath, xHouseIcon, xScreen):  

  # THE PATH
  lblMyPath = fontError.render(str(myPath), True, halfWhite)
  screen.blit(lblMyPath, (xHouseIcon + 30, 46))

# SHOW AN ERROR MESSAGE WHEN CREDENTIALS ARE WRONG
def showErrorMessage(myText, xScreen):
  lblError = fontError.render(str(myText), True, red)
  screen.blit(lblError, (xScreen, 400))

def drawImages(xEncryptButton, xDecryptButton, yEncrypButton, yDecryptButton, xHouseIcon, xFileBar, xScreen):

  # Draw a rectangle for scrolling files
  pygame.draw.rect(screen, black, (xFileBar + 410, 0, xScreen, 80))

  # FILE BROWSER: Arrows
  leftArrow = xFileBar + 405
  rightArrow = xFileBar + 435

  # Locker Image For Encrypt/Decrypt buttons
  screen.blit(imageLock, (xEncryptButton + 25, yEncrypButton + 45))
  screen.blit(imageUnlock, (xDecryptButton + 25, yDecryptButton + 45))

  # ARROWS for path navigation
  screen.blit(imageLeftArrow, (leftArrow, 45))
  screen.blit(imageRightArrow, (rightArrow, 45))

  # THE HOUSE ICON
  xHouseIcon = xFileBar + 470
  screen.blit(imageHouse, (xHouseIcon, 45))

  return xHouseIcon
  
# ------------------------------------------------------