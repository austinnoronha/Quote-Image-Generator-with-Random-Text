from PIL import Image, ImageDraw, ImageFont
import random
import textwrap

#Configuation and Settings
FONT_TYPE='./font/K2FyfZJVlfNNSEBXGb7TCI6oBjLz.ttf'
FONT_SIZE=40
BG_COLOR_SET = [
    (2, 48, 71),
    (40, 54, 24)
]
TEXT_COLOR_SET = [
    (255, 183, 3),
    (254, 250, 224)
]

def genSimpleImg(MAX_W = 1080, MAX_H = 1080):
    img  = Image.new( mode = "RGB", size = (MAX_W, MAX_H) )
    img.show()
  
def genInstaImg(MAX_W = 1080, MAX_H = 1080):    
    img = Image.new( mode = "RGB", size = (MAX_W, MAX_H), color = (73, 109, 137))
    fnt = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
    d = ImageDraw.Draw(img)
    wid, ht = 10, 32
    text = "Let's write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library."
    #text = "Let's write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library. On write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library"
    para = textwrap.wrap(text, width=FONT_SIZE)
    current_h, pad = ((MAX_W - wid) / 3), 20
    for line in para:
        print(line)
        d.text( 
            #xy=(wid/2, ht/2), 
            xy=((MAX_W - wid) / 2, current_h),
            text=line, 
            #outline = (255, 255, 255),
            font=fnt, 
            fill=(255, 255, 0), 
            #fill=(0, 127, 0),
            #align="center",
            #stroke_width=2, 
            #stroke_fill=2,
            anchor='mm'
            )
        current_h += ht + pad
    #img.save('pil_text_font.png', type='PNG')
    img.show()
    
def genBGImgMesh(MAX_W = 1080, MAX_H = 1080):
    random_index = random.randint(0, len(BG_COLOR_SET)-1)
    foreground_color = BG_COLOR_SET[random_index]
    background = Image.new('RGB', (MAX_W, MAX_H), (0,0,0))
    foreground = Image.new('RGB', (MAX_W, MAX_H), foreground_color)
    mask = Image.new('L', (MAX_W, MAX_H), 0)
    draw = ImageDraw.Draw(mask)
    for i in range(5, MAX_W, 20):
        draw.line((i, 0, i, MAX_W), fill=random.randrange(256))
        draw.line((0, i, MAX_H, i), fill=random.randrange(256))
    
    result = Image.composite(background, foreground, mask)
    #result.show()
    bg_name='bg.png'
    result.save(bg_name, type='PNG')
    writeTextOnImage(bg_name=bg_name, text_index=random_index)
    
def writeTextOnImage(bg_name='bg.png', text_index = 0, MAX_W = 1080, MAX_H = 1080):
    img = Image.open(bg_name)
    #img = Image.new( mode = "RGB", size = (MAX_W, MAX_H), color = (73, 109, 137))
    fnt = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
    d = ImageDraw.Draw(img)
    wid, ht = 10, 32
    text = "Let's write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library."
    #text = "Let's write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library. On write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library"
    para = textwrap.wrap(text, width=FONT_SIZE)
    current_h, pad = ((MAX_W - wid) / 3), 20
    text_color = TEXT_COLOR_SET[text_index]
    for line in para:
        print(line)
        d.text( 
            #xy=(wid/2, ht/2), 
            xy=((MAX_W - wid) / 2, current_h),
            text=line, 
            outline = (255, 7, 12),
            font=fnt, 
            fill=text_color, 
            #fill=(0, 127, 0),
            #align="center",
            stroke_width=2, 
            stroke_fill=2,
            anchor='mm'
            )
        current_h += ht + pad
    #img.save('pil_text_font.png', type='PNG')
    img.show()
    

