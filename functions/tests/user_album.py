'''
@File    :   user_album.py
@Time    :   2022/05/15 20:09:16
@Author  :   Liuanglin
@Desc    :   定义函数 make_album()
使用 while 循环
允许用户自行录入专辑信息
'''


def make_album(limit=3):
    albums = {}
    count = 0
    while count < limit:
        album = {}
        artist = input('enter artist : ')
        title = input('enter title : ')
        number_of_songs = input('how many songs in this album : ')
        album['aritst'] = artist.title()
        album['title'] = title.title()
        album['number_of_songs'] = number_of_songs
        count += 1
        albums[count] = album
    return albums


albums = make_album()


def format_index(index):
    if (index == 1): return f'1st'
    if (index == 2): return f'2nd'
    if (index == 3): return f'3rd'
    return f'{index}th'


for index, album in albums.items():
    print(f'{format_index(index)} album : ')
    for key, info in album.items():
        print(f'\t{key} : {info}')
    print('---------')
