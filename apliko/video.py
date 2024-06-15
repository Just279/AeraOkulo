import torch
from ultralytics import YOLO

d='cuda:0' if torch.cuda.is_available() else 'cpu'

def start_video(url):
    model = YOLO("./test_video.pt")
    results = model(str(url), save=True, imgsz=480, conf=0.25, stream=True, project='./', name='apliko/static/sv_video', exist_ok=True, device=d)#, verbose=False)

  #  for r in results:
 #       boxes= r.boxes
 #       masks= r.masks
 #       probs= r.probs

    
    dct={}
    alli={
                '0.': 'tensor(0.)',
                '1.': 'tensor(1.)',
                '2.': 'tensor(2.)',
                '3.': 'tensor(3.)',
                '4.': 'tensor(4.)'
            }
    
    for frame_number, result in enumerate(results):
        for detection in result.boxes:
            cls= detection.cls
            key=str(cls)
            for k in alli:
                if k in str(cls):
                    key=alli[k]
            a=dct.get(key,{})
            last=a.get('last',-1)
            start=a.get('start',-1)
            arro=a.get('arro',[])
            if last==-1:
                last=frame_number
                start=frame_number
            else:
                if frame_number-last<8:
                    last=frame_number
                else:
                    arro.append([start,last])
                    start=-1
                    last=-1

            a['last']=last
            a['start']=start
            a['arro']=arro
            dct[key]=a
        jlast=frame_number
                
    for key in dct:          
        a=dct.get(key,{})
        last=a.get('last',-1)
        start=a.get('start',-1)
        arro=a.get('arro',[])
        if last!=-1:
            arro.append([start,last])
        a['last']=last
        a['start']=start
        a['arro']=arro
        dct[key]=a
    a='''
    name_file=str(url)
    name_file=name_file[name_file.rfind('/')+1:]
    name_file=name_file[:name_file.rfind('.')]
    
    out='apliko/static/sv_video/'+name_file+'.txt'
    with open(out,'w') as f:
        for key in dct: 
            f.write(f"KEY {key}\n")
            a=dct.get(key,{})
            arro=a.get('arro',[])
            for arr in arro:
                f.write(f"{arr[0]/jlast} {arr[1]/jlast}\n")
    '''
    st256=''
    lbls={
        'tensor([0.])':'БПЛА (коптер)',
        'tensor([1.])':'Самолет',
        'tensor([2.])':'Вертолет',
        'tensor([3.])':'Птица',
        'tensor([4.])':'БПЛА (самолет)',
        }
    for key in dct: 
        st256+=lbls.get(key)+'_^_'
        a=dct.get(key,{})
        arro=a.get('arro',[])
        for arr in arro:
            st256+=str(arr[0]/jlast)+' '+str(arr[1]/jlast)+'&^_'
        st256+='&$_'

    return st256
