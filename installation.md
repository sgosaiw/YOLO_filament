**Installation instructions**
------------------------------------

**Using conda create an environment and name it accordingly**
 
```
conda create -n yolov8_halpha python=3.9
conda activate yolov8_halpha
```

**Install utilities to download images from web**

```
pip install simple_image_download==0.4
```

Now the code "download_images.py" should work to download images from the web.

** To annotate or label images install labelImg
```
pip install labelImg
```

run "labelImg" command

In a folder store images that we need to label. 
Select the data folder and also the output folder in labelImg.
Also make sure the algorithm selected is YOLO inside labelImg (on left hand panel).
Select boxes around filaments, prominences and active regions.
This will create folder named labels with one label.txt files for each image.
The objects are names in orger in classes.txt
 
Split the labeled data into two sets:
"yolov8" folder
|-----classes.txt   data_custom.yaml
    |---
        "train"             "val"
     images_|_labels   images_|_labels


**Install yolov8**

```
pip install ultralytics
```
This will install Pytorch CPU version. For latest GPU cuda version check Pytorch website. 


```
pip3 install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cuda_versionXX
```

This will uninstall CPU version.

From YOLOv8 site download yolov8m.pt or other model. Larger models accurate but slower.

**Start training and validating on labeled custom data**

** Predict on new data and movies**



 


