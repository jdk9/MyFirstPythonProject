# -*- coding: utf-8 -*-

import urllib
import base64
import json
import sys
import os
import time
import re
import http.cookiejar

'''
    [Python 小冰颜值测试](https://www.jianshu.com/p/53a8276a67da)
'''
class Ice(object):
    """docstring for Ice"""
    ice_page = 'https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi'
    ice_api = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process?{}'
    upload_file_api = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'

    def __init__(self, img_data):
        self.img_data = img_data

    def upLoadFile(self):
        imgdataBase64 = base64.b64encode(self.img_data)
        req = urllib.request.Request(self.upload_file_api, imgdataBase64)

        try:
            response = urllib.request.urlopen(req)
        except Exception:
            print ('Server Error.')
            exit()
        else:
            return response.read()

    def test(self):
        ret = json.loads(self.upLoadFile())
        data = {
            'MsgId': '%d063' % int(time.time()),
            'CreateTime': int(time.time()),
            'Content[imageUrl]': '%s%s' % (ret['Host'], ret['Url']),
        }

        param = {
            'service': 'yanzhi',
        }

        api = self.ice_api.format(urllib.urlencode(param))

        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)

        opener.open(self.ice_page)

        req = urllib.request.Request(
            api,
            urllib.urlencode(data),
            headers={'Referer': self.ice_page},
        )

        response = opener.open(req)
        if response.code == 200:
            ret = json.loads(response.read())
            if ret is None:
                print('Server Error.')
                exit()
            if 'content' in ret:
                print(str(ret['content']['text'].encode('utf-8')))
                print(ret['content']['imageUrl'])
                exit()
        print('Server Error.')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Error: iceface.py [localfile|http].')
        exit()

    # is localfile?
    if not os.path.isfile(sys.argv[-1]):
        rec = re.match(r'^[a-zA-z]+://[^\s]*$', sys.argv[-1])
        if rec is None:
            print('Param error.')
            exit()
        try:
            print('Download File...')
            req = urllib.request.urlopen(sys.argv[-1])
        except Exception:
            print('Download File error.')
            exit()
        else:
            imgdata = req.read()
    else:
        with open(sys.argv[-1], 'rb') as f:
            imgdata = f.read()
    o = Ice(imgdata)
    o.test()