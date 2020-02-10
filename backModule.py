import pygame
pygame.init()
pygame.scrap.init()

user_input_value = ""
iUsedCtrlV = False
font = pygame.font.Font("Resources\\Roboto\\Roboto-Black.ttf", 13)
black = (250, 250, 250)
active = False

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
  if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
      user_input_value += str(clipboard)
      iUsedCtrlV = True
  else:
      iUsedCtrlV = False
  return iUsedCtrlV, user_input_value


# Classical text input management
def textInput(event, text):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RETURN:
      print(text)
      text = text
    elif event.key == pygame.K_BACKSPACE:
      text = text[:-1]
    else:
      text += event.unicode
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
    if event.key == pygame.K_RETURN:
      print(text)
      text = text
    elif event.key == pygame.K_BACKSPACE:
      text = text[:-1]
      secretText = secretText[:-1]
    else:
      text += event.unicode
      secretText += "*"
  else: 
    text = text
  try:
    return text, secretText
  except UnboundLocalError:
    text = text
    return text, secretText

