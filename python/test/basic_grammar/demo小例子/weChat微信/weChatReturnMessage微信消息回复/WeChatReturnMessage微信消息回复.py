import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if u'黄彦文' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])

        return '来啦? 老弟!'
    elif u'钱桦' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        return '6啊, 钱桦!'
    elif u'陈凯' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        return '凯哥牛逼! QAQ'
    elif u'高萌' in msg['Text']:
        print('[INFO]: %s' % msg['Text'])
        return 'ॣ ॣ ॣ'

itchat.auto_login()
itchat.run()