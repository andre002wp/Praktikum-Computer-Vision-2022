#import the pyplot and wavfile modules 

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage,QPixmap
from scipy.io import wavfile
import sys
import os

class Ui(QtWidgets.QMainWindow):
    
    img = []
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Comvis Mod 1.ui', self)

        self.btnOpenFile = self.findChild(QtWidgets.QPushButton, 'OpenFile_btn')
        self.btnOpenFile.clicked.connect(self.loadFile) 
        self.btnOpenFile = self.findChild(QtWidgets.QPushButton, 'OpenFile_btn')
        self.spectogram = self.findChild(QtWidgets.QLabel, 'spectogram_label')
        self.spectogram.setPixmap(self.rezizeandShow(self.getGreyVersion(self.img)))
        self.timefreq = self.findChild(QtWidgets.QLabel, 'timefreq_label')
        self.timefreq.setPixmap(self.rezizeandShow(self.getGreyVersion(self.img)))
        
        self.show()

    def loadFile(self):
        # This is executed when the button is pressed
        print('btn Open File Pressed')
        openFileDialog = QFileDialog.getOpenFileName(self,"select Image File",os.getcwd(),"Image Files (*.wav)")
        fileimg = openFileDialog[0]

        if(len(fileimg)>4):
            #import the pyplot and wavfile modules
            # Read the wav file (mono)
            samplingFrequency, signalData = wavfile.read(fileimg)
            #on this audio file maybe stereo audio(?) so what we should do is plot the spectogram to the left or right channel
            #ceritanya pengen fasih inggris xixixi
            print(f"number of channels = {signalData.shape[1]}")
            length = signalData.shape[0] / samplingFrequency
            print(f"length = {length}s")
            plt.figure(figsize=(15,10))
            plt.title('Spectrogram of a wav file with piano music')

            plt.subplot(211)
            plt.plot(signalData)
            plt.xlabel('Sample')
            plt.ylabel('Amplitude')
            plt.subplot(212)
            plt.specgram(signalData[:,0],Fs=samplingFrequency)
            plt.xlabel('Time')
            plt.ylabel('Frequency')
            plt.show()

    def showSpectogram(self,spectogram):
        pass

    def showTimeFreq(self,timeFreq):
        pass
    


 



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
app.exit(0)
# sys.exit(app.exec_())