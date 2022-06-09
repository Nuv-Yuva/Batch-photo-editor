from PIL import Image , ImageFont , ImageDraw , ImageOps
import pandas as pd
df = pd.read_csv('regs.csv') 


for i in range(1,168):

    #adding photos
    
    img1 = Image.open(r"main-photo.png")
    img2 = Image.open(r"photo-to-be-added.png")
    img3 = Image.open(r"photo-to-be-added.png")
    img1.paste(img2, (2320,1740), mask = img2)                      #adding image 1
    img1.paste(img3, (500,1790), mask = img3)                       #adding image 2
    




    #adding the text 

    I1 = ImageDraw.Draw(img1)                                       #confirming changes
    fnt = ImageFont.truetype(r'Nunito-Medium.ttf', 80)              #font
    txt = Image.new(mode="L",size=(1135,600))                       #the text description
    d = ImageDraw.Draw(txt)





    #adding the qr code

    d.text( (0,0), df.iloc[i-1]["nam"],font = fnt, fill = (255))    #data frame for data here i used "nam" bcoz i could not edit it in excel for some reason, change accordingly
    w=txt.rotate(0,  expand=1)                                      #rotating text for the id of qr code
    img1.paste( ImageOps.colorize(w, (0,0,0), (255,255,255)), (1360,1440),  w)  #pasting the text 


    img1.save('./certificates/' + str(i) + '.png')                  #saving final image 
    # img1.show()