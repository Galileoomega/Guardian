#!/usr/bin/python3
import pygame, os, style, mouseChanger, pygame_textinput, idVector
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
listOfColor = [grey, grey, whiteGrey, grey, grey]

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
loginIsOk = False
tempEncryptButton = False
tempDecryptButton = False
# ----------------------------------------------

# Create textinput-object
textinputUsername = pygame_textinput.TextInput("", robotoRegularTTF, 17, True, (255,255,255), grey)
textinputPassword = pygame_textinput.TextInput("", robotoRegularTTF, 17, True, (255,255,255), grey)


while True:

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
  iPressedMyEncryptButton, tempEncryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 90, yEncrypButton, yEncrypButton + 40, tempEncryptButton)
  # Detect click on DECRYPT BUTTON
  iPressedMyDecryptButton, tempDecryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xDecryptButton, xDecryptButton + 90, yDecryptButton, yDecryptButton + 40, tempDecryptButton)

  mouseChanger.flyDetectorButtons(tempDecryptButton, listOfColor, 4)

  # DEBUG
  if iPressedMyEncryptButton:
    print(iPressedMyEncryptButton)
  
  if iPressedMyDecryptButton:
    print(iPressedMyDecryptButton)

  if loginIsOk:
    # BOX
    style.drawUiBox(listOfColor)
    # LABEL
    style.drawUiLabel(textinputUsername.get_text())
    # IMAGES
    style.drawImages()
  else:
    iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked)

  # Check If Login is OK
  loginIsOk = idVector.confirmationLogin(iPressedMyLoginButton)

  if not(loginIsOk):
    # TEXT INPUT USERNAME
    if focusOnUsernameBar:
      # Feed it with events every frame
      textinputUsername.update(events)
    # Blit its surface onto the screen
    screen.blit(textinputUsername.get_surface(), (xLoginWindow + 25, yUsernameBar + 2))

    # TEXT INPUT PASSWORD
    if focusOnPasswordBar:
      # Feed it with events every frame
      textinputPassword.update(events)

    # Blit its surface onto the screen
    screen.blit(textinputPassword.get_surface(), (xLoginWindow + 25, yPasswordBar + 2))
  
  pygame.display.update()