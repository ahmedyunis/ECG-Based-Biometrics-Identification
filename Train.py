import os
import preprocessing as preproc
import os
import numpy as np
def train():
    # traning
    FolderTrain ="G:/DSP PROJECT/Lab 9 [20-4-2019]/Data/biometrics/train"
    labelValue = 0
    trainData = []
    trainLable = []
    finalTrain = []
    finalLabel = []
    for filename in os.listdir(FolderTrain):
        pathSignal = os.path.join(FolderTrain, filename)
        tData, tLabel = preproc.preprocessingFun(pathSignal, labelValue)
        trainData.append(tData)
        trainLable.append(tLabel)
        labelValue += 1
    for i in range(len(trainData)):
        finalTrain+=trainData[i]
        finalLabel+=trainLable[i]
    finalTrain = np.array(finalTrain)
#    finalTrain =np.float32(finalTrain)
    finalLabel = np.array(finalLabel , dtype=np.int)
    np.save('train_data.npy', finalTrain)
    np.save('train_lable.npy', finalLabel)
    return finalTrain , finalLabel
