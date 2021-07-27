import imagehash
from first import Ui_MainWindow
from PIL import Image
import difflib
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import sys
from tempfile import mktemp
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout,QTableWidgetItem
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui
import logging
import numpy as np
from numpy import genfromtxt
import pandas as pd
import librosa
import librosa.display
from classes import *
from imagededup.methods import PHash
phasher = PHash()
import os
from math import floor
from pydub import AudioSegment
import xlrd
class ApplicationWindow(QtWidgets.QMainWindow):
    w=0
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionsong1.triggered.connect(lambda : self.loadsong(1))
        self.ui.actionsong2.triggered.connect(lambda : self.loadsong(2))
        self.ui.pushButton.clicked.connect(lambda: self.hashes())
        self.audFiles = [None, None]
        self.audMix = None
        self.names = []
        self.score = []
        self.TopTen1 = []
        self.similarity1 = []
        self.similarity2 = []
        self.TopTen1 = []
    def loadsong(self, songNumber ):
        fname = QFileDialog.getOpenFileName(self, 'choose the signal',os.getenv('HOME'), "mp3(*.mp3)")
        self.path = fname[0]
        wname=convert_to_wav(self.path)
        if 1 == songNumber:
            self.wavsong1, self.samplingFrequency1 = librosa.load(wname)
            self.audFiles[0] = self.wavsong1
        elif 2 == songNumber:
            self.ui.horizontalSlider.setDisabled(False)
            self.wavsong2,self.samplingFrequency2 = librosa.load(wname)
            self.audFiles[1] = self.wavsong2
    def hashes(self):
        if(self.audFiles[0] is not None) and (self.audFiles[1] is not None):
            self.sliderRatio = self.ui.horizontalSlider.value() / 100
            self.audMix = slider(self.audFiles[0], self.audFiles[1], self.sliderRatio)
        else:
            if self.audFiles[0] is not None : self.audMix = self.audFiles[0]
            if self.audFiles[1] is not None: self.audMix = self.audFiles[1]
        self.hash_mfcc = ...
        self.hash_chroma_stft = ...
        self.hash_mfcc,self.hash_chroma_stft=hashess(self.audMix,self.samplingFrequency1)
        self.compare()
        print(self.hash_mfcc ,self.hash_chroma_stft )
    def compare(self):
        self.score,self.names = comparee(self.hash_mfcc, self.hash_chroma_stft)
        for l in range((int((len(self.score)/ 2)))):
            self.similarity1.append(self.score[l])
            self.similarity2.append(self.score[int((len(self.score)/ 2))+ l])
        self.result()
    def result(self):
        self.weighted = []
        for l in range(10):
            self.weighted.append((1 / 3) * self.similarity1[l] + (2 / 3) * self.similarity2[l])
        for row in range(10) :
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem((self.names[row])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(self.weighted[row])))
        self.similarity1.clear()
        self.similarity2.clear()
        self.names.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
if __name__ == "__main__":
	main()

































# def clear(self):
#     self.ui.tableWidget.clear()
#     self.wavsong1.clear()
#     self.wavsong2.clear()
#     self.similarity1.clear()
#     self.similarity2.clear()
#     self.similarity2.clear()