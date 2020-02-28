import mouseChanger, os, json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
buttonStatePath = os.path.join(THIS_FOLDER, 'buttonState.json')

xCell = 550

tempFileButton0 = False
tempFileButton1 = False
tempFileButton2 = False
tempFileButton3 = False
tempFileButton4 = False
tempFileButton5 = False
tempFileButton6 = False
tempFileButton7 = False
tempFileButton8 = False
tempFileButton9 = False
tempFileButton10 = False

def filesClickDetector(xCell, yCellList, xMouse, yMouse, lenOfBoxesOfFiles):
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
		tempFileButton3 = data['tempFileButton3']
		tempFileButton4 = data['tempFileButton4']
		tempFileButton5 = data['tempFileButton5']
		tempFileButton6 = data['tempFileButton6']
		tempFileButton7 = data['tempFileButton7']
		tempFileButton8 = data['tempFileButton8']
		tempFileButton9 = data['tempFileButton9']
		tempFileButton10 = data['tempFileButton10']
	else:
		tempFileButton0 = False
		tempFileButton1 = False
		tempFileButton2 = False
		tempFileButton3 = False
		tempFileButton4 = False
		tempFileButton5 = False
		tempFileButton6 = False
		tempFileButton7 = False
		tempFileButton8 = False
		tempFileButton9 = False
		tempFileButton10 = False
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[0], yCellList[0] + 25, tempFileButton0)
	iPressedMyFile1, tempFileButton1 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[1], yCellList[1] + 25, tempFileButton1)
	iPressedMyFile2, tempFileButton2 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[2], yCellList[2] + 25, tempFileButton2)
	iPressedMyFile3, tempFileButton3 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[3], yCellList[3] + 25, tempFileButton3)
	iPressedMyFile4, tempFileButton4 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[4], yCellList[4] + 25, tempFileButton4)
	iPressedMyFile5, tempFileButton5 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[5], yCellList[5] + 25, tempFileButton5)
	iPressedMyFile6, tempFileButton6 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[6], yCellList[6] + 25, tempFileButton6)
	iPressedMyFile7, tempFileButton7 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[7], yCellList[7] + 25, tempFileButton7)
	iPressedMyFile8, tempFileButton8 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[8], yCellList[8] + 25, tempFileButton8)
	iPressedMyFile9, tempFileButton9 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[9], yCellList[9] + 25, tempFileButton9)
	iPressedMyFile10, tempFileButton10 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell, xCell + lenOfBoxesOfFiles, yCellList[10], yCellList[10] + 25, tempFileButton10)
	if tempFileButton0:
		print(tempFileButton0, '10')

	f = open(buttonStatePath, 'w')

	x = { 
		'tempFileButton0': str(tempFileButton0),
		'tempFileButton1': str(tempFileButton1),
		'tempFileButton2': str(tempFileButton2),
		'tempFileButton3': str(tempFileButton3),
		'tempFileButton4': str(tempFileButton4),
		'tempFileButton5': str(tempFileButton5),
		'tempFileButton6': str(tempFileButton6),
		'tempFileButton7': str(tempFileButton7),
		'tempFileButton8': str(tempFileButton8),
		'tempFileButton9': str(tempFileButton9),
		'tempFileButton10': str(tempFileButton10)
	}

	f.write(json.dumps(x))
	f.close()
