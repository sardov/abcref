import cv2, numpy as np, sys
# remove light embroidery text from a dark tee photo region via inpainting
def blank(src, dst, box):
    im=cv2.imread(src); x0,y0,x1,y1=box
    roi=im[y0:y1,x0:x1]; g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    base=np.median(g)
    m=(g>base+25).astype(np.uint8)*255
    m=cv2.dilate(m,np.ones((5,5),np.uint8),iterations=2)
    mask=np.zeros(im.shape[:2],np.uint8); mask[y0:y1,x0:x1]=m
    out=cv2.inpaint(im,mask,9,cv2.INPAINT_TELEA)
    cv2.imwrite(dst,out); return mask.sum()//255
A='/home/claude/abcref/refs/photokit/'
print(blank(A+'f4-product-card.png','blanks/b1_card.png',(500,180,760,260)))
print(blank(A+'f2-tee-on-dark.png','blanks/b2_dark.png',(470,250,680,330)))
print(blank(A+'f3-folded-on-stone.png','blanks/b3_stone.png',(380,520,760,640)))
