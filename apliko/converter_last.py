import cv2

def convert_avi_to_mp4(inp,out):
    try:
        cap=cv2.VideoCapture(inp)
        if not cap.isOpened():
            print('Not opened')
            return
        fr_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fr_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps=cap.get(cv2.CAP_PROP_FPS)

        fourcc=cv2.VideoWriter_fourcc(*'mp4v')
        out=cv2.VideoWriter(out,fourcc,fps,(fr_width,fr_height))

        while True:
            ret, frame=cap.read()
            if not ret:
                break
            out.write(frame)
        cap.release()
        out.release()
    except Exception as e:
        print(e)

#inp2='vid2_m1vdpEN.avi'
#out2='vid2_m1vdpEN.mp4'
#convert_avi_to_mp4(inp2,out2)
