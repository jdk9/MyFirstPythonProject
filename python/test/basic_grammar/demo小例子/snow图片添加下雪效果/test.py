import base64
import os
from memory_pic import snow_jpg

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

get_pic(snow_jpg, 'snow_jpg')
# 在这里使用图片 icon.ico
os.remove('snow_jpg')