import unittest
from anonymous_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试 AnonymousSurvey 类"""

    def setUp(self):
        """setUp() 方法创建对象，并可以在所有的测试案例使用这些对象"""
        question = "你最喜欢的水果："
        self.my_survey = AnonymousSurvey(question)
        self.fruits = ["葡萄", "香蕉", "梨子"]

    def test_store_single_response(self):
        """使用 assertIn 方法测试元素是否存在数组中"""
        self.my_survey.store_response("葡萄")
        self.assertIn('葡萄', self.my_survey.response)

    def test_store_many_response(self):
        for res in self.fruits:
            self.my_survey.store_response(res)
        for res in self.my_survey.response:
            self.assertIn(res, self.fruits)


if __name__ == '__main__':
    unittest.main()
