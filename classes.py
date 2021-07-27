import imagehash
# from PyQt5 import QtWidgets
# from first import Ui_MainWindow
# from PIL import Image
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import sys
from tempfile import mktemp
from PIL import Image
import pylab
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout,QTableWidgetItem
from PyQt5 import QtCore, QtWidgets, QtMultimedia
import logging
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import pandas as pd
import librosa
import librosa.display
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image
from imagededup.methods import PHash
phasher = PHash()
import os
import csv
from math import floor
from pydub import AudioSegment
import csv
from math import floor
from pydub import AudioSegment
import pandas as pd
import xlrd
# class modes() :
def convert_to_wav(wave):
    mp3_audio = AudioSegment.from_file(wave, format="mp3")[:60000]  # read mp3
    wname = mktemp('.wav')  # use temporary file
    mp3_audio.export(wname, format="wav")
    return wname
def slider(wavsong1,wavsong2,r):
    wavsongg1 = wavsong1 * r + wavsong2 * (1- r)
    return wavsongg1
def hashess(mixx,samplingFrequency1):
    mfcc = librosa.feature.mfcc(mixx,samplingFrequency1)
    hash1 = str((imagehash.phash(Image.fromarray(mfcc),hash_size=16)))
    chroma_stft = librosa.feature.chroma_stft(mixx,samplingFrequency1)
    hash2 = str((imagehash.phash(Image.fromarray(chroma_stft),hash_size=16)))
    return(hash1,hash2)
def comparee(hash1,hash2):
    d = {}
    data = []
    data1=[]
    name=[]
    namess=[]
    scoree=[]
    df = pd.read_excel("final.xls")
    for i in range(70):
        data.append(df.iloc[i, 2])
        data1.append(df.iloc[i, 1])
        name.append(df.iloc[i, 0])
    features_hash = [hash1,hash2]
    for k in features_hash:
        for i in range(len(data)):
            s2 =data1[i]
            s1 = k
            song_name = name[i]
            s = (1- (imagehash.hex_to_hash(s1) - imagehash.hex_to_hash(s2)) / 256.0)
            d.update({name[i] : s})
            # d.update({name[i] : s})
        sort = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for a_tuple in sort:
            namess.append(a_tuple[0])
        for b_tuple in sort:
            scoree.append(b_tuple[1])
        for m in range(len(data)):
            data1[m] = data[m]
        d.clear()
        sort.clear()
    return(scoree,namess)
  
       

