#import the pyplot and wavfile modules 

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
from scipy.io import wavfile
import sys
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class Ui(QtWidgets.QMainWindow):
    
    img = []
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Comvis Mod 1.ui', self)

        self.btnOpenFile = self.findChild(QtWidgets.QPushButton, 'OpenFile_btn')
        self.btnOpenFile.clicked.connect(self.loadFile) 
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
            self.showSpectogram(signalData)
            self.showTimeFreq(signalData[:,0],samplingFrequency)

            # plt.figure(figsize=(15,10))
            # plt.title('Spectrogram of a wav file with piano music')
            # plt.subplot(211)
            # plt.plot(signalData)
            # plt.xlabel('Sample')
            # plt.ylabel('Amplitude')
            # plt.subplot(212)
            # plt.specgram(signalData[:,0],Fs=samplingFrequency)
            # plt.xlabel('Time')
            # plt.ylabel('Frequency')
            # plt.show()

    def showSpectogram(self,spectogram):
        self.spectogram_view.canvas.axes.clear()
        self.spectogram_view.canvas.axes.plot(spectogram)
        # self.spectogram_view.canvas.axes.set_ylabel('Y', color='black')
        # self.spectogram_view.canvas.axes.set_xlabel('X', color='black')
        self.spectogram_view.canvas.axes.set_title('Spectogram')
        self.spectogram_view.canvas.axes.grid()
        self.spectogram_view.canvas.draw()

    def showTimeFreq(self,signalData,samplingFrequency):
        self.timefreq_view.canvas.axes.clear()
        self.timefreq_view.canvas.axes.specgram(signalData,Fs=samplingFrequency)
        self.timefreq_view.canvas.axes.set_title('Time Frequency')
        self.timefreq_view.canvas.axes.set_facecolor('green')
        self.timefreq_view.canvas.axes.grid()
        self.timefreq_view.canvas.draw()
    


 



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
app.exit(0)
# sys.exit(app.exec_())