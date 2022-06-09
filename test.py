
from PIL import Image , ImageFont , ImageDraw , ImageOps
import pandas as pd
df = pd.read_csv('regs.csv') 


for i in range(1,168):
    
    img1 = Image.open(r"hfc.png")
    img2 = Image.open(r"main2.png")
    img3 = Image.open(r"main3.png")
    img1.paste(img2, (2320,1740), mask = img2)
    img1.paste(img3, (500,1790), mask = img3)
    

    I1 = ImageDraw.Draw(img1)
    fnt = ImageFont.truetype(r'Nunito-Medium.ttf', 80)
    txt = Image.new(mode="L",size=(1135,600))
    d = ImageDraw.Draw(txt)


    d.text( (0,0), df.iloc[i-1]["nam"],font = fnt, fill = (255))
    w=txt.rotate(0,  expand=1)
    img1.paste( ImageOps.colorize(w, (0,0,0), (255,255,255)), (1360,1440),  w)


    img1.save('./certificates/' + str(i) + '.png')
    # img1.show()