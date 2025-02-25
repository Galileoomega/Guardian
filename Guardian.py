#!/usr/bin/python3

#####################################################################################
########                      Guardian Main                                  ########
########                          v1.2                                       ########
#####################################################################################

import os, hashlib, json, style, mouseChanger, random
import cryptography
from cryptography.fernet import Fernet
from multiprocessing import Process
from module import engine, backModule, idVector, fileDir, controller, timeVar
from importlib import reload
import pygame
from pygame.locals import *

playing = True
pygame.init()

pygame.event.set_blocked(pygame.MOUSEMOTION)

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
robotoRegularTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Regular.ttf')

# Change window name
pygame.display.set_caption("Guardian")

# Changing default ICON
whiteSquarePNG = os.path.join(THIS_FOLDER, 'Resources\\white-square.png')
myIcon = pygame.image.load(whiteSquarePNG)
pygame.display.set_icon(myIcon)

# PYGAME INITIALISATION
clock = pygame.time.Clock()

# -------------------VARIABLE-------------------
# Position And Size
xScreen = 750
yScreen = 550


flags = RESIZABLE | DOUBLEBUF | HWSURFACE
flags2 = FULLSCREEN | DOUBLEBUF | HWSURFACE

screen = pygame.display.set_mode((xScreen, yScreen), flags)

screen.set_alpha(None)

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

# FILE BROWSER: Arrows
leftArrow = xFileBar + 385
rightArrow = xFileBar + 415

xHouseIcon = xFileBar + 400

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
tempFileButtons = False
iPressedMyFiles = False
tempFileButtons0 = False
tempFileButtons1 = False
needToBuildMyFile = True
iPressedMyLogOutButton = False
tempLogOutButton = False
showSettingsMenu = False
iPressedMenuOption1 = False
iPressedMenuOption2 = False
iPressedMenuOption3 = False
tempMenuOption1 = False
tempMenuOption2 = False
tempMenuOption3 = False

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
myPath = myPath.capitalize()
xCell = 520
yCell = 100
listDir = []
scrollMarker = 0
yCellList = []
lenOfBoxesOfFiles = 200
activeFile = ''
oldTime = 0
oneTap = False
tempActiveFile = ""
listOfPendingFiles = []
nameOfPendingFiles = []
actualFile = ""
needToShowSuccessMessage = False
timeDelay = 0

# FONT 
font = pygame.font.Font(robotoRegularTTF, 15)
littleFont = pygame.font.Font(robotoRegularTTF, 12)

# DEFINE TEXT
errorPathList = littleFont.render("Maximum File", True, lavanda)
# ----------------------------------------------

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text

def logout():
  loginIsOk = False
  showSettingsMenu = False


while playing:

  # GET THE NEW WIDTH OF THE SCREEN
  xScreen, yScreen = pygame.display.get_surface().get_size()

  # Set FPS
  clock.tick(90)
  # Refresh Window
  screen.fill(black)
  # Get Mouse Position
  xMouse, yMouse = pygame.mouse.get_pos()
  # Get Time Value
  time = pygame.time.get_ticks()

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
        screen = pygame.display.set_mode(scrsize,flags)
        changed = True

    # ---------DETECT AN F11/ESCAPE TO PUT WINDOW IN FULLSCREEN---------
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
          modes = pygame.display.list_modes()
          screen = pygame.display.set_mode(modes[0], flags2)
          xScreen, yScreen = modes[0]
        
        if event.key == pygame.K_ESCAPE:
          screen = pygame.display.set_mode((xScreen, yScreen), flags)
          xScreen = 750
          yScreen = 550
    # -----------------------------------------------------------

  # --------------------------HOME SCREEN--------------------------
  if not(showSettingsMenu):
    if not(makingAnimation):
      if loginIsOk:
        
        # Detect click on ENCRYPT BUTTON
        iPressedMyEncryptButton, tempEncryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xEncryptButton, xEncryptButton + 73, yEncrypButton, yEncrypButton + 40, tempEncryptButton)
        # Detect click on DECRYPT BUTTON
        iPressedMyDecryptButton, tempDecryptButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xDecryptButton, xDecryptButton + 73, yDecryptButton, yDecryptButton + 40, tempDecryptButton)
        # Detect Click On "Add Button"
        iPressedMyAddButton, tempIClickedAddButton = mouseChanger.clickButtonDetect(xMouse, yMouse, xAddButton, xAddButton + widthAddButton, yAddButton, yAddButton + lengthAddButton, tempIClickedAddButton)
        # Detect clcik on LOGOUT BUTTON
        iPressedMyLogOutButton, tempLogOutButton = mouseChanger.clickButtonDetect(xMouse, yMouse, 20, 30, 20, 50, tempLogOutButton)
        # FILE BROWSER: Arrows
        leftArrow = xFileBar + 405
        rightArrow = xFileBar + 435
        # Detect arrow press (LEFT)
        iPressedMyLeftArrow, tempCloseLeftArrow = mouseChanger.clickButtonDetect(xMouse, yMouse, leftArrow, leftArrow + 20, 45, 65, tempCloseLeftArrow)
        # Detect arrow press (RIGHT)
        iPressedMyRightArrow, tempCloseRightArrow = mouseChanger.clickButtonDetect(xMouse, yMouse, rightArrow, rightArrow + 10, 45, 65, tempCloseRightArrow)
        
        # ------------Change Button Color While pressed------------
        # Decrypt Button
        mouseChanger.flyDetectorButtons(tempDecryptButton, listOfColor, 4, grey)
        # Encrypt Button
        mouseChanger.flyDetectorButtons(tempEncryptButton, listOfColor, 3, grey)
        # Add Button
        mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 9, black)
        mouseChanger.flyDetectorButtons(tempIClickedAddButton, listOfColor, 10, black)
        # ---------------------------------------------------------

        # BOX
        xFileBar, xPathList, xEncryptButton, xDecryptButton, xAddButton, yDecryptButton, yEncrypButton = style.drawUiBox(listOfColor, xScreen, yScreen, xMainTitle)
        # LABEL
        style.drawUiLabel(xScreen, xFileBar, xDecryptButton, xEncryptButton, xPathList, yEncrypButton, yDecryptButton)
        
        # ----------LISTING ALL FILES----------
        try:
          listDir, xCell, yCell, yCellList, lenOfBoxesOfFiles, activeFiles, oneTap, tempActiveFile = fileDir.listingFiles(myPath, xCell, yCell, xScreen, scrollMarker, xMouse, yMouse, yCellList, oneTap, tempActiveFile)
        except FileNotFoundError:
          print("ERROR CATCHED: FileNotFoundError at line 280")
          myPath = fileDir.popPathElement(myPath)
          myPath = fileDir.popPathElement(myPath)
          listDir, xCell, yCell, yCellList, lenOfBoxesOfFiles, activeFiles, oneTap, tempActiveFile = fileDir.listingFiles(myPath, xCell, yCell, xScreen, scrollMarker, xMouse, yMouse, yCellList, oneTap, tempActiveFile)
        # -------------------------------------

        # --------Build the file wich contain all click controller--------
        if needToBuildMyFile:
          if yCellList == []:
            yCellList = [10]
          fileDir.buildController(yCellList)
          needToBuildMyFile = False
        # ----------------------------------------------------------------

        # ------------ Detect all click on the file ------------
        controller = reload(controller)
        timeVar.time = pygame.time.get_ticks()
        timeVar.myPath = myPath
        controller.filesClickDetector(xCell, yCellList, xMouse, yMouse, lenOfBoxesOfFiles, time)
        # ------------------------------------------------------

        # -----------GO INTO A FOLDER WHEN DOUBLE CLICK-----------
        x = fileDir.folderType(myPath + "\\" + timeVar.fileName)
        if not(x):
          if timeVar.clickState == "double":
              # Will allow to update the content of the new folder
              needToBuildMyFile = True
              
              # Reset the scroll orientation 
              scrollMarker = 0
              
              # Update the name of the file wich has been clicked
              try:
                timeVar.fileName = listDir[int(activeFiles[-1])]
              except IndexError:
                print("ERROR CATCHED : listDir() : ", listDir, "with index : ", activeFiles, "[-1]")
                pass
              
              if myPath == "C:\\":
                myPath = myPath[:-1]

              timeVar.text = myPath

              myPath += "\\" + timeVar.fileName
              timeVar.clickState = ""
              pygame.time.delay(70)

          if fileDir.folderType(myPath):
            myPath = fileDir.popPathElement(myPath)
            print("DELETED")
          timeVar.text = myPath
        # --------------------------------------------------------

        # ----------DETECT SCROLL MOUSE----------
        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN:
            # SCROLL UP
            if event.button == 5:
              scrollMarker += 15
            # SCROLL DOWN
            if event.button == 4:
              scrollMarker -= 15
            
          if scrollMarker < 0:
            scrollMarker = 0
        # ---------------------------------------

        # --------- CHANGING DIRECTORY ---------
        if iPressedMyLeftArrow:
          # Will allow to update the content of the new folder
          needToBuildMyFile = True
          
          yCellList = []
          myPath = fileDir.popPathElement(myPath)
        # --------------------------------------

        # IMAGES
        xHouseIcon = style.drawImages(xEncryptButton, xDecryptButton, yEncrypButton, yDecryptButton, xHouseIcon, xFileBar, xScreen)

        # PATHS
        style.drawPath(myPath, xHouseIcon, xScreen)

        # ------ DECLARE A VAR WICH CONTAIN THE ACTIVE BUTTON ------
        if activeFiles == None or activeFiles == "":
          pass
        else:
          index = int(activeFiles[-1])
          actualFile = listDir[index]
        # ---------------------------------------------------------

        # ----------LISTING ALL PENDING FILES----------
        # Display the awaiting files on the screen
        fileDir.listPendingFiles(nameOfPendingFiles)
        # ---------------------------------------------

        # ADDING PATH TO WAIT LIST
        if actualFile != "":
          if iPressedMyAddButton:
            if not(actualFile in nameOfPendingFiles):
              nameOfPendingFiles.append(timeVar.activeFile)
              actualFile = ""
              if timeVar.fileOnFocusPath != "":
                listOfPendingFiles.append(timeVar.fileOnFocusPath)
              timeVar.fileOnFocusPath = ""
        
        # ------------------ ENCRYPT/DECRYPT ALL PENDING FILES ------------------
        if len(listOfPendingFiles) > 0:
          if iPressedMyEncryptButton:
            idVector.encryptFiles(listOfPendingFiles, userPassword)
            # Reset pending files
            listOfPendingFiles = []
            nameOfPendingFiles = []
            # Show on the screen a label "SUCCESSFULL"
            needToShowSuccessMessage = True
          if iPressedMyDecryptButton:
            idVector.decryptFiles(listOfPendingFiles, userPassword)
            # Reset pending files
            listOfPendingFiles = []
            nameOfPendingFiles = []
            # Show on the screen a label "SUCCESSFULL"
            needToShowSuccessMessage = True
        # ---------------------------------------------------------------

        # Display the success label with a delay called "timeDelay"
        if needToShowSuccessMessage:
          xSuccessLabel = xEncryptButton + 140
          ySuccessLabel = yEncrypButton + 10

          if timeDelay > 100:
            needToShowSuccessMessage = False
            timeDelay = 0

          timeDelay += 1
          style.showSuccessfullLabel(xSuccessLabel, ySuccessLabel)

        # -----------LIST OF PATH--------------
        # 6 is equal of the number of file simultaneously
        if len(listOfPath) >= 6: 
          screen.blit(errorPathList, (xElement, yPathList + lengthListPath + 10))

        for u in range(0, len(listOfPath)):
          yElement = u * 12 + yPathList + 20
          u = littleFont.render(listOfPath[u], True, white)
          screen.blit(u, (xElement, yElement))
        # -------------------------------------

        # -------------- SETTINGS MENU --------------
        if iPressedMyLogOutButton:
          if showSettingsMenu:
            showSettingsMenu = False
          else:
            showSettingsMenu = True
        # -------------------------------------------
  # ---------------------------------------------------------------

  # -------------------------WINDOW LOGIN--------------------------
  if not(showSettingsMenu):
    if not(loginIsOk):
      
      # DRAW MAIN TITLE
      xMainTitle = style.drawMainTitle(xScreen, loginIsOk, xMainTitle, yLoginWindow - 58)

      yUsernameBar = yLoginWindow + 70
      yPasswordBar = yLoginWindow + 140

      yButtonLogin = (yLoginWindow + lengthLoginWindow) - 50
      xButtonLogin = xLoginWindow + (widthLoginWindow / 2) - 35

      # Background Of Window Login
      xLoginWindow = (xScreen / 2) - (widthLoginWindow / 2)
      yLoginWindow = (yScreen / 2) - (lengthLoginWindow / 2) - 30
      iPressedMyLoginButton, focusOnUsernameBar, focusOnPasswordBar, tempIClicked = style.loginWindow(xMouse, yMouse, tempIClicked, xLoginWindow, yLoginWindow)

      for event in events:
        if event.type == pygame.KEYDOWN:
          if pygame.key.name(event.key) == "enter":
            iPressedMyLoginButton = True
          if event.key == pygame.K_RETURN:
            iPressedMyLoginButton = True

      # Check If Login is OK
      try:
        loginIsOk, wrongPass = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)
      except TypeError:
        loginIsOk = idVector.confirmationLogin(userPassword, iPressedMyLoginButton, userUsername)

      if loginIsOk:
        makingAnimation = True

      # Show An Error If the password is not correct
      if wrongPass:
        style.showErrorMessage("Invalid credentials...", xScreen / 2 - 55, yLoginWindow + 10)

      # TEXT INPUT USERNAME
      if timeVar.focusOnUsernameBar:
        for event in events:
          userUsername = backModule.textInput(event, userUsername, 100)
      # Blit the text on the screen
      textinputUsername = font.render(userUsername, True, white)
      screen.blit(textinputUsername, (xLoginWindow + 25, yUsernameBar + 3))

      # TEXT INPUT PASSWORD
      if timeVar.focusOnPasswordBar:
        for event in events:
          userPassword, hideUserPassword = backModule.secretTextInput(event, userPassword, hideUserPassword)
      # Blit the text on the screen
      textinputPassword = font.render(hideUserPassword, True, white)
      screen.blit(textinputPassword, (xLoginWindow + 25, yPasswordBar + 3))
  # ---------------------------------------------------------------

  # ------------------------MENU SETTINGS--------------------------
  if showSettingsMenu:


    xField = style.showSettingsMenu(xScreen, userUsername)
    # ARROW BUTTON (to close settings menu)
    iPressedMyLogOutButton, tempLogOutButton = mouseChanger.clickButtonDetect(xMouse, yMouse, 20, 50, 20, 50, tempLogOutButton)
    # MENU OPTION 1
    iPressedMenuOption1, tempMenuOption1 = mouseChanger.clickButtonDetect(xMouse, yMouse, xField, xField + 300, 250, 275, tempMenuOption1)
    # MENU OPTION 2
    iPressedMenuOption2, tempMenuOption2 = mouseChanger.clickButtonDetect(xMouse, yMouse, xField, xField + 300, 300, 325, tempMenuOption2)
    # MENU OPTION 3
    iPressedMenuOption3, tempMenuOption3 = mouseChanger.clickButtonDetect(xMouse, yMouse, xField, xField + 300, 350, 375, tempMenuOption3)

    if iPressedMyLogOutButton:
      showSettingsMenu = False
    if iPressedMenuOption1:
      print("Change Password click")
    if iPressedMenuOption2:
      print("See folder")
    if iPressedMenuOption3:
      loginIsOk = False
      showSettingsMenu = False
      userUsername = ""
      userPassword = ""
      hideUserPassword = ""
  # ---------------------------------------------------------------

  if makingAnimation:
    if loginIsOk:
      xCycleAdding = xLoginWindow + widthLoginWindow / 2
      xCycleRemoval = xLoginWindow + widthLoginWindow / 2
    loginIsOk = False

    makingAnimation, xCycleAdding, xCycleRemoval, xLoginWindow, alpha = style.loginLoading(xCycleAdding, xCycleRemoval, xLoginWindow, alpha, xScreen, yScreen, yLoginWindow)
    if not(makingAnimation):
      loginIsOk = True

  #screen.blit(update_fps(), (10,0))
  pygame.display.update()