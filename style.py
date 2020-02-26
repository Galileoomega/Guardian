# FRONT END but call some BACK-END function
from pygame import *
import os, mouseChanger, pygame, re
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
leftArrow = xDialogBrowser + widthDialogBrowser - 70
rightArrow = xDialogBrowser + widthDialogBrowser - 30

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

    rect         = Rect(rect)
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

def loginLoading(xCycleAdding, xCycleRemoval, xLoginWindow, alpha):

  if not(int(xCycleAdding) == widthLoginWindow / 2 - 42):
    pygame.draw.line(screen, lavanda, (xLoginWindow + (widthLoginWindow / 2), yLoginWindow), (xCycleAdding, yLoginWindow), 3)
    pygame.draw.line(screen, lavanda, (xLoginWindow + (widthLoginWindow / 2), yLoginWindow), (xCycleRemoval, yLoginWindow), 3)

    if xCycleAdding > 250 - 50:
      xCycleAdding -= 0.8
    else:
      xCycleAdding -= 1.3
    
    if xCycleRemoval < 250 + 50:
      xCycleRemoval += 0.8
    else:
      xCycleRemoval += 1.3

    makingAnimation = True
    xCycleRemoval = xCycleRemoval
    xCycleAdding = xCycleAdding

    ##############################
  if xCycleAdding < 200:
    alpha += 2.5
    s = pygame.Surface((xScreen,yScreen))  # the size of your rect
    s.set_alpha(alpha)              # alpha level
    s.fill(black)           # this fills the entire surface
    screen.blit(s, (0,50))

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
  
  # LOGIN Button
  AAfilledRoundedRect(screen, (xButtonLogin, yButtonLogin, 70, 30), listOfColor[8], 0.2)
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
  AAfilledRoundedRect(screen, (xFileBar, yFileBar, widthBar, lengthBar), listOfColor[0], 0.4)
  # Path list background
  pygame.draw.rect(screen, listOfColor[1], (xPathList, yPathList, widthListBar, lengthListPath))
  # Legend of Path List
  pygame.draw.rect(screen, listOfColor[2], (xPathList, yPathList, widthListBar, lengthListPath - 80))
  # Encrypt Button
  AAfilledRoundedRect(screen, (xEncryptButton, yEncrypButton, widthEncryptButton, lengthEncryptButton), listOfColor[3], 0.2)
  # Decrypt Button
  AAfilledRoundedRect(screen, (xDecryptButton, yDecryptButton, widthDecryptButton, lengthDecryptButton), listOfColor[4], 0.2)
  # Add Button
  AAfilledRoundedRect(screen, (xAddButton, yAddButton, widthAddButton, lengthAddButton), grey, 0.5)
  # Arrow Of "Add Button"
  pygame.draw.rect(screen, listOfColor[9], (xFileBar + widthBar + 37, yFileBar + 12, 21, 2))
  pygame.draw.rect(screen, listOfColor[10], (xFileBar + widthBar + 47, yFileBar + 2.5, 2, 21))
  
# FILE BROWSER: FILE OPENNING (BACKGROUND)
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
  # ARROWS
  leftArrow = xDialogBrowser + widthDialogBrowser - 60
  rightArrow = xDialogBrowser + widthDialogBrowser - 30
  screen.blit(imageRightArrow, (rightArrow, yDialogBrowser + 30))
  screen.blit(imageLeftArrow, (leftArrow, yDialogBrowser + 30))

  return xCloseCircle, yCloseCircle, leftArrow, rightArrow
  
# FILE BROWSER: FILE OPENNING (INSIDE)
def browserDialogContent(element, separator, xDialogBrowser, yDialogBrowser):
  lblElement = fontText.render(str(element), True, halfWhite)

  # ---SEE If Its A Folder---
  x = re.search("\.", element)
  if not(x):
    screen.blit(imageFolder, (xDialogBrowser + 5, yDialogBrowser + separator + 48))
  else:
    screen.blit(imageFile, (xDialogBrowser + 5, yDialogBrowser + separator + 49))
  #---------------------------

  # FILES NAME
  screen.blit(lblElement, (xDialogBrowser + 30, yDialogBrowser + separator + 50))
  # THE LINE BEETWEEN THE FILES
  pygame.draw.aaline(screen, black, (xDialogBrowser + 28, yDialogBrowser + 56), (xDialogBrowser + widthDialogBrowser - 20, yDialogBrowser + 56), 2)
  pygame.draw.aaline(screen, black, (xDialogBrowser + 28, yDialogBrowser + separator + 70), (xDialogBrowser + widthDialogBrowser - 20, yDialogBrowser + separator + 70), 2)
  
  return separator

# Draw main Title
def drawMainTitle():
  screen.blit(lblMainTitle, (xMainTitle, yMainTitle))

# Draw all Label
def drawUiLabel():
  # FILE label
  screen.blit(lblFile, (xFilelbl, yFilelbl))
  screen.blit(lblDecryptButton, (xDecryptButton + 16, yDecryptButton + 11))
  screen.blit(lblCryptButton, (xEncryptButton + 16, yEncrypButton + 11))
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