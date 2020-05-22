import mouseChanger, os, json
oldTime = 0
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
tempFileButton11 = False
tempFileButton12 = False
tempFileButton13 = False
tempFileButton14 = False
tempFileButton15 = False
tempFileButton16 = False
tempFileButton17 = False
tempFileButton18 = False
tempFileButton19 = False
tempFileButton20 = False
tempFileButton21 = False
tempFileButton22 = False

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
		tempFileButton3 = data['tempFileButton3']
		tempFileButton4 = data['tempFileButton4']
		tempFileButton5 = data['tempFileButton5']
		tempFileButton6 = data['tempFileButton6']
		tempFileButton7 = data['tempFileButton7']
		tempFileButton8 = data['tempFileButton8']
		tempFileButton9 = data['tempFileButton9']
		tempFileButton10 = data['tempFileButton10']
		tempFileButton11 = data['tempFileButton11']
		tempFileButton12 = data['tempFileButton12']
		tempFileButton13 = data['tempFileButton13']
		tempFileButton14 = data['tempFileButton14']
		tempFileButton15 = data['tempFileButton15']
		tempFileButton16 = data['tempFileButton16']
		tempFileButton17 = data['tempFileButton17']
		tempFileButton18 = data['tempFileButton18']
		tempFileButton19 = data['tempFileButton19']
		tempFileButton20 = data['tempFileButton20']
		tempFileButton21 = data['tempFileButton21']
		tempFileButton22 = data['tempFileButton22']
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
		tempFileButton11 = False
		tempFileButton12 = False
		tempFileButton13 = False
		tempFileButton14 = False
		tempFileButton15 = False
		tempFileButton16 = False
		tempFileButton17 = False
		tempFileButton18 = False
		tempFileButton19 = False
		tempFileButton20 = False
		tempFileButton21 = False
		tempFileButton22 = False
	iPressedMyFile0, tempFileButton0 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[0], yCellList[0] + 25, tempFileButton0, time)
	iPressedMyFile1, tempFileButton1 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[1], yCellList[1] + 25, tempFileButton1, time)
	iPressedMyFile2, tempFileButton2 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[2], yCellList[2] + 25, tempFileButton2, time)
	iPressedMyFile3, tempFileButton3 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[3], yCellList[3] + 25, tempFileButton3, time)
	iPressedMyFile4, tempFileButton4 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[4], yCellList[4] + 25, tempFileButton4, time)
	iPressedMyFile5, tempFileButton5 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[5], yCellList[5] + 25, tempFileButton5, time)
	iPressedMyFile6, tempFileButton6 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[6], yCellList[6] + 25, tempFileButton6, time)
	iPressedMyFile7, tempFileButton7 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[7], yCellList[7] + 25, tempFileButton7, time)
	iPressedMyFile8, tempFileButton8 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[8], yCellList[8] + 25, tempFileButton8, time)
	iPressedMyFile9, tempFileButton9 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[9], yCellList[9] + 25, tempFileButton9, time)
	iPressedMyFile10, tempFileButton10 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[10], yCellList[10] + 25, tempFileButton10, time)
	iPressedMyFile11, tempFileButton11 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[11], yCellList[11] + 25, tempFileButton11, time)
	iPressedMyFile12, tempFileButton12 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[12], yCellList[12] + 25, tempFileButton12, time)
	iPressedMyFile13, tempFileButton13 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[13], yCellList[13] + 25, tempFileButton13, time)
	iPressedMyFile14, tempFileButton14 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[14], yCellList[14] + 25, tempFileButton14, time)
	iPressedMyFile15, tempFileButton15 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[15], yCellList[15] + 25, tempFileButton15, time)
	iPressedMyFile16, tempFileButton16 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[16], yCellList[16] + 25, tempFileButton16, time)
	iPressedMyFile17, tempFileButton17 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[17], yCellList[17] + 25, tempFileButton17, time)
	iPressedMyFile18, tempFileButton18 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[18], yCellList[18] + 25, tempFileButton18, time)
	iPressedMyFile19, tempFileButton19 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[19], yCellList[19] + 25, tempFileButton19, time)
	iPressedMyFile20, tempFileButton20 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[20], yCellList[20] + 25, tempFileButton20, time)
	iPressedMyFile21, tempFileButton21 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[21], yCellList[21] + 25, tempFileButton21, time)
	iPressedMyFile22, tempFileButton22 = mouseChanger.clickFileDetect(xMouse, yMouse, xCell - 40, xCell + lenOfBoxesOfFiles, yCellList[22], yCellList[22] + 25, tempFileButton22, time)

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
		'tempFileButton10': str(tempFileButton10),
		'tempFileButton11': str(tempFileButton11),
		'tempFileButton12': str(tempFileButton12),
		'tempFileButton13': str(tempFileButton13),
		'tempFileButton14': str(tempFileButton14),
		'tempFileButton15': str(tempFileButton15),
		'tempFileButton16': str(tempFileButton16),
		'tempFileButton17': str(tempFileButton17),
		'tempFileButton18': str(tempFileButton18),
		'tempFileButton19': str(tempFileButton19),
		'tempFileButton20': str(tempFileButton20),
		'tempFileButton21': str(tempFileButton21),
		'tempFileButton22': str(tempFileButton22)
	}

	f.write(json.dumps(x))
	f.close()
