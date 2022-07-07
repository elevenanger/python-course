'''
@File    :   polling.py
@Time    :   2022/05/06 22:12:41
@Author  :   Liuanglin
@Desc    :   
发起最爱语言投票
创建一个候选人清单
已经有三个人选择了喜欢的语言
遍历列表
1、如果已经选择了喜欢的语言，感谢他们的选择
2、如果没有做出选择，邀请他们选择
'''

candidates = ['zhao', 'qian', 'sun', 'li']

favorite_language = {
    'zhao': 'java',
    'qian': 'python',
    'sun': 'rust',
}

for name in candidates:
    if name in favorite_language.keys():
        print(f'{name.title()} tks')
    else:
        print(f'{name.title()} please poll for your favorite language')
