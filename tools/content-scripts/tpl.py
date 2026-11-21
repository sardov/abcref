import sys; sys.path.insert(0,'/home/claude/content')
from mock import *
from slides import ins, cr, mark, BG, TX, GR, LN, BONEC
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
W,H=1080,1350
PH='rush b'; NO=3; LINE='a plan, technically.'
def label(d,x,y,col=TX,sub=LN):
    d.text((x,y),f'no. {NO:02d}',font=ins(28),fill=sub,anchor='lm')
    d.text((x,y+70),PH,font=cr(76),fill=col,anchor='lm')
    d.text((x,y+140),LINE,font=cr(36,400),fill=sub,anchor='lm')
def brand(d,col=TX): d.text((W-70,H-70),'soft spawn',font=cr(34,400),fill=col,anchor='rm')
def fit(img,w): return img.resize((w,int(img.height*w/img.width)),Image.LANCZOS)
tee=mock_text('b5',PH,cm=11); fold=mock_text('b7',PH,cm=11)
# V1 whole tee on paper
im=Image.new('RGB',(W,H),BG); t=fit(tee.crop((150,120,1850,1880)),860); im.paste(t,((W-t.width)//2,40))
# blend edges: paste on BG-like bg; blank bg is ~(239,231,221) already
d=ImageDraw.Draw(im); label(d,80,1000); brand(d); im.save('tpl/v1_whole.jpg',quality=90)
# V2 folded
im=Image.new('RGB',(W,H),BG); t=fit(fold.crop((330,560,1670,1640)),900); im.paste(t,((W-t.width)//2,80))
d=ImageDraw.Draw(im); label(d,80,1020); brand(d); im.save('tpl/v2_folded.jpg',quality=90)
# V3 macro + small whole
im=Image.new('RGB',(W,H),BG); mac=tee.crop((730,300,1260,600)); mac=mac.resize((W,int(mac.height*W/mac.width)),Image.LANCZOS)
im.paste(mac.crop((0,0,W,min(mac.height,760))),(0,0))
sm=fit(tee.crop((150,120,1850,1880)),360); im.paste(sm,(W-sm.width-50,800))
d=ImageDraw.Draw(im); label(d,80,900); brand(d); im.save('tpl/v3_macro.jpg',quality=90)
# V4 dark museum
dk=np.array(tee.crop((150,120,1850,1880))).astype(np.float32)
bgmask=(np.abs(dk-np.array([239,231,221])).sum(2)<40)
dk[bgmask]=[20,20,19]
im=Image.new('RGB',(W,H),(20,20,19)); t=fit(Image.fromarray(dk.astype(np.uint8)),860)
yy,xx=np.mgrid[0:H,0:W]; spot=np.exp(-(((xx-W/2)/520)**2+((yy-420)/520)**2))
base=np.array(im).astype(np.float32)+spot[...,None]*28; im=Image.fromarray(np.clip(base,0,255).astype(np.uint8))
im.paste(t,((W-t.width)//2,40))
d=ImageDraw.Draw(im); label(d,80,1000,col=BONEC,sub=(150,150,140)); brand(d,BONEC); im.save('tpl/v4_dark.jpg',quality=90)
# hooks 4:5
def hook(lines,sub,fn):
    im=Image.new('RGB',(W,H),GR); d=ImageDraw.Draw(im); y=H*0.40-len(lines)*55
    for l in lines: d.text((W/2,y),l,font=cr(96),fill=BONEC,anchor='mm'); y+=112
    d.text((W/2,y+50),sub,font=ins(36),fill=BONEC,anchor='mm')
    d.text((W/2,H-110),'soft spawn',font=cr(40,400),fill=BONEC,anchor='mm'); im.save(fn,quality=90)
hook(['only players','will understand'],'which one would you wear?','tpl/hook_a.jpg')
hook(['if you get it,','you get it'],'pick one. comment it.','tpl/hook_b.jpg')
hook(['said it','a thousand times'],'now wear it.','tpl/hook_c.jpg')
