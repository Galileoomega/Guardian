# Listing and Place All files
import os, pygame, style, re, mouseChanger, json
from multiprocessing import Process
pygame.init()

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# FILE BROWSER: When Left Arrow Is Pressed, change to under directory (EXCEPTIONNAL CALLED HERE)
def popPathElement(myPath):
  word = ''

  for u in myPath[::-1]:
    word += u
    if u == "\\":
      word = word[::-1]
      myPath = myPath.replace(word, "")
      word = ''
      break

  return myPath

THIS_FOLDER = popPathElement(THIS_FOLDER)

# -------------------VARIABLE-------------------
# Position And Size
xScreen = 500
yScreen = 550
screen = pygame.display.set_mode((xScreen, yScreen))

xCell = 550
yCell = 100
yCellList = []

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
white = (255,255,255)
halfWhite = (200,200,200)
grey = (67, 67, 70)
whiteGrey = (47, 47, 50)
red = (189, 11, 11)
lavanda = (0, 115, 210)
listOfColor = [grey, grey, whiteGrey, grey, grey, darkBlack, grey, grey, grey, black, black]

# ---------PATH---------
robotoLightTTF = os.path.join(THIS_FOLDER, 'Resources\\Roboto\\Roboto-Light.ttf')
imageFolderPath = os.path.join(THIS_FOLDER, 'Resources\\folder.png')
imageFilePath = os.path.join(THIS_FOLDER, 'Resources\\file-image.png')
controllerPath = os.path.join(THIS_FOLDER, 'module\\controller.py')
# ----------------------

fontText = pygame.font.Font(robotoLightTTF, 13)

# ---------IMAGE---------
imageFolder = pygame.image.load(imageFolderPath)
imageFile = pygame.image.load(imageFilePath)
# -----------------------

iPressedMyFiles = False
tempFileButtons = False

# ----------------------------------------------

def buildController(yCellList):

  # ----------------- CONTROLLER BUILD -----------------
  f = open(controllerPath, "w")
  
  f.write(
    "import mouseChanger, os, json" + "\n" + 
    "THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))\n" + 
    "buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')\n\n" + 
    "xCell = 550" + "\n\n"
  )

  for u in range(0, len(yCellList)):
    f.write("tempFileButton" + str(u) + " = False\n")

  f.write(
    "\ndef filesClickDetector(xCell, yCellList, xMouse, yMouse, lenOfBoxesOfFiles):\n" + 
    "\ttry:"
    "\n\t\twith open(buttonStatePath) as f:\n" + 
    "\t\t\tdata = json.load(f)\n" + 
    "\t\t\tif len(data) == len(yCellList):\n" + 
    "\t\t\t\tiHaveMyData = True\n" + 
    "\t\t\telse:\n"
    "\t\t\t\tiHaveMyData = False\n" + 
    "\texcept json.decoder.JSONDecodeError:\n" + 
    "\t\tiHaveMyData = False\n\n"
    "\tif iHaveMyData:\n"
  )

  for u in range(0, len(yCellList)):
    f.write("\t\ttempFileButton" + str(u) + " = data['tempFileButton" + str(u) + "']\n")
  
  f.write("\telse:\n")

  for u in range(0, len(yCellList)):
    f.write("\t\ttempFileButton" + str(u) + " = False\n")

  for u in range(0, len(yCellList)):
    f.write("\tiPressedMyFile" + str(u) + ", tempFileButton" + str(u) + " = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList["+ str(u) +"], yCellList["+ str(u) +"] + 25, tempFileButton" + str(u) + ")" + "\n")
  
  # ------DEBUG------
  #for u in range(0, len(yCellList)):
  #f.write(
  #  "\tif tempFileButton" + str(0) + ":\n"
  #  "\t\tprint(tempFileButton"+ str(0) +", '" + str(u) + "')" + "\n"
  #)
  #for u in range(0, len(yCellList)):
  #  f.write(
  #    "\tif iPressedMyFile" + str(u) + ":\n" + 
  #    "\t\tprint('OverFly " + str(u) + "')\n" 
  #  )
  # -----------------

  f.write(
    "\n\tf = open(buttonStatePath, 'w')\n\n" + 
    "\tx = { \n"
  )

  for u in range(0, len(yCellList)):
    if not(u == len(yCellList) - 1):
      f.write("\t\t'tempFileButton" + str(u) + "': str(tempFileButton" + str(u) + "),\n")
    else:
      f.write("\t\t'tempFileButton" + str(u) + "': str(tempFileButton" + str(u) + ")\n")

  f.write(
    "\t}\n\n" + 
    "\tf.write(json.dumps(x))\n" + 
    "\tf.close()\n"
  )
  
  f.close()
  # ----------------------------------------------------

# Get all the files in the directory (myPath) similar to a ls 
def listingFiles(myPath, xCell, yCell, xScreen, scrollMarker, xMouse, yMouse, yCellList):
  listDir = os.listdir(myPath)
  listDir.sort()

  for element in listDir:

    # Delete useless file to show
    if re.search('NTUSER.DAT.*', element):
      break

    # Change the coordinates (Y)
    yCell = listDir.index(element) * 40 + 100 - scrollMarker

    # ------- Add Each coordinates into a list -------
    if len(yCellList) < len(listDir):
      if not(len(yCellList) > len(listDir)):
        yCellList.append(yCell)
    # ------------------------------------------------

    # Call the function which will draw the UI element for this file
    xCell, yCell, lenOfBoxesOfFiles = renderFile(element, xCell, yCell, xScreen, xMouse, yMouse)

  return listDir, xCell, yCell, yCellList, lenOfBoxesOfFiles

# FOR....
def renderFile(nameOfFile, xCell, yCell, xScreen, xMouse, yMouse):

  # Size of boxes management
  lenOfBoxesOfFiles = int(xScreen - xCell - 10)
  if lenOfBoxesOfFiles < 30:
    lenOfBoxesOfFiles = 30
  if lenOfBoxesOfFiles > 200:
    lenOfBoxesOfFiles = 200

  # ---SEE If Its A Folder Or File---
  x = re.search("\.", nameOfFile)
  if not(x):
    screen.blit(imageFolder, ((xCell - 32), (yCell - 2)))
  else:
    screen.blit(imageFile, ((xCell - 30), (yCell)))
  #---------------------------  

  # Separator beetween files ( BACKGROUND )
  buttonStatePath = os.path.join(THIS_FOLDER, 'module\\buttonState.json')

  with open(buttonStatePath) as f:
    data = json.load(f)

  ########################################################################### NEED TO CHANGE THE COMPARAISON (NameOfFile) #########################
  if data[str(nameOfFile)] == True:
    style.AAfilledRoundedRect(screen, (xCell - 4, yCell - 5, lenOfBoxesOfFiles, 30), lavanda, 0.4)
  else:
    style.AAfilledRoundedRect(screen, (xCell - 4, yCell - 5, lenOfBoxesOfFiles, 30), grey, 0.4)

  # BLIT Files Names
  lblNameOfFile = fontText.render(str(nameOfFile), True, halfWhite)
  screen.blit(lblNameOfFile, (xCell, yCell))

  return xCell, yCell, lenOfBoxesOfFiles

# Remove one element from the path 
def popPathElement(myPath):
  word = ''

  myPath = myPath.capitalize()

  for u in myPath[::-1]:
    word += u
    if u == "\\":
      word = word[::-1]
      for u in range(0, len(word)):
        myPath = myPath[:-1]
      word = ''
      break
    if myPath == "C:":
      myPath = "C:/"

  return myPath
