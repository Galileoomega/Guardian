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

xElement = int(xPathList) + 5
yElement = int(yPathList)

# Color
black = (40, 40, 43)
lavanda = (0, 115, 210)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey, black, black]

tempIClicked = False
focusOnPasswordBar = False
focusOnUsernameBar = False
loginIsOk = False
tempEncryptButton = False
tempDecryptButton = False
wrongPass = False
stop = False
active = False
tempIClickedAddButton = False
iPressedMyAddButton = False

# OTHER
userPassword = ""
clipboard = ""
userUsername = ""
userFile = ""
hideUserPassword = ""
fileToEncrypt = [str]
listOfPath = []

# FONT 
font = pygame.font.Font(robotoRegularTTF, 15)
littleFont = pygame.font.Font(robotoRegularTTF, 12)

# DEFINE TEXT
errorPathList = littleFont.render("Maximum File", True, lavanda)
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

  if loginIsOk:

    # Detect click on ENCRYPT BUTTON
    iPressedMyEncryptButton, tempEncryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 73, yEncrypButton, yEncrypButton + 40, tempEncryptButton)
    # Detect click on DECRYPT BUTTON
    iPressedMyDecryptButton, tempDecryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xDecryptButton, xDecryptButton + 73, yDecryptButton, yDecryptButton + 40, tempDecryptButton)
    # Detect Click On "Add Button"
    iPressedMyAddButton, tempIClickedAddButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xAddButton, xAddButton + widthAddButton, yAddButton, yAddButton + lengthAddButton, tempIClickedAddButton)


    # Change Button Color While pressed
    # Decrypt Button
    mouseChanger.flyDetectorButtons(tempDecryptButton, listOfColor, 4, grey)
    # Encrypt Button
    mouseChanger.flyDetectorButtons(tempEncryptButton, listOfColor, 3, grey)
    # Add Button
    mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 9, black)
    mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 10, black)

    # DEBUG
    if iPressedMyEncryptButton:
      print(iPressedMyEncryptButton)

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
        userFile = backModule.textInput(event, userFile, lengthBar)

    # Show the text input on the screen
    textinputFile = font.render(userFile, True, white)
    screen.blit(textinputFile, (xFileBar + 5, yFileBar + 3))
    # ------------------------------

    # ---------ADDING VALUE TO LIST---------
    if iPressedMyAddButton:
      # Check if theres is no more than 6 value
      if not(len(listOfPath) == 6):
        listOfPath.append(userFile)

    if len(listOfPath) >= 6: 
      screen.blit(errorPathList, (xElement, yPathList + lengthListPath + 10))

    for u in range(0, len(listOfPath)):
      yElement = u * 12 + yPathList + 20
      u = littleFont.render(listOfPath[u], True, white)
      screen.blit(u, (xElement, yElement))
    # -------------------------------------

  else:
    # Background Of Window Login
    iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked)

  # --------------WINDOW LOGIN--------------
  if not(loginIsOk):
    # Check If Login is OK
    try:
      loginIsOk, wrongPass = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)
    except TypeError:
      loginIsOk = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)

    # Show An Error If the password is not correct
    if wrongPass:
      style.showErrorMessage("Invalid credentials...")

    # TEXT INPUT USERNAME
    if focusOnUsernameBar:
      for event in events:
        userUsername = backModule.textInput(event, userUsername, 100)
    # Blit the text on the screen
    textinputUsername = font.render(userUsername, True, white)
    screen.blit(textinputUsername, (xLoginWindow + 25, yUsernameBar + 3))

    # TEXT INPUT PASSWORD
    if focusOnPasswordBar:
      for event in events:
        userPassword, hideUserPassword = backModule.secretTextInput(event, userPassword, hideUserPassword)
    # Blit the text on the screen
    textinputPassword = font.render(hideUserPassword, True, white)
    screen.blit(textinputPassword, (xLoginWindow + 25, yPasswordBar + 3))
  # ----------------------------------------
  pygame.display.update()