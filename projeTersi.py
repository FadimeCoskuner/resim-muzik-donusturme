import wave                     # sesleri ses dosyalarına kaydetmek için.
from PIL import Image           # resim işlemleri için.
import numpy as np              
from math import sqrt           

w = wave.open("./datasetTersi/KuzuKuzu.wav", mode = "rb")   # ses dosyasını açar ve okur.
frames = w.readframes(w.getnframes())    # okuma sırasında frame'leri alır ve frame'leri okur.

pixels = []

for i in range(0,w.getnframes(),3):                      # getnframes() = video da bulunan frame sayısını tutar. Frame sayısına kadar 3'er artacak şekilde döngü oluşturulur.
    pixels.append((frames[i],frames[i+1],frames[i+2]))   # pixels dizisine okuduğu frame'leri 3er 3er olarak atar.

boyut = int(sqrt(w.getnframes()/3))   # kare görüntüye sığdırma.

img = []

for x in range(0,boyut):    # frame'leri satır satır okur. En sonda img listesine her satırı atar.
    satir = []    
    for y in range(0,boyut):
        satir.append(pixels[x*boyut+y])
    img.append(satir)

liste = np.array(img, dtype=np.uint8)  # resime çevirmek için uint8 tipinde numpy dizisi oluşur.
new_image = Image.fromarray(liste)     # array değerlerini alır. Bellek dosyası oluşturur. 
new_image.save('./datasetTersi/resim.png') # oluşturulan resmi .png olarak kaydeder.
