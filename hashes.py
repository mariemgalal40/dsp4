from pydub import AudioSegment
from tempfile import mktemp
import matplotlib.pyplot as plot
import librosa.display
import os
from PIL import Image
import imagehash
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("hases")
n=0
m=0
l=1
v=0
paths=[]
songs_name=[]
feature=['Mel-Frequency Cepstral','Chroma']
directory='D:/desk/dsp4/Group22'
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
         paths.append(filename)
         songs_name.append(os.path.splitext(filename)[0])
for t in feature:
    m+=1
    sheet.write(0,m,t)
for o in songs_name:
       v+=1
       sheet.write(v,0,o)
for i in paths:
    plot.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
    fn_mp3 = os.path.join(directory +"/", i)
    mp3_audio = AudioSegment.from_file(fn_mp3, format="mp3")[:60000]
    sound = AudioSegment.from_mp3(f"{fn_mp3}")
    wname = mktemp('.wav')  # use temporary file
    sound.export(wname, format="wav")  # convert to wav
    wavsong, samplingFrequency = librosa.load(wname, duration=60)
    mfcc = librosa.feature.mfcc(wavsong, samplingFrequency) #Mel-Frequency Cepstral Coefficients(MFCCs)
    hash_mfcc=str((imagehash.phash(Image.fromarray(mfcc),hash_size=16)))
    chroma_stft = librosa.feature.chroma_stft(wavsong, samplingFrequency) #Chroma feature
    hash_chroma_stft=str((imagehash.phash(Image.fromarray(chroma_stft),hash_size=16)))
    hases=[hash_mfcc,hash_chroma_stft]
    print
    for k in hases:
       n+=1
       sheet.write(l,n,k)
    n=0
    l+=1
    hases.clear()
workbook.save("try1.xls")






# rolloff= librosa.feature.spectral_rolloff(wavsong, samplingFrequency) #rolloff
# hash_rolloff=str((imagehash.phash(Image.fromarray(rolloff))))
# spec_bw = librosa.feature.spectral_bandwidth(wavsong, samplingFrequency) #spectral_bandwidth
# hash_spec_bw=str((imagehash.phash(Image.fromarray(spec_bw))))
# spec_cent = librosa.feature.spectral_centroid(wavsong, samplingFrequency)
# hash_centroid= str((imagehash.phash(Image.fromarray(spec_cent))))

# spect = plot.specgram(wavsong, Fs=samplingFrequency)
# plot.savefig('spectro/' + os.path.splitext(i)[0]+'.png', bbox_inches=None, pad_inches=0)
# librosa.display.specshow(featured.T, sr=samplingFrequency)
# plot.savefig('centroid/' + os.path.splitext(i)[0] + '.png', bbox_inches=None, pad_inches=0)
# featured = librosa.feature.spectral_rolloff(y=wavsong, sr=samplingFrequency)
# librosa.display.specshow(featured.T, sr=samplingFrequency)
# plot.savefig('rolloff/' + os.path.splitext(i)[0] + '.png', bbox_inches=None, pad_inches=0)