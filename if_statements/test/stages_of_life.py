'''
@File    :   stages_of_life.py
@Time    :   2022/05/03 11:03:00
@Author  :   Liuanglin
@Desc    :   人生的阶段
1、小于 2 岁 baby
2、2~4 岁 toddler
3、4~13 岁 kid 
4、13~20 岁 teenager 
5、20~65 adult
6、60 岁或以上 elder
'''

person_stage = ['baby', 'toddler', 'kid', 'teenager', 'adult', 'elder']
person_stage_age = [0, 2, 4, 13, 20, 65]
persons_age = [1, 3, 5, 15, 23, 70]
for age in persons_age:
    if age >= person_stage_age[0] and age < person_stage_age[1]:
        print(person_stage[0])
    elif age >= person_stage_age[1] and age < person_stage_age[2]:
        print(person_stage[1])
    elif age >= person_stage_age[2] and age < person_stage_age[3]:
        print(person_stage[2])
    elif age >= person_stage_age[3] and age < person_stage_age[4]:
        print(person_stage[3])
    elif age >= person_stage_age[4] and age < person_stage_age[5]:
        print(person_stage[4])
    else:
        print(person_stage[5])
