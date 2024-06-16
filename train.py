from ultralytics import YOLO

device = "cuda"

def main():
    # Load a model
    model = YOLO("yolov8m.yaml")  # build a new model from scratch
    model.to(device)

    # Use the model
    results = model.train(data="config.yaml", imgsz=480, epochs=50)  # train the model
    metrics = model.val()  # validate the model

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()
    main()
