"""soft spawn — слайды 9:16 для каруселей TikTok/IG и роликов."""
import sys; sys.path.insert(0,'/home/claude/content')
from mock import *
from PIL import Image, ImageDraw, ImageFont
F='/home/claude/abcref/tools/post-generator/fonts/'
BG=(239,231,221); TX=(26,26,26); GR=(18,47,37); LN=(76,79,76); BONEC=(236,230,218)
def ins(s): return ImageFont.truetype(F+'instrument-sans-500.ttf',s)
def cr(s,w=500): return crim(s,w)
W,H=1080,1920
def mark(d,cx,cy,R,col,width=3):
    L=0.618*R; d.line((cx-L,cy,cx+L,cy),fill=col,width=width); d.line((cx,cy-L,cx,cy+L),fill=col,width=width)
    r=0.088*R*1.0; d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col)
def hook(title,sub='',style='green'):
    bg,fg=(GR,BONEC) if style=='green' else (BG,TX)
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); y=H*0.40
    for line in title.split('|'):
        d.text((W/2,y),line,font=cr(104),fill=fg,anchor='mm'); y+=120
    if sub: d.text((W/2,y+60),sub,font=ins(38),fill=fg,anchor='mm')
    d.text((W/2,H-170),'soft spawn',font=cr(44,400),fill=fg,anchor='mm')
    return im
def product(mock_img,num,name,line='embroidered cotton · oversized',crop=(443,140,1543,1240)):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    c=mock_img.crop(crop); c=c.resize((W,int(c.height*W/c.width)),Image.LANCZOS)
    im.paste(c,(0,260))
    y=260+c.height+90
    d.text((80,y),f'no. {num:02d}',font=ins(30),fill=LN,anchor='lm')
    d.text((80,y+85),name,font=cr(86),fill=TX,anchor='lm')
    d.text((80,y+170),line,font=ins(32),fill=LN,anchor='lm')
    d.text((W-80,H-110),'soft spawn',font=cr(40,400),fill=TX,anchor='rm')
    return im
def endcard(line1='softspawn.com',line2='join the lobby'):
    im=Image.new('RGB',(W,H),GR); d=ImageDraw.Draw(im)
    mark(d,W/2,H*0.40,170,BONEC,width=5)
    d.text((W/2,H*0.58),'soft spawn',font=cr(96,500),fill=BONEC,anchor='mm')
    d.text((W/2,H*0.58+110),line1,font=ins(40),fill=BONEC,anchor='mm')
    if line2: d.text((W/2,H*0.58+170),line2,font=ins(32),fill=(200,205,198),anchor='mm')
    return im
