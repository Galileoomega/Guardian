import pygame, json, os
pygame.init()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

lavandaa = (0, 115, 210)
xStart = 10
yStart = 10

xEnd = 100
yEnd = 100

# Line Simulation (Background)
def renderLineSimulation(screen):
  path = os.path.join(THIS_FOLDER, 'Bin\\Engine\\data.json')

  # -------Retrieve Data-------
  with open(path) as f:
    data = json.load(f)
  xEnd = int(data["xEnd"])
  yEnd = int(data["yEnd"])
  xStart = int(data["xStart"])
  yStart = int(data["yStart"])

  f.close()
  # ---------------------------

  
  if xEnd < 500:
    xStart += 1
    yStart += 1
    xEnd += 2
    yEnd += 2
  else:
    xStart += 2
    yStart += 2
    xEnd += 1
    yEnd += 1

  if xEnd > 700:
    xEnd = 2
    yEnd = 2
    xStart = 1
    yStart = 1

  # -------Update Data-------
  toDump = {
    "xStart": str(xStart),
    "yStart": str(yStart),
    "xEnd": str(xEnd),
    "yEnd": str(yEnd)
  }
  with open(path, "w+") as f:
    json.dump(toDump, f)

  # -------------------------

  pygame.draw.line(screen, lavandaa, (xStart, yStart), (xEnd, yEnd), 4)