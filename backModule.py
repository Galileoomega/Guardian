import pygame
pygame.init()
pygame.scrap.init()

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