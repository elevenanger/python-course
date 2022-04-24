'''
@File    :   animals.py
@Time    :   2022/04/23 21:44:20
@Author  :   Liuanglin
@Desc    :   具备相似特征的三种动物
分别用一句话描述各个动物
最后描述它们的共同特征
'''

wild_cats = ['lion','leopard','tiger']
desc = ['king of the jungle','neaty hunter','king of beasts']
index = 0
for cat in wild_cats :
    print(f'{cat.title()} is {desc[index]}')
    index = index + 1
print('They are all cats.')