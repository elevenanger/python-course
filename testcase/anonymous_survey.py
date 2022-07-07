# @File  : anonymous_survey.py
# @Author: liuanglin
# @Time: 2022/6/27 20:59 
# -*- coding: utf-8 -*-


class AnonymousSurvey:
    """匿名调查类"""

    def __init__(self, question):
        """存储问题并给予答复"""
        self.question = question
        self.response = []

    def show_question(self):
        """打印问题信息"""
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_result(self):
        print("问卷答案：")
        for res in self.response:
            print(f"- {res}")
