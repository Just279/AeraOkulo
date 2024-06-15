import cv2
from PIL import Image
from ultralytics import YOLO  
import numpy as np
import random
from .models import Mesagoj

model = YOLO('test.pt')

def gen_frames():
    cap = cv2.VideoCapture(0)

    colors={
                'tensor(0.)': (0, 255, 0),
                'tensor(1.)': (255, 0, 0),
                'tensor(2.)': (0, 0, 255),
                'tensor(3.)': (150, 150, 0),
                'tensor(4.)': (0, 150, 150)
            }

    names={
                'tensor(0.)': 'БПЛА (коптер)',
                'tensor(1.)': 'Самолет',
                'tensor(2.)': 'Вертолет',
                'tensor(3.)': 'Птица',
                'tensor(4.)': 'БПЛА (самолет)'
            }
    alarms0={
                'tensor(0.)': -1,
                'tensor(1.)': -1,
                'tensor(2.)': -1,
                'tensor(3.)': -1,
                'tensor(4.)': -1
            }
    alli={
                '0.': 'tensor(0.)',
                '1.': 'tensor(1.)',
                '2.': 'tensor(2.)',
                '3.': 'tensor(3.)',
                '4.': 'tensor(4.)'
            }
    while True:
        ret, frame = cap.read()
        for key in alarms0:
            alarms0[key]-=1
        if not ret:
            break
        image = Image.fromarray(frame[..., ::-1])
        results = model(image)
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        for ind in range(len(results)):
            for detection in results[ind].boxes:
                x_min, y_min, x_max, y_max = detection.xyxy[ind]
                conf = detection.conf[ind] 
                cls = detection.cls[ind]

                key=str(cls)
                for k in alli:
                    if k in str(cls):
                        key=alli[k]
                color=colors.get(key,(0, 255, 0))
                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)
                cv2.putText(frame, f"{model.names[int(cls)]}: {conf:.2f}", (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                if alarms0.get(key,-1)<0 and key in ['tensor(0.)','tensor(4.)']:
                    m=Mesagoj()
                    m.name='Новое сообщение: '+names.get(key,'БПЛА')
                    m.description='Обнаружен '+names.get(key,'БПЛА')
                    m.is_new3=None
                    m.save()
                alarms0[key]=45
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
    cv2.destroyAllWindows()
