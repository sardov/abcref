"""слайды -> ролик 9:16: каждый слайд с медленным зумом, жёсткие склейки."""
import subprocess, sys, glob, os
def make(slides, out, durs, fps=30):
    parts=[]
    for i,(s,d) in enumerate(zip(slides,durs)):
        p=f'/tmp/part_{i}.mp4'; n=int(d*fps)
        vf=(f"scale=1188:2112,zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={fps},format=yuv420p")
        subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-i',s,'-vf',vf,'-t',str(d),'-c:v','libx264','-preset','veryfast','-crf','20',p],check=True)
        parts.append(p)
    with open('/tmp/list.txt','w') as f: f.write(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i','/tmp/list.txt','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','copy','-c:a','aac',out],check=True)
if __name__=='__main__':
    d=sys.argv[1]; out=sys.argv[2]
    s=sorted(glob.glob(d+'/*.png')); durs=[2.2]+[1.4]*(len(s)-2)+[2.5]
    make(s,out,durs); print(out)
