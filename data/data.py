import os
import json
from main.question import Question

#加载json里面的题目数据构建好对象
def load_questions(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # 处理JSON键名与类属性名的映射
        questions = []
        for q_data in data:
            questions.append(Question(** q_data))
        return questions #返回题目对象

def save_questions(questions, path):#这里的题目对象是所有题目的对象
    with open(path, 'w', encoding='utf-8') as file:
        # 通过__ dict __方法将对象转换为字典,然后使用json.dump保存
        json.dump([q.__dict__ for q in questions], file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    '''    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建questions.json的绝对路径
    path = os.path.join(script_dir, 'questions.json')
    questions = load_questions(path)
    print(f"成功加载 {len(questions)} 个题目\n")
    for i, q in enumerate(questions, 1):
        print(f"题目 {i}: {q.question}")
        print(f"类别: {q.category}")
        print(f"正确答案: {q.options[q.answer]}\n")'''
    # 测试保存功能
    #构建一个测试题目
    test_question = Question(
        id=2,
        question="测试题目",
        options=["选项A", "选项B", "选项C", "选项D"],
        answer=0,
        review_count=5,
        correct_count=3,
        accuracy_rating=0.6,
        analysis="这是一个测试题目的分析"
    )
    save_questions([test_question] , 'test_questions.json')


