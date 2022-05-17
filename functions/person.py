'''
@File    :   person.py
@Time    :   2022/05/17 21:14:18
@Author  :   Liuanglin
@Desc    :   人物模块
'''


def person_info(first_name,last_name,**other_info) :
    person = {}
    person['first'] = first_name.title()
    person['last'] = last_name.title()
    for k,v in other_info.items() :
        person[k] = v.title()
    return person

def describe_person(person) :
    print(f"{person['first']} {person['last']} : ")
    for k,v in person.items() :
        if k == 'first' or k == 'last' : continue
        print(f"\t{k} : {v}")