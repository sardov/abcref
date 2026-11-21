"""soft spawn — мокапы: текст-вышивка и гравюра-печать на пустых футболках."""
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONTS='/home/claude/abcref/tools/post-generator/fonts/'
BONE=(236,230,218); WHITE_THREAD=(242,241,236); BLACK_THREAD=(28,28,28)
# blank: file, center x, top y of design, px per cm
BLANKS={
 'b1':('blanks/b1_card.png',624,246,13.3),
 'b2':('blanks/b2_dark.png',563,400,12.3),
 'b3':('blanks/b3_stone.png',470,622,34.5),
 'b5':('blanks/b5_coal_front.png',993,376,21.1),
 'b6':('blanks/b6_grey_front.png',993,376,21.1),
 'b7':('blanks/b7_coal_folded.png',999,1030,49.6),
}
def crim(px,w=600):
    f=ImageFont.truetype(FONTS+'CrimsonPro-VF.ttf',px); f.set_variation_by_axes([w]); return f
def text_mask(text,width_px,ss=4,ref='gg, go next'):
    # width_px = width that the REFERENCE phrase would have; all phrases share one font size
    f=crim(200); d=ImageDraw.Draw(Image.new('L',(10,10)))
    l,t,r,b=d.textbbox((0,0),ref,font=f); s=width_px*ss/(r-l)
    f=crim(max(8,int(200*s))); l,t,r,b=d.textbbox((0,0),text,font=f)
    m=Image.new('L',(r-l+40,b-t+40),0); ImageDraw.Draw(m).text((20-l,20-t),text,font=f,fill=255)
    m=m.resize((m.width//ss,m.height//ss),Image.LANCZOS)
    return np.asarray(m).astype(np.float32)/255, 20//ss
def embroider(fab,mask,x,y,color):
    h,w=mask.shape; reg=fab[y:y+h,x:x+w].astype(np.float32)
    # satin-stitch texture: fine diagonal lines + noise
    yy,xx=np.mgrid[0:h,0:w]; stitch=0.88+0.12*np.sin((xx+yy*0.35)*2.2)
    stitch*=1+np.random.normal(0,0.04,(h,w))
    # emboss: light from top-left
    blur=cv2.GaussianBlur(mask,(0,0),max(0.8,h/40)); gy,gx=np.gradient(blur)
    shade=np.clip(1+(-gx-gy)*2.0,0.65,1.25)
    col=np.array(color,np.float32)[None,None,:]*(stitch*shade)[...,None]
    # shadow under thread
    sh=cv2.GaussianBlur(np.roll(np.roll(mask,1,0),1,1),(0,0),1.2)[...,None]
    reg=reg*(1-0.45*sh)
    a=np.clip(cv2.GaussianBlur(mask,(0,0),0.5),0,1)[...,None]
    fab[y:y+h,x:x+w]=np.clip(reg*(1-a)+col*a,0,255)
def print_art(fab,art,x,y,ink=(232,226,214),opacity=0.92):
    h,w=art.shape; reg=fab[y:y+h,x:x+w].astype(np.float32)
    detail=reg-cv2.GaussianBlur(reg,(0,0),3)
    a=(np.clip(cv2.GaussianBlur(art,(0,0),0.6),0,1)*opacity)[...,None]
    out=reg*(1-a)+np.array(ink,np.float32)*a+detail*0.8*a
    fab[y:y+h,x:x+w]=np.clip(out,0,255)
def load_art(path,width_px):
    im=Image.open(path).convert('L'); im=im.resize((int(width_px),int(width_px*im.height/im.width)),Image.LANCZOS)
    a=np.asarray(im).astype(np.float32)/255; a=np.clip((a-0.12)/0.75,0,1); return a
def mock_text(blank,text,cm=11,thread='white',caption=None):
    f,cx,top,ppc=BLANKS[blank]; fab=cv2.cvtColor(cv2.imread(f),cv2.COLOR_BGR2RGB).astype(np.float32)
    m,pad=text_mask(text,cm*ppc); h,w=m.shape
    embroider(fab,m,int(cx-w/2),int(top-pad),WHITE_THREAD if thread=='white' else BLACK_THREAD)
    return Image.fromarray(fab.astype(np.uint8))
def mock_art(blank,art_path,cm=20,caption=None,cap_cm=1.3,gap_cm=1.6):
    f,cx,top,ppc=BLANKS[blank]; fab=cv2.cvtColor(cv2.imread(f),cv2.COLOR_BGR2RGB).astype(np.float32)
    a=load_art(art_path,cm*ppc); h,w=a.shape; y=int(top+0.5*ppc)
    print_art(fab,a,int(cx-w/2),y)
    if caption:
        pass
    if caption:
        f2=crim(int(cap_cm*ppc)); d=ImageDraw.Draw(Image.new('L',(1,1)))
        l,t,r,b=d.textbbox((0,0),caption,font=f2); cm_img=Image.new('L',(r-l+10,b-t+10),0)
        ImageDraw.Draw(cm_img).text((5-l,5-t),caption,font=f2,fill=255)
        cap=np.asarray(cm_img).astype(np.float32)/255
        print_art(fab,cap,int(cx-cap.shape[1]/2),int(y+h+gap_cm*ppc))
    return Image.fromarray(fab.astype(np.uint8))
if __name__=='__main__':
    import sys
    for b in ['b1','b2','b3']: mock_text(b,'ff 15',cm=9).save(f'test_ff15_{b}.png')
