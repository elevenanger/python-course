import unittest
from anonymous_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试 AnonymousSurvey 类"""

    def test_store_single_response(self):
        """使用 assertIn 方法测试元素是否存在数组中"""
        question = "你最喜欢吃的水果："
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("葡萄")
        self.assertIn('葡萄', my_survey.response)

    def test_store_many_response(self):
        question = "你最喜欢吃的水果："
        my_survey = AnonymousSurvey(question)
        fruits = ["葡萄", "香蕉", "梨子"]
        for res in fruits:
            my_survey.store_response(res)
        for res in my_survey.response:
            self.assertIn(res, fruits)


if __name__ == '__main__':
    unittest.main()
