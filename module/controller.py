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

def filesClickDetector(xCell, yCellList, xMouse, yMouse, tempFileButtons):
	try:
		with open(buttonStatePath) as f:
			data = json.load(f)
			iHaveMyData = True
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
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[0], yCellList[0] + 50, tempFileButton0)
	iPressedMyFile1, tempFileButton1 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[1], yCellList[1] + 50, tempFileButton1)
	iPressedMyFile2, tempFileButton2 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[2], yCellList[2] + 50, tempFileButton2)
	iPressedMyFile3, tempFileButton3 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[3], yCellList[3] + 50, tempFileButton3)
	iPressedMyFile4, tempFileButton4 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[4], yCellList[4] + 50, tempFileButton4)
	iPressedMyFile5, tempFileButton5 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[5], yCellList[5] + 50, tempFileButton5)
	iPressedMyFile6, tempFileButton6 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[6], yCellList[6] + 50, tempFileButton6)
	iPressedMyFile7, tempFileButton7 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[7], yCellList[7] + 50, tempFileButton7)
	iPressedMyFile8, tempFileButton8 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[8], yCellList[8] + 50, tempFileButton8)
	iPressedMyFile9, tempFileButton9 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[9], yCellList[9] + 50, tempFileButton9)
	iPressedMyFile10, tempFileButton10 = mouseChanger.clickButtonDetect(xMouse, yMouse, xCell, xCell + 50, yCellList[10], yCellList[10] + 50, tempFileButton10)
	if iPressedMyFile0:
		print(iPressedMyFile0)
	if iPressedMyFile1:
		print(iPressedMyFile1)
	if iPressedMyFile2:
		print(iPressedMyFile2)
	if iPressedMyFile3:
		print(iPressedMyFile3)
	if iPressedMyFile4:
		print(iPressedMyFile4)
	if iPressedMyFile5:
		print(iPressedMyFile5)
	if iPressedMyFile6:
		print(iPressedMyFile6)
	if iPressedMyFile7:
		print(iPressedMyFile7)
	if iPressedMyFile8:
		print(iPressedMyFile8)
	if iPressedMyFile9:
		print(iPressedMyFile9)
	if iPressedMyFile10:
		print(iPressedMyFile10)

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
