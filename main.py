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
widthListBar = 300
xPathList = (xScreen / 2) - (widthListBar / 2)

xEncryptButton = 50
yEncrypButton = 400

yDecriptButton = 400
xDecryptButton = 340

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
white = (255,255,255)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
loginIsOk = True
iPressedMyEncryptButton = False
iPressedMyLoginButton = False
laal = False
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
  iPressedMyEncryptButton, laal = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 90, yEncrypButton, yEncrypButton + 40, laal)

  # 
  if iPressedMyEncryptButton:
    print(iPressedMyEncryptButton)

  if loginIsOk:
    # BOX
    style.drawUiBox()
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