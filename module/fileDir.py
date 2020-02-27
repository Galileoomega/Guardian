# Listing and Place All files
import os, pygame, style, re
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
# ----------------------

fontText = pygame.font.Font(robotoLightTTF, 13)

# ---------IMAGE---------
imageFolder = pygame.image.load(imageFolderPath)
imageFile = pygame.image.load(imageFilePath)
# -----------------------

# ----------------------------------------------

# Get all the files in the directory (myPath) similar to a ls 
def listingFiles(myPath, xCell, yCell, xScreen):
  listDir = os.listdir(myPath)
  for element in listDir:
    yCell = listDir.index(element) * 40 + 100
    if yCell >= 1000:
      yCell = 300

    xCell, yCell = renderFile(element, xCell, yCell, xScreen)

  return listDir, xCell, yCell

# FOR....
def renderFile(nameOfFile, xCell, yCell, xScreen):

  # Size of boxes management
  lenOfBoxes = int(xScreen - xCell - 10)
  if lenOfBoxes < 30:
    lenOfBoxes = 30
  if lenOfBoxes > 200:
    lenOfBoxes = 200

  # ---SEE If Its A Folder Or File---
  x = re.search("\.", nameOfFile)
  if not(x):
    screen.blit(imageFolder, ((xCell - 32), (yCell - 2)))
  else:
    screen.blit(imageFile, ((xCell - 30), (yCell)))
  #---------------------------  

  # Separator beetween files
  style.AAfilledRoundedRect(screen, (xCell - 4, yCell - 5, lenOfBoxes, 30), whiteGrey, 0.4)

  # Files Names
  lblNameOfFile = fontText.render(str(nameOfFile), True, halfWhite)
  screen.blit(lblNameOfFile, (xCell, yCell))

  return xCell, yCell

# Remove one element from the path 
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