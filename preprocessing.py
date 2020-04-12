import cv2
import numpy as np
from scipy import signal
from sklearn import preprocessing
import AutoCorr as autoCorr
import DCT as dct

def NonZero(L):
	X = []
	for i in range(len(L)):
		if L[i] == 0:
			continue
		else:
			X.append(L[i])
	return X

def preprocessingFun(pathSignal, lableValue):
	file = open(pathSignal, 'r')
	signalData = file.read()
	signalData = signalData.split()
	label = []
	segData = []
	nyq = 0.5 * 360
	low = 0.5 / nyq
	high = 40 / nyq
	y, x = signal.butter(1, [low, high], 'band')

	meanRemoval = 0
	for i in range(len(signalData)):
		meanRemoval = meanRemoval + float(signalData[i])
	meanRemoval = meanRemoval / len(signalData)
	for i in range(len(signalData)):
		signalData[i] = float(signalData[i]) - meanRemoval
	outfilter = signal.lfilter(x, y, signalData)
	outfilter = np.array(outfilter)
	outnormalize = cv2.normalize(outfilter, cv2.NORM_MINMAX)
	
	heartbet = 205
	count = 0
	for i in range(0, len(outfilter) - heartbet * 4, 820):
		if (i == 0):
			Data = outnormalize[i:i + (heartbet * 4)]
			Data = Data.reshape((Data.shape[0]))
			x = np.correlate(Data, Data, mode='full')
			segData.append(NonZero(dct.DCT(x)))
			label.append(lableValue)

		else:
			label.append(lableValue)

			if (i + heartbet * 4 > len(outfilter)):
				Data = outnormalize[i:]
				Data = Data.reshape((Data.shape[0]))
				x = np.correlate(Data, Data, mode='full')
				segData.append(NonZero(dct.DCT(x)))
				break
			else :
				Data = outnormalize[i:i + (heartbet * 4)]
				Data = Data.reshape((Data.shape[0]))
				x = np.correlate(Data, Data, mode='full')
				segData.append(NonZero(dct.DCT(x)))
	return segData , label
