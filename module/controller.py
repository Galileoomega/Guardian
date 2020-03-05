import mouseChanger, os, json
oldTime = 0
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')

xCell = 550

tempFileButton0 = False
tempFileButton1 = False
tempFileButton2 = False

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
		tempFileButton1 = data['tempFileButton1']
		tempFileButton2 = data['tempFileButton2']
	else:
		tempFileButton0 = False
		tempFileButton1 = False
		tempFileButton2 = False
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[0], yCellList[0] + 25, tempFileButton0, time)
	iPressedMyFile1, tempFileButton1 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[1], yCellList[1] + 25, tempFileButton1, time)
	iPressedMyFile2, tempFileButton2 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[2], yCellList[2] + 25, tempFileButton2, time)

	f = open(buttonStatePath, 'w')

	x = { 
		'tempFileButton0': str(tempFileButton0),
		'tempFileButton1': str(tempFileButton1),
		'tempFileButton2': str(tempFileButton2)
	}

	f.write(json.dumps(x))
	f.close()
