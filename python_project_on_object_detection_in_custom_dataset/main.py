from ultralytics import YOLO
model = YOLO("yolov8n.yaml") #build a new model from scratch
results = model.train(data='config.yaml', epochs=60)