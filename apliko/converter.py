import subprocess

def convert_avi_to_mp4(inp,out):
    try:
        subprocess.run([
            'ffmpeg','-i',inp,
            '-c:v','libx264','-c:a','aac',out
            ])
    except:
        try:
            while inp.find('/')!=-1:
                ind9=inp.find('/')
                inp=inp[:ind9]+'\\'+inp[ind9+1:]
            while out.find('/')!=-1:
                ind9=out.find('/')
                out=out[:ind9]+'\\'+out[ind9+1:]
            subprocess.run([
            'ffmpeg','-i',inp,
            '-c:v','libx264','-c:a','aac',out
            ])
        except Exception as e:
            print(e)

#inp2='vid2_m1vdpEN.avi'
#out2='vid2_m1vdpEN.mp4'
#convert_avi_to_mp4(inp2,out2)
