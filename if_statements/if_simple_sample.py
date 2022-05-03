'''
@File    :   if_simple_sample.py
@Time    :   2022/05/02 18:50:38
@Author  :   Liuanglin
@Desc    :   简单的 if 表达式
'''

'''
if condition expression : 
    logic expression
== != 
'''
cars = ['infiniti','auto','bmw','benz']
for car in cars :
    if car == 'bmw' :
        print(car.title())
    elif car.lower() != 'auto'.lower():
        print(car.upper())
    else :
        print(car)

# 数字的比较可以直接使用数学运算符
age = 29
if age >= 10 : print('nice age')
if age <= 30 : print('young')
age_2 = 27
# 使用 and 组合条件，判断多个条件都为 true 
if age > 20 and age_2 < 30 and age != 40 :
    print(age+age_2)
# 使用 or 组合条件，判断多个条件中存在 true 
if age <= 30 or age_2 >=40 :
    print(age-age_2)
# 使用 in 判断某个元素是否在列表中
if 'audi' in cars :
    print('we got audi here')
else:
    print('audi not for sale')
# 使用 not in 判断某个元素不在列表中
if 'xiaopeng' not in cars:
    print('sorry ~')