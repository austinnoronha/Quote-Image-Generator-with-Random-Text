import os
from dotenv import load_dotenv

load_dotenv()

QUOTE_GEN_API = os.getenv('QUOTE_GEN_API')
SAMPLE_TEXT = os.getenv('SAMPLE_TEXT')
FONT_SIZE = int(os.getenv('FONT_SIZE'))
FONT_TYPE = os.getenv('FONT_TYPE')
#FONT_TYPE='./font/6NUK8FKMIQOGaw6wjYT7ZHG_zsBBfiftWmA08mCgdfM.ttf'
BG_COLOR_SET = [
    (2, 48, 71),
    (40, 54, 24),
    (38, 70, 83),
    (240, 234, 210),
    (20, 33, 61),
    (244, 140, 6)
]
TEXT_COLOR_SET = [
    (255, 183, 3),
    (254, 250, 224),
    (231, 111, 81),
    (181, 131, 141),
    (252, 163, 17),
    (3, 7, 30)
]