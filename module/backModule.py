import pygame, os, style
pygame.init()
pygame.scrap.init()

user_input_value = ""
iUsedCtrlV = False
font = pygame.font.Font("Resources\\Roboto\\Roboto-Black.ttf", 13)
black = (250, 250, 250)
active = False
listDir = [str]
separator = 10
myPath = ""

# PROGRAM : Will take the text of the clipboard
def getContentOfClipboard():
  try:
    clipboard = pygame.scrap.get(pygame.SCRAP_TEXT)
    try:
      clipboard = clipboard.decode("utf-8")
    except UnicodeDecodeError:
      clipboard = ''
  except AttributeError:
    pass
  try:
    clipboard = clipboard[:-1]
  except TypeError:
    pass
  
  try:
    if len(clipboard) > 400:
      clipboard = ""
      print("Error : Invalid Clipoard")
  except TypeError:
    pass 

  return clipboard

# GRAPHIC : Detect a CTRL + V or C
def keyboardCommandDetection(user_input_value, event):
  clipboard = getContentOfClipboard()
  if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
    user_input_value += str(clipboard)

  return user_input_value

# GRAPHIC : Detect a CTRL + A
def selectAllText(user_input_value):
  if event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
    iUsedCtrlA = True
  else:
    iUsedCtrlA = False
    user_input_value = user_input_value
  return iUsedCtrlA, user_input_value

# Classical text input management
def textInput(event, text, maxLimit):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_BACKSPACE:
      text = text[:-1]
    else:
      if len(text) <= maxLimit:
        # Detect a CTRL + V
        text = keyboardCommandDetection(text, event)

        # Filtering invalid character
        try:
          if ord(event.unicode) > 31:
            text += event.unicode
        except TypeError:
          pass
  else: 
    text = text
  try:
    return text
  except UnboundLocalError:
    text = text
    return text

# Same than textInput() but for password
def secretTextInput(event, text, secretText):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_BACKSPACE:
      text = text[:-1]
      secretText = secretText[:-1]
    else:
      # Filtering invalid character
      try:
        if ord(event.unicode) > 31:
          text += event.unicode
          secretText += "*"
      except TypeError:
        pass
  try:
    return text, secretText
  except UnboundLocalError:
    print("error")
    return text, secretText

# Will read all file in a directory and give them an position
def listDirectory(separator, xDialogBrowser, yDialogBrowser, myPath):
  listDir = os.listdir(myPath)
  
  for u in listDir:
    # GET THE INDEX OF U FOR COUNT
    separator = listDir.index(u) * 20 + 10
    if separator == 100:
      separator = 10
    separator = style.browserDialogContent(u, separator, xDialogBrowser, yDialogBrowser)
  
  return separator

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

