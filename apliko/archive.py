import zipfile
from ultralytics import YOLO
import os

def start_archive(path,name):
    with zipfile.ZipFile(path+'/'+name+'.zip','r') as zip_ref:
        zip_ref.extractall('./apliko/static/sv_archive/'+name+'/')

    model = YOLO("./test_archive.pt")

    results = model('./apliko/static/sv_archive/'+name+'/', save=True, imgsz=480, save_txt=True, project='./', name='apliko/static/sv_archive/'+name, exist_ok=True)

def create_archive(path,name):
    zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()
