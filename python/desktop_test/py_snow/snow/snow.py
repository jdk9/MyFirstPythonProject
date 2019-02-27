# 导入相应模块
import pygame
import random
import base64
import os
from memory_pic import snow_jpg

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()

# pygame初始化
pygame.init()
# 取出图片
get_pic(snow_jpg, 'snow.jpg')
# 声明屏幕/窗口size大小，与背景图片的大小一样才能完美显示
SIZE = (1280, 821)
# 给屏幕设置大小，参数为上面设置的大小
screen = pygame.display.set_mode(SIZE)
# 设置标题
pygame.display.set_caption("下雪了")
# 加载背景图
background = pygame.image.load('snow.jpg')

# 定义一个雪花列表
snow = []
# 初始化雪花
for i in range(300):
    # randrange()方法返回指定递增基数集合中的一个随机数
    # randrange()是不能直接访问的，需要导入random模块，然后通过ranom静态对象调用
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    # ranint用于生成指定范围内的随机整数
    speedx = random.randint(-1, 1)
    speedy = random.randint(3,6)
    snow.append([x, y, speedx, speedy])
# 创建时钟对象，用来控制游戏循环频率
clock = pygame.time.Clock()

done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 绘制位图
    screen.blit(background, (0,0))


    # 雪花列表循环
    for i in range(len(snow)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3]-3)
        # 移动雪花位置（下一次循环起效）
        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow[i][1] > SIZE[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, SIZE[0])
    # 更新显示到屏幕表面
    pygame.display.flip()
    # 每秒循环20次
    clock.tick(20)

os.remove('snow.jpg')
pygame.quit()