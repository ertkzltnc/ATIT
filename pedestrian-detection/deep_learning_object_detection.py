
import numpy as np

import cv2
import datetime
def getFileName():
        return datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg")
fn=getFileName()

args={'image': 'images/images.jpg', 'prototxt': 'MobileNetSSD_deploy.prototxt.txt', 'model': 'MobileNetSSD_deploy.caffemodel', 'confidence': 0.2}
print(args)
# sınıf etiketleri listesini başlatmak için MobileNet SSD eğitildi
# algılar, sonra her sınıf için bir dizi sınırlayıcı kutu rengi oluşturur
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# serileştirilmiş modelimizi diskten yükle
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

#giriş görüntüsünü yükleyin ve görüntü için bir giriş bloğu oluşturun 
# Sabit 300x300 piksele yeniden boyutlandırarak ve ardından normalleştirerek
# not: normalleştirme MobileNet SSD'nin yazarları aracılığıyla yapılır.


image = cv2.imread(args["image"])

(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

        # bloğu ağdan geçirin ve tespitleri alın
       
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

        # tespitler üzerinde döngü
for i in np.arange(0, detections.shape[2]):
                 
        confidence = detections[0, 0, 0, 2]

                #'güvenin' sağlayarak zayıf algılamaları filtreleyin
                # minimum güvenden daha büyük
        if confidence > args["confidence"]:
                        #sınıf etiketinin indeksini `detections`dan çıkarmak,
                        # sonra sınırlayıcı kutunun (x, y) koordinatlarını hesaplayın. 
                idx = int(detections[0, 0, i, 1])
                if idx==15:
                
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")

                                        # tahmini göstermek
                        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                        print("[INFO] {}".format(label))
                        cv2.rectangle(image, (startX, startY), (endX, endY),COLORS[idx], 2)
                        y = startY - 15 if startY - 15 > 15 else startY + 15
                        cv2.putText(image, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    
yol="/home/pi/pedestrian-detection/sonuc/"+str(fn)
print(yol)
cv2.imshow("Output", image)
cv2.imwrite(yol,image)
cv2.waitKey(0)    
#Ekranı temizle ve pencereleri kapat

cv2.destroyAllWindows()
