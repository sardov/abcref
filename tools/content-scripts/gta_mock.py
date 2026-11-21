import sys; sys.path.insert(0,'/home/claude/content')
from mock import *
from PIL import ImageFont
DJ='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def star_mask(width_px,ss=4):
    f=ImageFont.truetype(DJ,200); d=ImageDraw.Draw(Image.new('L',(10,10)))
    t='★★★★★'; l,tp,r,b=d.textbbox((0,0),t,font=f); s=width_px*ss/(r-l)
    f=ImageFont.truetype(DJ,int(200*s)); l,tp,r,b=d.textbbox((0,0),t,font=f)
    m=Image.new('L',(r-l+40,b-tp+40),0); ImageDraw.Draw(m).text((20-l,20-tp),t,font=f,fill=255)
    m=m.resize((m.width//ss,m.height//ss),Image.LANCZOS); return np.asarray(m).astype(np.float32)/255,20//ss
def mock(blank,text,cm=11):
    f,cx,top,ppc=BLANKS[blank]; fab=cv2.cvtColor(cv2.imread(f),cv2.COLOR_BGR2RGB).astype(np.float32)
    if text=='★★★★★': m,pad=star_mask(cm*0.8*ppc)
    else: m,pad=text_mask(text,cm*ppc)
    h,w=m.shape; embroider(fab,m,int(cx-w/2),int(top-pad),WHITE_THREAD)
    return Image.fromarray(fab.astype(np.uint8))
P=[('wasted','wasted'),('stars','★★★★★'),('wanted','wanted'),('she','she will appreciate this'),('worth','worth the wait'),('since','waited since 2013'),('florida','florida man')]
for k,t in P:
    for b in ['b5','b7']:
        mock(b,t).resize((1200,1200),Image.LANCZOS).save(f'gta/{k}_{b}.jpg',quality=92)
print('ok')
