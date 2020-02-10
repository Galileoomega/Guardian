#!/usr/bin/python3

#####################################################################################
########                      Guardian Main                                  ########
########                          v1.0                                       ########
#####################################################################################

# Catch error if the installation is not good
try:
  import pygame, os, style, mouseChanger, idVector, hashlib, cryptography, json, backModule
  from cryptography.fernet import Fernet
  playing = True
except ModuleNotFoundError:
  for u in range(0, 5):
    print("!! FATAL ERROR: You have to follow the installation instruction (README.md) !!")
  playing = False
  input()
pygame.init()

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
robotoRegularTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Regular.ttf')

# Change window name
pygame.display.set_caption("SHA-256")

# Changing default ICON
whiteSquarePNG = os.path.join(THIS_FOLDER, 'Resources\\white-square.png')
myIcon = pygame.image.load(whiteSquarePNG)
pygame.display.set_icon(myIcon)

# PYGAME INITIALISATION
xScreen = 500
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))
clock = pygame.time.Clock()

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
lavanda = (0, 115, 210)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey]

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
loginIsOk = False
tempEncryptButton = False
tempDecryptButton = False
wrongPass = False
stop = False
active = False

# OTHER
userPassword = ""
clipboard = ""
userUsername = ""
userFile = ""

# FONT 
font = pygame.font.Font(robotoRegularTTF, 15)
# ----------------------------------------------

while playing:

  # Set FPS
  clock.tick(120)

  # Refresh Window
  screen.fill(black)

  # Get Mouse Position
  xMouse, yMouse = pygame.mouse.get_pos()
  
  events = pygame.event.get()
  for event in events:
      if event.type == pygame.QUIT:
          exit()
  
  # Calling Front-End function
  style.drawMainTitle()

  #Calling Back-End function
  # Detect click on ENCRYPT BUTTON
  iPressedMyEncryptButton, tempEncryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 73, yEncrypButton, yEncrypButton + 40, tempEncryptButton)
  # Detect click on DECRYPT BUTTON
  iPressedMyDecryptButton, tempDecryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xDecryptButton, xDecryptButton + 73, yDecryptButton, yDecryptButton + 40, tempDecryptButton)
  
  mouseChanger.flyDetectorButtons(tempDecryptButton, listOfColor, 4)
  
  mouseChanger.flyDetectorButtons(tempEncryptButton, listOfColor, 3)

  # Get The Content Of The Clipboard
  clipboard = backModule.getContentOfClipboard()
  
  # DEBUG
  if iPressedMyEncryptButton:
    print(iPressedMyEncryptButton)

  if iPressedMyDecryptButton:
    print(iPressedMyDecryptButton)
  

  if loginIsOk:
    # BOX
    style.drawUiBox(listOfColor)
    # LABEL
    style.drawUiLabel()
    # IMAGES
    style.drawImages()

    # -----------FILE BAR-----------
    # Detect click On FILE BAR
    focusOnFileBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xFileBar, xFileBar + 250, yFileBar, yFileBar + 25, tempIClicked)
    # CHANGE COLOR IF FOCUSED
    if focusOnFileBar:
      pygame.draw.rect(screen, lavanda, (xFileBar - 1, yFileBar - 1, widthBar + 2, lengthBar + 2))
      pygame.draw.rect(screen, grey, (xFileBar, yFileBar, widthBar, lengthBar))
    # Detect overfly on FILE BAR
    mouseSkinChanged = mouseChanger.flyDetector(xMouse, yMouse, xFileBar, xFileBar + 250, yFileBar, yFileBar + 25)
    # TEXT INPUT FILE BAR
    if focusOnFileBar:
      for event in events:
        userFile = backModule.textInput(event, userFile)
    # Show the text input on the screen
    textinputFile = font.render(userFile, True, white)
    screen.blit(textinputFile, (xFileBar + 5, yFileBar + 3))
    # ------------------------------
  else:
    iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked)

  # --------------WINDOW LOGIN--------------
  if not(loginIsOk):
    # Check If Login is OK
    try:
      loginIsOk, wrongPass = idVector.confirmationLogin(userPassword, iPressedMyLoginButton)
    except TypeError:
      loginIsOk = idVector.confirmationLogin(userPassword, iPressedMyLoginButton)

    # Show An Error If the password is not correct
    if wrongPass:
      style.showErrorMessage("Invalid credentials...")

    # TEXT INPUT USERNAME
    if focusOnUsernameBar:
      for event in events:
        userUsername = backModule.textInput(event, userUsername)
    # Blit the text on the screen
    textinputUsername = font.render(userUsername, True, white)
    screen.blit(textinputUsername, (xLoginWindow + 25, yUsernameBar + 3))

    # TEXT INPUT PASSWORD
    if focusOnPasswordBar:
      for event in events:
        userPassword = backModule.secretTextInput(event, userPassword)
    # Blit the text on the screen
    textinputPassword = font.render(userPassword, True, white)
    screen.blit(textinputPassword, (xLoginWindow + 25, yPasswordBar + 3))
  # ---------------------------------------
  pygame.display.update()