import itchat
import pygame

'''
	微信红包提醒
	原文链接: [AhabCode/微信红包助手.py](https://github.com/AhabWang/AhabCode/blob/master/%E5%BE%AE%E4%BF%A1%E7%BA%A2%E5%8C%85%E5%8A%A9%E6%89%8B.py)
'''

'''声音提示'''
def voice ():
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()

'''监控是否有红包-群聊(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=True)
def getNoteGroup(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        # voice()

'''监控是否有红包-个人(Note参数: 通知消息类型)'''
@itchat.msg_register('Note', isGroupChat=False)
def getNote(msg):
    if u'收到红包' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        # voice()

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
    itchat.logout()