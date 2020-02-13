import pygame, json, os
pygame.init()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

lavandaa = (0, 115, 210)

xEnd = 100
yEnd = 100
finishedToDraw = False

# Line Simulation (Background)
def renderLineSimulation(screen, xStartUser, yStartUser, index):
  if index == 1:
    path = os.path.join(THIS_FOLDER, 'Bin\\Engine\\data.json')
  else:
    path = os.path.join(THIS_FOLDER, 'Bin\\Engine\\data2.json')

  # -------Update Data-------
  with open(path) as f:
    data = json.load(f)
    added = data["added"]
  f.close()

  if added == "False":
    added = False
  if added == "True":
    added = True

  if added:
    print("RESET")

    toDump = {
      "xStart": str(xStartUser),
      "yStart": str(yStartUser),
      "xEnd": str(xStartUser),
      "yEnd": str(yStartUser),
      "added": str(False)
    }
    with open(path, "w+") as f:
      json.dump(toDump, f)

  # -------------------------


  # -------Retrieve Data-------
  if index == 1:
    with open(path) as f:
      data = json.load(f)
    xEnd = int(data["xEnd"])
    yEnd = int(data["yEnd"])
    xStart = int(data["xStart"])
    yStart = int(data["yStart"])

    f.close()
  else:
    with open(path) as f:
      data = json.load(f)
    xEnd = int(data["xEnd"])
    yEnd = int(data["yEnd"])
    xStart = int(data["xStart"])
    yStart = int(data["yStart"])
  # ---------------------------

  if xEnd < 400:
    xStart += 1
    yStart += 1
    xEnd += 2
    yEnd += 2
  else:
    xStart += 3
    yStart += 3
    xEnd += 2
    yEnd += 2
  if index == 1:
    if xEnd > 700:
      xEnd = 2
      yEnd = 2
      xStart = 1
      yStart = 1
      finishedToDraw = True
    else:
      finishedToDraw = False
  else:
    if xEnd > 700:
      xEnd = 2
      yEnd = 80
      xStart = 1
      yStart = 80
      finishedToDraw = True
    else:
      finishedToDraw = False


  # -------Update Data-------
  toDump = {
    "xStart": str(xStart),
    "yStart": str(yStart),
    "xEnd": str(xEnd),
    "yEnd": str(yEnd),
    "added": str(False)
  }
  if finishedToDraw:
    print("AADDED IS NOW TRUE")
    toDump = {
      "xStart": str(xStart),
      "yStart": str(yStart),
      "xEnd": str(xEnd),
      "yEnd": str(yEnd),
      "added": str(True)
    }

  with open(path, "w+") as f:
    json.dump(toDump, f)

  # -------------------------

  pygame.draw.line(screen, lavandaa, (xStart, yStart), (xEnd, yEnd), 3)
  return finishedToDraw