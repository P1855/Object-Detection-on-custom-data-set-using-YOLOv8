# Object-Detection-on-custom-data-set-using-YOLOv8
This project uses **Ultralytics** library importing **YOLOv8** object detection tool to detect object on a custom dataset.
Here, the object used for detection is Alpaca. The YOLOv8 model was trained using the training data and validation set was used for validating the prediction of the model. 
## The result
The model detected object with an **User's accuracy** of **80%** and **precision** of **84%**. The results can be further improved by increasing the depth of object detection ( increasing the number of epochs, more randomised training dataset, etc.)
Also the model was then used for object detection on a custom dataset, here two custom videos were used for detecting the **Alpacas** in the videos. The model could correctly detect the Alpacas and return the object detection in the output videos.

## The dataset
The data used in this project is downloaded by downloading [downloader.py](https://raw.githubusercontent.com/openimages/dataset/master/downloader.py) file from the **Open Images Dataset V7** and then downloading the test, train and validation datasets. Then the images were transformed to YOLO format.
