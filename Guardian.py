#!/usr/bin/python3

#####################################################################################
########                      Guardian Main                                  ########
########                          v1.2                                       ########
#####################################################################################

# Catch error if the installation is not good
try:
  import pygame, os, hashlib, cryptography, json, style, mouseChanger, random
  from cryptography.fernet import Fernet
  from multiprocessing import Process
  from module import engine, backModule, idVector

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
clock = pygame.time.Clock()

# -------------------VARIABLE-------------------
# Position And Size
xScreen = 500
yScreen = 550

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

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
xDialogBrowser = (xScreen / 2) - (widthDialogBrowser / 2) - 10
yDialogBrowser = 100

# Blue Circle
xCloseCircle = xDialogBrowser + widthDialogBrowser - 30
yCloseCircle = yDialogBrowser + 2

xElement = int(xPathList) + 5
yElement = int(yPathList)

# ARROWS
leftArrow = 0
rightArrow = 0

# Color
black = (40, 40, 43)
lavanda = (0, 115, 210)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (57, 57, 60)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey, black, black]

# BOOL LOOP
tempIClicked = False
focusOnPasswordBar = focusOnUsernameBar = False
loginIsOk = False
tempEncryptButton = tempDecryptButton = False
tempCloseCircle = iPressedMyCircleButton = False
wrongPass = False
stop = False
active = False
tempIClickedAddButton = iPressedMyAddButton = False
showBrowser = False
needToDraw = False
finishedToDraw = True
makingAnimation = False
iPressedMyLeftArrow = tempCloseLeftArrow = False
tempCloseRightArrow = iPressedMyRightArrow = False
fullscreen = False

# OTHER
userPassword = ""
clipboard = ""
userUsername = ""
userFile = ""
hideUserPassword = ""
fileToEncrypt = [str]
listOfPath = []
xCycleAdding = xLoginWindow + widthLoginWindow / 2
xCycleRemoval = xLoginWindow + widthLoginWindow / 2
alpha = 0
separator = 10
myPath = THIS_FOLDER

# FONT 
font = pygame.font.Font(robotoRegularTTF, 15)
littleFont = pygame.font.Font(robotoRegularTTF, 12)

# DEFINE TEXT
errorPathList = littleFont.render("Maximum File", True, lavanda)
# ----------------------------------------------

while playing:

  # GET THE NEW WIDTH OF THE SCREEN
  xScreen, yScreen = pygame.display.get_surface().get_size()

  # Set FPS
  clock.tick(200)
  # Refresh Window
  screen.fill(black)
  # Get Mouse Position
  xMouse, yMouse = pygame.mouse.get_pos()

  # EVENTS
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.KEYDOWN:
        keyPress = True
    else:
        keyPress = False
    if event.type == pygame.QUIT:
        exit()
    # UPDATE The Size Of The Screen
    if event.type == pygame.VIDEORESIZE:
        scrsize = event.size  # or event.w, event.h
        screen = pygame.display.set_mode(scrsize,pygame.RESIZABLE)
        changed = True

    # ---------DETECT AN F11 TO PUT WINDOW IN FULLSCREEN---------
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
          modes = pygame.display.list_modes()
          if not modes:
            print ('16-bit not supported')
          else:
            print ('Found Resolution:', modes[0])
          screen = pygame.display.set_mode(modes[0], pygame.FULLSCREEN)
          xScreen, yScreen = modes[0]
        
        if event.key == pygame.K_ESCAPE:
          screen = pygame.display.set_mode((500, 550), pygame.RESIZABLE)
          xScreen = 500
          yScreen = 550
    # -----------------------------------------------------------
    
  # DRAW MAIN TITLE
  xMainTitle = style.drawMainTitle(xScreen, loginIsOk, xMainTitle)

  if not(makingAnimation):
    if loginIsOk:

      if not(showBrowser):
        # Detect click on ENCRYPT BUTTON
        iPressedMyEncryptButton, tempEncryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 73, yEncrypButton, yEncrypButton + 40, tempEncryptButton)
        # Detect click on DECRYPT BUTTON
        iPressedMyDecryptButton, tempDecryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xDecryptButton, xDecryptButton + 73, yDecryptButton, yDecryptButton + 40, tempDecryptButton)
        # Detect Click On "Add Button"
        iPressedMyAddButton, tempIClickedAddButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xAddButton, xAddButton + widthAddButton, yAddButton, yAddButton + lengthAddButton, tempIClickedAddButton)
      # Detect Click on blue circle (Browser Dialog)
      iPressedMyCircleButton, tempCloseCircle = mouseChanger.clickButtonDetect(xMouse, yMouse, xCloseCircle, xCloseCircle + 20, yCloseCircle, yCloseCircle + 20, tempCloseCircle)
      # Detect arrow press (LEFT)
      iPressedMyLeftArrow, tempCloseLeftArrow = mouseChanger.clickButtonDetect(xMouse, yMouse, leftArrow, leftArrow + 3, yDialogBrowser + 30, yDialogBrowser + 50, tempCloseLeftArrow)
      # Detect arrow press (RIGHT)
      iPressedMyRightArrow, tempCloseRightArrow = mouseChanger.clickButtonDetect(xMouse, yMouse, rightArrow, rightArrow + 3, yDialogBrowser + 30, yDialogBrowser + 50, tempCloseRightArrow)

      if not(showBrowser):
        # Change Button Color While pressed
        # Decrypt Button
        mouseChanger.flyDetectorButtons(tempDecryptButton, listOfColor, 4, grey)
        # Encrypt Button
        mouseChanger.flyDetectorButtons(tempEncryptButton, listOfColor, 3, grey)
        # Add Button
        mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 9, black)
        mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 10, black)

      # BOX
      xFileBar, xPathList, xEncryptButton, xDecryptButton, xAddButton, yDecryptButton, yEncrypButton = style.drawUiBox(listOfColor, xScreen, yScreen)
      # LABEL
      style.drawUiLabel(xScreen, xFileBar, xDecryptButton, xEncryptButton, xPathList, yEncrypButton, yDecryptButton)
      # IMAGES
      style.drawImages(xEncryptButton, xDecryptButton, yEncrypButton, yDecryptButton)
      # PATHS
      style.drawPath(myPath)

      if not(showBrowser):
        # -----------FILE BAR-----------
        # Detect click On FILE BAR
        focusOnFileBar, tempIClicked = mouseChanger.clickBarDetect(xMouse, yMouse, xFileBar, xFileBar + 250, yFileBar, yFileBar + 25, tempIClicked)

        # CHANGE COLOR IF FOCUSED
        if focusOnFileBar:
          style.AAfilledRoundedRect(screen, (xFileBar - 1, yFileBar - 1, widthBar + 2, lengthBar + 2), lavanda, 0.1)
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

      # Openning File Browser
      if iPressedMyAddButton:
        iPressedMyAddButton = False
        myPath = THIS_FOLDER
        showBrowser = True
        # Initialize the File Browser
        xCloseCircle, yCloseCircle, leftArrow, rightArrow = style.browserDialog(xDialogBrowser, yDialogBrowser)

      # ------------------The File Browser Window------------------
      if showBrowser:
        xCloseCircle, yCloseCircle, leftArrow, rightArrow = style.browserDialog(xDialogBrowser, yDialogBrowser)
        if iPressedMyLeftArrow:
          myPath = backModule.popPathElement(myPath)
        
        separator = backModule.listDirectory(separator, xDialogBrowser, yDialogBrowser, myPath)

        # Closing the window 
        if iPressedMyCircleButton:
          showBrowser = False
      # ----------------------------------------------------------

      # -----------LIST OF PATH--------------
      # 6 is equal of the number of file simultaneously
      if len(listOfPath) >= 6: 
        screen.blit(errorPathList, (xElement, yPathList + lengthListPath + 10))

      for u in range(0, len(listOfPath)):
        yElement = u * 12 + yPathList + 20
        u = littleFont.render(listOfPath[u], True, white)
        screen.blit(u, (xElement, yElement))
      # -------------------------------------

  # ------------------WINDOW LOGIN------------------
  if not(loginIsOk):

    # Background Of Window Login
    xLoginWindow = (xScreen / 2) - (widthLoginWindow / 2)
    iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked, xLoginWindow, yLoginWindow)

    for event in events:
      if event.type == pygame.KEYDOWN:
        if pygame.key.name(event.key) == "enter":
          iPressedMyLoginButton = True
        if event.key == pygame.K_RETURN:
          iPressedMyLoginButton = True
    # ---------LINES SIMULATION----------
    #if iPressedMyLoginButton:
    #  needToDraw = True
    #if needToDraw:
    #  finishedToDraw = engine.renderLineSimulation(screen, 40, random.randint(200, 300), 1)
    #  finishedToDraw2 = engine.renderLineSimulation(screen, -100, random. randint(0, 100), 2)
    #  if finishedToDraw:
    #    if finishedToDraw2:
    #      needToDraw = False
    # -----------------------------------
    
    # Check If Login is OK
    try:
      loginIsOk, wrongPass = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)
    except TypeError:
      loginIsOk = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)

    if loginIsOk:
      makingAnimation = True

    # Show An Error If the password is not correct
    if wrongPass:
      style.showErrorMessage("Invalid credentials...", xScreen / 2 - 55)

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
  # ------------------------------------------------

  if makingAnimation:
    if loginIsOk:
      xCycleAdding = xLoginWindow + widthLoginWindow / 2
      xCycleRemoval = xLoginWindow + widthLoginWindow / 2
    loginIsOk = False

    makingAnimation, xCycleAdding, xCycleRemoval, xLoginWindow, alpha = style.loginLoading(xCycleAdding, xCycleRemoval, xLoginWindow, alpha, xScreen, yScreen, yLoginWindow)
    if not(makingAnimation):
      loginIsOk = True

  
  pygame.display.update()