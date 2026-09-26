import sys
from PIL import Image,ImageDraw,ImageFont
"""Video thumbnail: python tools/make-thumbnail.py frame.png out.jpg "About today's grammar" "Mrs. Rachel Lynde" "Lesson 7.1"
   Pull the frame first:  ffmpeg -ss 32 -i video.mp4 -frames:v 1 frame.png"""
src,out,sub=sys.argv[1:4]
name=sys.argv[4] if len(sys.argv)>4 else 'Mrs. Rachel Lynde'
lesson=sys.argv[5] if len(sys.argv)>5 else 'Lesson 7.1'
im=Image.open(src).convert('RGB');W,H=im.size
ov=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(ov)
# a soft dark corner, top-left, over the sky — away from the face and
# from the player's controls, which cover the bottom of the frame
for r in range(520,0,-4):
    a=int(170*(1-r/520)**1.2)
    d.ellipse([-r*1.1,-r*0.75,r*1.1,r*0.75],fill=(28,22,14,a))
F='/usr/share/fonts/truetype/liberation2/'
t1=ImageFont.truetype(F+'LiberationSerif-Bold.ttf',44);t2=ImageFont.truetype(F+'LiberationSerif-Italic.ttf',27)
x,y=36,26
for dx,dy,col in ((2,2,(0,0,0,130)),(0,0,(255,250,238,255))):
    d.text((x+dx,y+dy),name,font=t1,fill=col)
d.text((x,y+56),sub,font=t2,fill=(250,236,206,255))
d.text((x,y+90),lesson,font=t2,fill=(250,236,206,235))
Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB').save(out,quality=82,optimize=True,progressive=True)
