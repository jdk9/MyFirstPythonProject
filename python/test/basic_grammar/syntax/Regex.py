# -*- coding: UTF-8 -*-

import re
strs = [
    '徐雪征,110223198206285329,5,2,北京市通州区漷县镇。www.bdpf.org.cn',
    '米兰,11022319870208602X,5,4,北京市通州区漷县镇。www.bdpf.org.cn',
    '张雪,110223198511066026,5,3,北京市通州区漷县镇。www.bdpf.org.cn',
    '张颖杰,110112199901085329,5,3,北京市通州区漷县镇。www.bdpf.org.cn',
    '张颖杰,,110112199901085329,5,3,北京市通州区漷县镇。www.bdpf.org.cn',
    '毛红娟,11022319781106532X,5,3,北京市通州区漷县镇。www.bdpf.org.cn'
]
for s in strs:
    # print(re.findall(r"(.+?),(.+?),(\d+?),(\d+?),(.+?)。(.+?)",s))
    # print(     re.match(r"([\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20} & [^,]),([\dxX]+?),(\d+?),(\d+?),(.+?)。(.+?)",s))
    print(     re.match(u'(((?!,).)*[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}((?!,).)*),([\dxX]{15,18}?),(\d+?),(\d+?),(.+?)。www.bdpf.org.cn',s))
    print(bool(re.match(u'(((?!,).)*[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}((?!,).)*),([\dxX]{15,18}?),(\d+?),(\d+?),(.+?)。www.bdpf.org.cn',s)))

# print('\n')
# s = 'www.bdpf.org.cn'
# print(re.match(r'[a-zA-Z0-9\.]+', s))
# ((?!abc).)*admin((?!abc).)*