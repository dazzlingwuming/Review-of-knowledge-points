#定义题目类
class Question(object):
    def __init__(self, id = None, question = None,options = None,answer = None ,review_count = 0 ,correct_count = 0,accuracy_rating = None,analysis = None):
        self.id = id
        self.question = question
        self.options = options
        self.answer = answer
        self.analysis = analysis
        self.review_count = review_count
        self.correct_count = correct_count
        self.accuracy_rating = accuracy_rating


