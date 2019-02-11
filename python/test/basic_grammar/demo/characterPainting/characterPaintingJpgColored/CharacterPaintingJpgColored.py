#-*- coding:utf-8 -*-
'''
    [简单实现图片转彩色字符画](https://blog.csdn.net/kongfu_cat/article/details/79511087)
'''
import os
from PIL import Image, ImageFont, ImageDraw
import argparse

'''
    # #当做命令行运行的时候
    # #命令行输入参数处理
    # parser = argparse.ArgumentParser()
    # parser.add_argument('file')
    # parser.add_argument('-o','--output')
    # #获取参数
    # args = parser.parse_args()
    # File = args.file
    # OUTPUT = args.output
'''
file_name = '魏舒婷.png'
# file_name = '比特币.jpg'

# ascii_char = list("MNHQ$OC67)oa+>!:+. ")
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将像素转换为ascii码
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    '''
        # #当做命令行运行的时候
        im = Image.open(File)
    '''
    im = Image.open(file_name)
    width = int(im.width/2) #高度比例为原图的1/6较好，由于字体宽度
    height = int(im.height/5)  #高度比例为原图的1/15较好，由于字体高度
    im_txt = Image.new("RGB",(im.width*3,im.height*3),(255,255,255))
    im = im.resize((width,height),Image.NEAREST)
    txt = ""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j,i))
            colors.append((pixel[0],pixel[1],pixel[2]))#记录像素颜色信息
            if(len(pixel) == 4):
                txt += get_char(pixel[0],pixel[1],pixel[2],pixel[3])
            else:
                txt += get_char(pixel[0],pixel[1],pixel[2])
        txt += '\n'
        colors.append((255,255,255))
    dr = ImageDraw.Draw(im_txt)
    font=ImageFont.load_default().font#获取字体
    x=y=0
    #获取字体的宽高
    font_w,font_h=font.getsize(txt[1])
    font_h *= 1.37 #调整后更佳
    #ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x+=font_h
            y=-font_w
        dr.text([y,x],txt[i],colors[i])
        y+=font_w
    #输出
    # im_txt.save("output.png")
    im_txt.save(file_name.split('.')[0]+'-character.png')