# YOLO_filament : A YOLOv5 based detection of solar chromospheric filaments (Gosain,S. 2023)
Customized YOLOv8 neural network model for detecting filaments, prominences and active regions in fulldisk H-alpha images from GONG network.
YOLO (You Only Look Once) is a convolutional neural network (CNN) designed for object recognition in images and videos. It is very fast and allows real time object detection. 

**Install YOLOv8**
Follow instructions on YOLO website
https://github.com/ultralytics/ultralytics

**Create Labeled Data for Training and Validation**
Used LabelImg to label images. 
```
pip install labelImg
```
**Train Model for Filaments, prominences and Active Regions using Labeled data**
```
yolo task=detect mode=train epochs=400 data=data_custom.yaml model=yolov8m.pt imgsz=640 batch=32 patience=400
```
**Predict using YOLOv8 on images/movies from NSO GONG Halpha network.**
```
yolo task=detect mode=predict model=custom_halpha.pt show=True conf=0.5 source=1.jpeg
```
![alt text](https://github.com/sgosaiw/YOLO_filament/blob/main/1.jpeg?raw=true)

**Utility programs**
convert_gif_mp4.py : Convert a colored or BW GIF animation to BW mp4 file
convert_gif_HE_mp4.py: Convert a colored or BW GIF animation to BW mp4 file with HistogramEqualization
download.py: Download images from internet search.
