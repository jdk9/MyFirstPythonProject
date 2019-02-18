import itchat, time, random
'''
    给微信所有好友发送一段话
    原文链接: [MyApp/PythonApplication1/自己的小练习/Happy-Mid-Autumn-Festival.py](https://github.com/xiaoxiaoyao/MyApp/blob/master/PythonApplication1/%E8%87%AA%E5%B7%B1%E7%9A%84%E5%B0%8F%E7%BB%83%E4%B9%A0/Happy-Mid-Autumn-Festival.py)
'''

# 群发内容（随机选一条）
SINCERE_WISH = [u'祝中秋快乐',u'中秋快乐呀',u'中秋快乐哟',u'中秋节快乐呀~',u'中秋节快乐!',u'中秋国庆快乐!']
itchat.auto_login(True)
i=1
friendList = itchat.get_friends(update=True)[i:]

print('即将给',len(friendList),'个好友发送中秋祝福，祝福内容为以下随机挑一个：\n',SINCERE_WISH)

for friend in friendList:
    # 祝福语中随机选一条
    SEND_WISH=random.choice(SINCERE_WISH)
    try:
        # 如果是演示目的，把下面的 itchat.send 方法改为 print 即可
        itchat.send(SEND_WISH, friend['UserName'])
        print(friend['UserName'],'\n第',i,'个好友已经成功发送，发送内容为',SEND_WISH)
        # print(friend['DisplayName'] or friend['NickName'])
        # 为了防止封号，自动延时发送
        time.sleep(1+random.random()*124)
    except Exception:# 用于解决异常情况
        print(Exception,":")
        print('ERROR!\n第',i,'个好友发送失败，以下是详细信息')
        friend
    finally:
        # 计数
        i=i+1