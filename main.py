from PIL import Image, ImageDraw, ImageFont
#from PIL.ExifTags import TAGS
import textwrap

FONT_TYPE='./font/K2FyfZJVlfNNSEBXGb7TCI6oBjLz.ttf'
FONT_SIZE=40
# sqaure images
width = 1080
height = 1080

# landscape images
# width = 1080
# height = 566

# Simple black bg image
# img  = Image.new( mode = "RGB", size = (width, height) )
# img.show()


img = Image.new( mode = "RGB", size = (width, height), color = (73, 109, 137))
fnt = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
d = ImageDraw.Draw(img)
wid, ht = 10, 32
MAX_W, MAX_H = 1080, 1080
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

# # extracting the exif metadata
# exifdata = img.getexif()
 
# # looping through all the tags present in exifdata
# for tagid in exifdata:
     
#     # getting the tag name instead of tag id
#     tagname = TAGS.get(tagid, tagid)
 
#     # passing the tagid to get its respective value
#     value = exifdata.get(tagid)
   
#     # printing the final result
#     print(f"{tagname:25}: {value}")
    
#image = Image.new("RGB", (600, 400), "blue")
#draw = ImageDraw.Draw(img)
#font = ImageFont.truetype(FONT_TYPE, 32)
#text_color = (255, 255, 255) # white
#text = "Let's write a Python tutorial showing how to center a multiline string vertically and horizontally on an image using the Pillow library."

# astr = '''The rain in Spain falls mainly on the plains.'''
# para = textwrap.wrap(astr, width=15)

# MAX_W, MAX_H = 200, 200
# im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype(
#     FONT_TYPE, 18)
# draw.text((width/2, height/2), astr, font=FONT_TYPE)
# im.show()