import sys; sys.path.insert(0,'/home/claude/content')
from mock import *
from slides import ins, cr, mark, GR, BONEC, BG, TX, LN
from PIL import Image, ImageDraw
import numpy as np, cv2
W,H=1080,1350; DK=(20,20,19); CARD=(236,230,218)  # было #A99E90 — слишком тёмный, исключён 21 нояб; теперь bone #ECE6DA
def fit(img,w): return img.resize((w,int(img.height*w/img.width)),Image.LANCZOS)
def mk(blank,text): return mock_text(blank,text,cm=11)
def label(d,x,y,no,ph,line,col=TX,sub=LN):
    d.text((x,y),f'no. {no:02d}',font=ins(28),fill=sub,anchor='lm')
    d.text((x,y+70),ph,font=cr(76),fill=col,anchor='lm')
    d.text((x,y+140),line,font=cr(36,400),fill=sub,anchor='lm')
def brand(d,col=TX): d.text((W-70,H-70),'soft spawn',font=cr(34,400),fill=col,anchor='rm')
def slideA(no,ph,line):
    im=Image.new('RGB',(W,H),BG); im.paste(fit(mk('b5',ph),880),(100,20)); d=ImageDraw.Draw(im); label(d,80,1000,no,ph,line); brand(d); return im
def slideB(no,ph,line):
    im=Image.new('RGB',(W,H),BG); im.paste(fit(mk('b7',ph),880),(100,20)); d=ImageDraw.Draw(im); label(d,80,1000,no,ph,line); brand(d); return im
def slideC(no,ph,line):
    tee=mk('b5',ph); im=Image.new('RGB',(W,H),BG)
    mac=tee.crop((730,300,1260,600)).resize((W,int(300*W/530)),Image.LANCZOS); im.paste(mac.crop((0,0,W,min(mac.height,760))),(0,0))
    im.paste(fit(tee,360),(W-410,800)); d=ImageDraw.Draw(im); label(d,80,900,no,ph,line); brand(d); return im
def hook(lines,sub,bg,fg,fn):
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); y=H*0.40-len(lines)*55
    for l in lines: d.text((W/2,y),l,font=cr(96),fill=fg,anchor='mm'); y+=112
    d.text((W/2,y+50),sub,font=ins(36),fill=fg,anchor='mm'); d.text((W/2,H-110),'soft spawn',font=cr(40,400),fill=fg,anchor='mm'); im.save(fn,quality=92)
def end(bg,fg,fn,line='which one would you wear?'):
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); mark(d,W/2,H*0.38,150,fg,width=5)
    d.text((W/2,H*0.58),'soft spawn',font=cr(90,500),fill=fg,anchor='mm'); d.text((W/2,H*0.58+100),line,font=ins(36),fill=fg,anchor='mm')
    d.text((W/2,H*0.58+160),'softspawn.com · join the lobby',font=ins(30),fill=fg,anchor='mm'); im.save(fn,quality=92)
CAR={
 'cs':('A',[('rush b','a plan, technically.'),('1 hp','still in it.'),('clutch',"1v3. don't talk to me."),('ace','five for five.'),('nt','nice try. we both know.'),('smoke mid','and pray.'),('35hp','enough.')]),
 'lol':('C',[('ff 15','a polite way to give up.'),('mid or feed','a negotiation.'),('jungle diff',"it's always the jungler."),('0 / 10 / 2','the kda speaks.'),('penta','screenshot it.'),('space created','trust me.'),('pos 5','the real carry.')]),
 'gen':('B',[('afk','back in 5.'),('brb','never back.'),('skill issue','said with love.'),('tilted','one more though.'),('respawning','give me a second.'),('touch grass','tomorrow.'),('mute all','peace.')]),
}
F={'A':slideA,'B':slideB,'C':slideC}
for k,(st,items) in CAR.items():
    for i,(ph,line) in enumerate(items,1):
        F[st](i,ph,line).save(f'plan/{k}_{i+1:02d}.jpg',quality=90)
hook(['only players','will understand'],'which one would you wear?',GR,BONEC,'plan/cs_01.jpg'); end(DK,BONEC,'plan/cs_09.jpg')
hook(['if you get it,','you get it'],'pick one. comment it.',BG,TX,'plan/lol_01.jpg'); end(GR,BONEC,'plan/lol_09.jpg',"what's missing? drop your line.")
hook(['you said it','a thousand times'],'now wear it.',CARD,TX,'plan/gen_01.jpg'); end(DK,BONEC,'plan/gen_09.jpg','tag the one who says this.')
# stories 9:16
SW,SH=1080,1920
def story(lines,sub,bg,fg,fn):
    im=Image.new('RGB',(SW,SH),bg); d=ImageDraw.Draw(im); y=SH*0.42-len(lines)*60
    for l in lines: d.text((SW/2,y),l,font=cr(104),fill=fg,anchor='mm'); y+=120
    if sub: d.text((SW/2,y+60),sub,font=ins(38),fill=fg,anchor='mm')
    d.text((SW/2,SH-200),'soft spawn',font=cr(44,400),fill=fg,anchor='mm'); im.save(fn,quality=90)
story(['no logos.','just signals.'],'',GR,BONEC,'plan/st_q1.jpg')
story(["you see it,","others don't."],'clothing for those who know',BG,TX,'plan/st_q2.jpg')
story(['which one','would you wear?'],'vote in the poll ↓',DK,BONEC,'plan/st_poll.jpg')
story(['new post'],'swipe through. pick one.',CARD,TX,'plan/st_newpost.jpg')
print('done')
