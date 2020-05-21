import mouseChanger, os, json
oldTime = 0
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')

xCell = 550

tempFileButton0 = False

def filesClickDetector(xCell, yCellList, xMouse, yMouse, lenOfBoxesOfFiles, time):
	try:
		with open(buttonStatePath) as f:
			data = json.load(f)
			if len(data) == len(yCellList):
				iHaveMyData = True
			else:
				iHaveMyData = False
	except json.decoder.JSONDecodeError:
		iHaveMyData = False

	if iHaveMyData:
		tempFileButton0 = data['tempFileButton0']
	else:
		tempFileButton0 = False
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[0], yCellList[0] + 25, tempFileButton0, time)

	f = open(buttonStatePath, 'w')

	x = { 
		'tempFileButton0': str(tempFileButton0)
	}

	f.write(json.dumps(x))
	f.close()
