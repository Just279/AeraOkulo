from ultralytics import YOLO

def start_photo(url):
    model = YOLO("./test_photo.pt")
    threshold = 0.5
    results = model(str(url), save=True, imgsz=480, save_txt=True, project='./', name='apliko/static/sv_imgs', exist_ok=True)

