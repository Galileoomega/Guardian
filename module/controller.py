import mouseChanger, os, json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')

xCell = 550

tempFileButton0 = False

def filesClickDetector(xCell, yCellList, xMouse, yMouse):
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
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[0], yCellList[0] + 50, tempFileButton0)
	if tempFileButton0:
		print(tempFileButton0, '0')

	f = open(buttonStatePath, 'w')

	x = { 
		'tempFileButton0': str(tempFileButton0)
	}

	f.write(json.dumps(x))
	f.close()
