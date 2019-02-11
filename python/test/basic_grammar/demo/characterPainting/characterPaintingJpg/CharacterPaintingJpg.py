# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:45:47 2016

@author: yxz15
"""

from PIL import Image
import os

file_name = 'test.jpg';
# file_name = '啊.jpg';
# file_name = '棒.jpg';
# serarr=['@','-',' ']
serarr=['$','@','B','%','8','&','W','M','#','*',
        'o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t',
        '/','\\','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','!','l','I',';',':',',','\"','^','`','\'','.' ]
# serarr=['@','#','$','%','&','?','*','o','/','{','[','(','|','!','^','~','-','_',':',';',',','.','`',' ']
count=len(serarr)

def toText(image_file):
    image_file=image_file.convert("L")#转灰度
    asd =''#储存字符串
    for h in range(0,  image_file.size[1]):#h
        for w in range(0, image_file.size[0]):#w
            gray =image_file.getpixel((w,h))
            asd=asd+serarr[int(gray/(255/(count-1)))]
        asd=asd+'\n'
    return asd

def toText2(image_file):
    asd =''#储存字符串
    for h in range(0,  image_file.size[1]):#h
        for w in range(0, image_file.size[0]):#w
            r,g,b =image_file.getpixel((w,h))
            gray =int(r* 0.299+g* 0.587+b* 0.114)
            asd=asd+serarr[int(gray/(255/(count-1)))]
        asd=asd+'\n'
    return asd


image_file = Image.open(file_name) # 打开图片
image_file=image_file.resize((int(image_file.size[0]*0.8), int(image_file.size[1]*0.4)))#调整图片大小
# image_file=image_file.resize((int(image_file.size[0]*0.9), int(image_file.size[1]*0.5)))#调整图片大小

print(u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)
try:
    os.remove('./tmp.txt')
except  WindowsError:
    pass

tmp=open('tmp.txt','a')


tmp.write(toText2(image_file))

tmp.close()