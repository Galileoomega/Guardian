#!/usr/bin/python3
import pygame, os, style, mouseChanger, pygame_textinput
pygame.init()

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Change window name
pygame.display.set_caption("SHA-256")

# Changing default ICON
whiteSquarePNG = os.path.join(THIS_FOLDER, 'Resources\\white-square.png')
myIcon = pygame.image.load(whiteSquarePNG)
pygame.display.set_icon(myIcon)

# PYGAME INITIALISATION
xScreen = 450
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))
clock = pygame.time.Clock()

# ----------------------VARIABLE----------------------
black = (40, 40, 43)
grey = (67, 67, 70)
loginIsOk = False
tempIClicked = True

# Login Window
lengthLoginWindow = 240
widthLoginWindow = 300
xLoginWindow = (xScreen / 2) - (widthLoginWindow / 2)
yLoginWindow = 150

yUsernameBar = yLoginWindow + 70
yPasswordBar = yLoginWindow + 140

yButtonLogin = (yLoginWindow + lengthLoginWindow) - 50
xButtonLogin = xLoginWindow + (widthLoginWindow / 2) - 35

# ----------------------------------------------------

# Create textinput-object
textinputUsername = pygame_textinput.TextInput("", "", 25, True, (255,255,255), grey)
textinputPassword = pygame_textinput.TextInput("", "", 25, True, (255,255,255), grey)


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

  if loginIsOk:
    style.drawUiBox()
    style.drawUiLabel()
  else:
    iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked)

  # CHECK IF THE LOGIN IS CORRECT BACKEND ?
  if iPressedMyLoginButton:
    loginIsOk = True

  if not(loginIsOk):
    # TEXT INPUT USERNAME
    if focusOnUsernameBar:
      # Feed it with events every frame
      textinputUsername.update(events)
    # Blit its surface onto the screen
    screen.blit(textinputUsername.get_surface(), (xLoginWindow + 25, yUsernameBar + 4))

    # TEXT INPUT PASSWORD
    if focusOnPasswordBar:
      # Feed it with events every frame
      textinputPassword.update(events)
      
    # Blit its surface onto the screen
    screen.blit(textinputPassword.get_surface(), (xLoginWindow + 25, yPasswordBar + 4))
  
  pygame.display.update()