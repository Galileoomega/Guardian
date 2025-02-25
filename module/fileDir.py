# Listing and Place All files
import os, pygame, style, re, mouseChanger, json, module.timeVar
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

xCell = 0
yCell = 100
yCellList = []

# File Input Bar
lengthBar = 25
widthBar = 270
xFileBar = (xScreen / 2) - (widthBar / 2)
yFileBar = 100

# Color
black = (40, 40, 43)
darkBlack = (20, 20, 23)
newBlack = (45, 45, 48)
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

activeFile = ""

# ----------------------------------------------

# Check if its a folder or a file and return a True/False
def folderType(myPath):
  # If x = True: ITS A FILE
  # If x = False: ITS A FOLDER
  x = os.path.isfile(myPath)

  module.timeVar.fileType = x
  
  return x


def buildController(yCellList):

  # ----------------- CONTROLLER BUILD -----------------
  f = open(controllerPath, "w")
  
  f.write(
    "import mouseChanger, os, json" + "\n" + 
    "oldTime = 0\n" + 
    "THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))\n" + 
    "buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')\n\n" + 
    "xCell = 550" + "\n\n"
  )

  for u in range(0, len(yCellList)):
    f.write("tempFileButton" + str(u) + " = False\n")

  f.write(
    "\ndef filesClickDetector(xCell, yCellList, xMouse, yMouse, lenOfBoxesOfFiles, time):\n" + 
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
    f.write("\tiPressedMyFile" + str(u) + ", tempFileButton" + str(u) + " = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList["+ str(u) +"], yCellList["+ str(u) +"] + 25, tempFileButton" + str(u) + ", time)" + "\n")

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
def listingFiles(myPath, xCell, yCell, xScreen, scrollMarker, xMouse, yMouse, yCellList, oneTap, tempActiveFile):
  try:
    listDir = os.listdir(myPath)
  except PermissionError:
    myPath = popPathElement(myPath)
    listDir = os.listdir(myPath)

  # Sort the list of files alphabetically
  listDir = sorted(sorted(listDir, reverse=True), key=str.lower)
  indexOfElement = 0
  activeFiles = ""
  yCellList = []
  listA = []
  listB = []

  # ----- Wipe the main list of files to make one of folder and files -----
  for element in listDir:
    x = folderType(module.timeVar.myPath + "\\" + element)
    if x:
      listA.append(element)
    else:
      listB.append(element)
  listDir = []
  listDir = listB + listA
  # -----------------------------------------------------------------------

  for element in listDir:

    # Delete useless file to show
    if re.search('NTUSER.DAT.*', element):
      break

    # Change the coordinates (Y)
    yCell = listDir.index(element) * 40 + 100 - scrollMarker

    # ------- Add Each coordinates into a list -------
    yCellList.append(yCell)
    # ------------------------------------------------

    # Get the size of the actual file
    # And convert It to KB
    size = int(os.path.getsize(myPath + "\\" + element) / 1000)

    # Call the function which will draw the UI element for this file
    xCell, yCell, lenOfBoxesOfFiles, activeFile = renderFile(element, size, xCell, yCell, xScreen, xMouse, yMouse, indexOfElement)

    # Get the index of the nameOfFile
    indexOfElement += 1

    if activeFile != "":
      if activeFile != tempActiveFile:
        oneTap = True
        module.timeVar.fileChanged = True
      else:
        module.timeVar.fileChanged = False
      if oneTap:
        tempActiveFile = activeFile
        module.timeVar.fileName = element
        oneTap = False
      takingFileName(element, myPath)
      activeFiles = activeFile

  try:
    return listDir, xCell, yCell, yCellList, lenOfBoxesOfFiles, activeFiles, oneTap, tempActiveFile
  except UnboundLocalError:
    lenOfBoxesOfFiles = 10
    return listDir, xCell, yCell, yCellList, lenOfBoxesOfFiles, activeFiles, oneTap, tempActiveFile

# FOR....
def renderFile(nameOfFile, sizeOfFile, xCell, yCell, xScreen, xMouse, yMouse, indexOfElement):

  # Concatenate the nameOfFile
  myFile = "tempFileButton" + str(indexOfElement)

  # Size of boxes management
  lenOfBoxesOfFiles = int(xScreen - xCell - 10)
  if lenOfBoxesOfFiles < 300:
    lenOfBoxesOfFiles = 300
  if lenOfBoxesOfFiles > 500:
    lenOfBoxesOfFiles = 500

  buttonStatePath = os.path.join(THIS_FOLDER, 'module\\buttonState.json')

  # Open the buttonState.json to see wich button is active
  with open(buttonStatePath) as f:
    data = json.load(f)

    # ------Translate str() to bool()------
    try:
      corelation1 = data[myFile]
    except KeyError:
      corelation1 = data["tempFileButton0"]
    if corelation1 == 'False':
      corelation = False
    else:
      corelation = True
    # -------------------------------------

    # BLIT BACKGROUND OF FILES
    if corelation:
      style.AAfilledRoundedRect(screen, (xCell - 41, yCell - 6, lenOfBoxesOfFiles + 2, 32), lavanda, 0.3)
      colorFiles = white
      activeFile = myFile
    else:
      style.AAfilledRoundedRect(screen, (xCell - 41, yCell - 6, lenOfBoxesOfFiles + 2, 32), grey, 0.3)
      activeFile = ""
      colorFiles = halfWhite
  
  # ----------- Check if the file has been ENCRYPTED -----------
  if nameOfFile[-3:len(nameOfFile)] == "sha":
    thisFileIsEncrypted = True
  else:
    thisFileIsEncrypted = False

  if thisFileIsEncrypted:
    if activeFile == "":
      style.AAfilledRoundedRect(screen, (xCell - 41, yCell - 6, lenOfBoxesOfFiles + 2, 32), lavanda, 0.3)
      style.AAfilledRoundedRect(screen, (xCell - 40, yCell - 5, lenOfBoxesOfFiles, 30), grey, 0.3)
    else:
      style.AAfilledRoundedRect(screen, (xCell - 41, yCell - 6, lenOfBoxesOfFiles + 2, 32), halfWhite, 0.3)
      style.AAfilledRoundedRect(screen, (xCell - 40, yCell - 5, lenOfBoxesOfFiles, 30), lavanda, 0.3)
  # ------------------------------------------------------------

  # Separator beetween files ( BACKGROUND )
  # ---SEE If Its A Folder Or File---
  x = folderType(module.timeVar.myPath + "\\" + nameOfFile)
  
  if not(x):
    screen.blit(imageFolder, ((xCell - 32), (yCell - 2)))
  else:
    screen.blit(imageFile, ((xCell - 31), (yCell - 1)))
  # ---------------------------------
  
  # ------------RESIZE NAME OF FILE IF HE'S TOO BIG------------
  if len(nameOfFile) >= 60:
    nameOfFile = nameOfFile[0:20] + "..." + str(nameOfFile[len(nameOfFile) - 10:len(nameOfFile)])
  # -----------------------------------------------------------


  # BLIT Files Names
  lblNameOfFile = fontText.render(str(nameOfFile), True, colorFiles)
  screen.blit(lblNameOfFile, (xCell, yCell))

  # BLIT Size Of Files
  if x:
    # Check if it need to be converted in Mo
    if sizeOfFile > 1000:
      sizeOfFile = sizeOfFile / 1000
      lblSizeOfFile = fontText.render(str(sizeOfFile) + " MB", True, colorFiles)
    else:
      lblSizeOfFile = fontText.render(str(sizeOfFile) + " KB", True, colorFiles)
    
    # Blit it to the screen
    lenOfFile, width = fontText.size(str(sizeOfFile))
    screen.blit(lblSizeOfFile, (lenOfBoxesOfFiles + 440 - lenOfFile, yCell))

  return xCell, yCell, lenOfBoxesOfFiles, activeFile

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
    myPath = "C:\\"

  module.timeVar.myPath = myPath

  return myPath

# File Path area SHOW (called in the same file in listingFiles())
def takingFileName(element, myPath):

  # ACTUAL FILE PATH for programm only
  module.timeVar.fileOnFocusPath = myPath + "\\" + element
  module.timeVar.activeFile = element

  myNewPath = ""
  count = 0

  for u in myPath:
    if u == '\\':
      count += 1
    if count >= 2:
      break

    myNewPath += u 

  # Will check if the name of the file is too big. (GRAPHIC ONLY)
  if len(element) >= 20:
    element = element[0:20] + "..." + str(element[len(element) - 10:len(element)])
  
  myNewPath += "\\...\\"
  module.timeVar.shortPathWithActiveFile = myNewPath + element

# List all the pending files for being encrypted/decrypted
def listPendingFiles(fileNames):
  yFile = 170
  resizedString = False
  lenOfBoxes = 360
  startPosition = 55
  startPositionCancelButton = 370

  for fileName in fileNames:
    yFile += 40

    # BLIT BACKGROUND OF FILES
    style.AAfilledRoundedRect(screen, (startPosition, yFile - 6, lenOfBoxes, 32), grey, 0.3)
    style.AAfilledRoundedRect(screen, (startPositionCancelButton, yFile - 3, 35, 26), newBlack, 0.3)
    
    # BLIT IMAGES AND CHECK IF ITS A FOLDER OR NOT
    if folderType(module.timeVar.myPath + "\\" + fileName):
      screen.blit(imageFile, (60, yFile - 1))
    else:
      screen.blit(imageFolder, (60, yFile - 1))

    # BLIT Files Names
    while len(fileName) > 35:
      fileName = fileName[:-1]
      resizedString = True
    if resizedString:
      fileName += "..."
      resizedString = False

    lblPendingFile = fontText.render(str(fileName), True, white)
    screen.blit(lblPendingFile, (90, yFile))

