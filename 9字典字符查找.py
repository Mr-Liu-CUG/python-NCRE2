#
# 在......上补充一行或多行代码
# 不得修改其他代码
#

import random
random.seed(2)

pdict= {'Alice':['123456789'],
        'Bob':['234567891'],
        'Lily':['345678912'],
        'Jane':['456789123']}

name = input('请输入一个人名:')
if name in pdict:
    print("{} {} {}".format(name, pdict[name][0], random.randint(1000,9999)))
else:
    print("对不起，您输入的用户信息不存在。")
