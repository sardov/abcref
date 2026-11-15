"""soft spawn — генератор постов и сторис.
python3 make_post.py story  --title "collection 01" --kicker "announcing" --sub "you see it, others don't" --bg photo.png -o out.png
python3 make_post.py text   --title "gg, go next" --lines "embroidered cotton" "oversized fit" --style green -o out.png
python3 make_post.py photo  --bg photo.png -o out.png        (кроп 4:5 под ленту)
"""
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os; F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts')+'/'; IS=F+'instrument-sans-500.ttf'
BG,TX,GR,LN,CD=(239,231,221),(26,26,26),(18,47,37),(76,79,76),(169,158,144)
BONE=(236,230,218)
def crim(s,w=380):
    f=ImageFont.truetype(F+'CrimsonPro-VF.ttf',s); f.set_variation_by_axes([w]); return f
def ins(s): return ImageFont.truetype(IS,s)
def track(d,cx,y,t,font,fill,sp,anchor='center'):
    w=sum(d.textlength(c,font=font) for c in t)+sp*(len(t)-1); x=cx-w/2 if anchor=='center' else cx
    for c in t: d.text((x,y),c,font=font,fill=fill,anchor='lm'); x+=d.textlength(c,font=font)+sp
def cover(path,W,H,top=0.0):
    im=Image.open(path).convert('RGB'); w,h=im.size; r=W/H
    if w/h>r: nw=int(h*r); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else: nh=int(w/r); y=int((h-nh)*top) if top else (h-nh)//2; im=im.crop((0,y,w,y+nh))
    return im.resize((W,H),Image.LANCZOS)
def story(a):
    W,H=1080,1920
    im=cover(a.bg,W,H,top=1.0) if a.bg else Image.new('RGB',(W,H),GR)
    if a.bg: im=ImageEnhance.Color(im).enhance(0.55); im=ImageEnhance.Brightness(im).enhance(0.72)
    d=ImageDraw.Draw(im); cy=int(H*0.40)
    if a.kicker: track(d,W/2,cy-130,a.kicker.upper(),ins(29),BONE,4)
    d.text((W/2,cy),a.title,font=crim(124),fill=BONE,anchor='mm')
    if a.sub: d.text((W/2,cy+150),a.sub,font=ins(33),fill=(214,214,206),anchor='mm',align='center',spacing=14)
    d.line((W/2-54,cy+330,W/2+54,cy+330),fill=BONE,width=2)
    d.text((W/2,H-140),'soft spawn',font=crim(46,400),fill=BONE,anchor='mm')
    return im
def text(a):
    W,H=1080,1350
    bg,fg,sub={'green':(GR,BONE,(200,205,198)),'sand':(CD,TX,LN),'paper':(BG,TX,LN)}[a.style]
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); x=120; y=int(H*0.36)
    if a.kicker: track(d,x,y,a.kicker.upper(),ins(26),sub,4,anchor='left'); y+=90
    for tl in a.title.split('|'):
        d.text((x,y),tl,font=crim(112),fill=fg,anchor='lm'); y+=118
    y-=8
    d.line((x,y,x+90,y),fill=fg,width=2); y+=80
    for l in a.lines or []: d.text((x,y),l,font=ins(34),fill=sub,anchor='lm'); y+=54
    d.text((x,H-120),'soft spawn',font=crim(40,400),fill=fg,anchor='lm')
    return im
def photo(a): return cover(a.bg,1080,1350)
p=argparse.ArgumentParser(); p.add_argument('kind',choices=['story','text','photo'])
p.add_argument('--title',default=''); p.add_argument('--kicker',default=''); p.add_argument('--sub',default='')
p.add_argument('--lines',nargs='*'); p.add_argument('--style',default='green'); p.add_argument('--bg'); p.add_argument('-o',required=True)
a=p.parse_args(); {'story':story,'text':text,'photo':photo}[a.kind](a).save(a.o); print('saved',a.o)
