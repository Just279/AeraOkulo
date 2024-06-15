import zipfile
import os

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('Новая папка/Python2.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('z1_H4BfqdI/', zipf)
zipf.close()
