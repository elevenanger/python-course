'''
@File    :   album.py
@Time    :   2022/05/15 19:53:29
@Author  :   Liuanglin
@Desc    :   定义一个名为 make_album() 的函数
该函数创建一个描述专辑的字典
专辑艺术家和标题作为参数
返回包括该参数的字典
使用此函数创建三个不同的专辑并打印返回值信息

使用 None 添加可选参数 曲目数量
如果该参数有被正常赋值
则将该信息添加到字典中
至少一次有曲目数量的函数调用
'''


def make_album(artist, title, number_of_songs=None):
    album = {}
    album['artist'] = artist.title()
    album['title'] = title.title()
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


lake_baikal = make_album('li jian', 'lake baikal')
forest = make_album('george winston', 'forest', number_of_songs=16)
vaper = make_album(artist='cloud cover', title='vaper', number_of_songs=7)

print(lake_baikal)
print(forest)
print(vaper)
