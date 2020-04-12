from tkinter import *
from tkinter import filedialog
import SVM as svmfun
import KNN as knnfun
import preprocessing as preproc
import Train as train
import os
import numpy as np
top = Tk()
top.geometry("200x170" )
top.title("WELCOM"  )
top.configure(bg ='darkblue')
#///////////////////////////////////////////
fileName =0
def readfile():
    top.filename = filedialog.askopenfilename(initialdir="G:/DSP PROJECT/Lab 9 [20-4-2019]/Data/biometrics/test",title="Select folder",
                                              filetypes=(("all folder", "*.*"), ("avi folder", "*.avi")))
    global filePath
    global lable
    filePath = top.filename
    fileName = filePath.split('/')[-1]
    fileName =fileName.split('.')[-2]
    if fileName =='s1':
        lable =0
    elif fileName=='s2':
        lable=1
    elif fileName=='s3':
        lable=2
    else:
        print("Bad Input file")
def svm():
    global selectClassifier
    selectClassifier =2
    main()
def knn():
    global selectClassifier
    selectClassifier=1
    main()
def main():
    if (os.path.exists('train_data.npy')):
        trainData = np.load('train_data.npy')
        trainLable = np.load('train_lable.npy')

    else:
        trainData, trainLable = train.train()
    if (os.path.exists('test_data.npy')):
        testData = np.load('test_data.npy')
        testLable = np.load('test_lable.npy')

    else:
        testData, testLable = preproc.preprocessingFun(filePath, lable)
        testData = np.array(np.float32(testData))
        testLable = np.array(testLable)
        np.save('test_data.npy', testData)
        np.save('test_lable.npy', testLable)
    #trainLable =np.reshape(trainLable ,(-1,1))
    if selectClassifier == 1:
        knnfun.knn(trainData, trainLable, testData, testLable, lable)
    else:
        svmfun.svm(trainData, trainLable, testData, testLable, lable)

B= Button(top, text="Select Test File" ,command =readfile,font=('helvetica', 12 , 'bold'))
B.place(x=40,y=40)

B= Button(top, text="SVM" ,command =svm,font=('helvetica', 12 , 'bold'))
B.place(x=50,y=100)

B= Button(top, text="KNN" ,command =knn,font=('helvetica', 12 , 'bold'))
B.place(x=110,y=100)

top.mainloop()
