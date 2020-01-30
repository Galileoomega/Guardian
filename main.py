#!/usr/bin/python3
import pygame, os, style, mouseChanger, pygame_textinput
pygame.init()

# Create textinput-object
textinput = pygame_textinput.TextInput()

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
loginIsOk = False
tempIClicked = True

# Login Window
lengthLoginWindow = 240
widthLoginWindow = 300
xLoginWindow = (xScreen / 2) - (widthLoginWindow / 2)
yLoginWindow = 150

# ----------------------------------------------------

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
    iPressedMyLoginButton, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked)

  if iPressedMyLoginButton:
    print(iPressedMyLoginButton)
  
  pygame.display.update()