import cv2
import os
from playsound import playsound

im = cv2.imread("./dataset/tavusKusu.jpg")   # Resim dosyasını açın
color_matrix = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)   # Resmi renkleri matrise atın
notes = {}
height, width,_ = color_matrix.shape

for i in range(width):
    for j in range(height):
        if (160<=color_matrix[j][i][0]<=179 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(255,0,0)]="Do/Kırmızı"
        elif (0<=color_matrix[j][i][0]<=22 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(10,180,180)]="Re/Turuncu"
        elif (22<color_matrix[j][i][0]<=38 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(30,180,180)]="Mi/Sarı"
        elif (38<color_matrix[j][i][0]<=75 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(56,180,180)]="Fa/Yeşil"
        elif (75<color_matrix[j][i][0]<=130 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(100,180,180)]="Sol/Mavi"
        elif (0<=color_matrix[j][i][0]<=30 and 0<=color_matrix[j][i][1]<=10 and 80<=color_matrix[j][i][2]<=130):
            notes[(15,5,105)]="La/Lacivert"
        elif (130<color_matrix[j][i][0]<=160 and 100<=color_matrix[j][i][1]<=255 and 100<=color_matrix[j][i][2]<=255):
            notes[(145,180,180)]="Si/Mor"
        elif (0<=color_matrix[j][i][0]<=30 and 0<=color_matrix[j][i][1]<=30 and 0<=color_matrix[j][i][2]<=30):
            notes[(0,0,0)]="İnce Do/Siyah"
print(notes)

mp3_files = []
for note in notes:                      # Her nota için ses dosyası oluşturulur
    print(notes[note])
    if notes[note] == "Do/Kırmızı":
        dosya = "./dataset/kalin_do.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "Re/Turuncu":
        dosya = "./dataset/re.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "Mi/Sarı":
        dosya = "./dataset/mi.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "Fa/Yeşil":
        dosya = "./dataset/fa.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "Sol/Mavi":
        dosya = "./dataset/sol.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "La/Lacivert":
        dosya = "./dataset/la.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "Si/Mor":
        dosya = "./dataset/si.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
    elif notes[note] == "İnce Do/Siyah":
        dosya = "./dataset/ince_do.mp3"
        dosya_yolu = os.path.join(dosya)
        mp3_files.append(dosya_yolu)
print(mp3_files)

for file in mp3_files:
    playsound(file)

