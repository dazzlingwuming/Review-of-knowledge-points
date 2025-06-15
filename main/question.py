#定义题目类
class Question(object):
    def __init__(self, id = None, question = None,options = None,answer = None,category = None,last_reviewed = None ,review_count = None ,correct_count = None,accuracy_rating = None,analysis = None):
        self.id = id
        self.question = question
        self.options = options
        self.answer = answer
        self.category = category
        self.last_reviewed = last_reviewed
        self.review_count = review_count
        self.correct_count = correct_count
        self.accuracy_rating = accuracy_rating
        self.analysis = analysis

