# 知识点回顾系统 - 基础框架
# 这是一个简单的命令行程序，我们将逐步完善它
import random
from data.data import load_questions

def main_menu():
    """显示主菜单"""
    print("\n===== 知识点回顾系统 =====")
    print("1. 开始测试")
    print("2. 添加题目")
    print("3. 查看题目列表")
    print("4. 学习统计")
    print("5. 退出")
    #题目加载
    question = load_questions("./data/questions.json")
    print(question)
    # 获取用户选择
    choice = input("请选择功能(1-5): ")
    return choice
#根据用户的选择选择具体功能
def choice(choice):
    actions = {
        1: start_testing,
        2: add_prombles,
        3: view,
        4: Study_statistics,
        5: project_exit,
        6: user_input_answer
    }
    return actions.get(int(choice))
# 根据用户的选择执行具体功能

#定义具体功能
#1. 开始测试"
def start_testing(questions ,test_number = 1 ):#questions是题目列表,这里最好是做成列表，方便读取，test_number是测试次数
    #首先检查题目列表是否为空
    if (not questions) and test_number > len(questions):
        print("题目列表不够，请先添加题目。")
        return
    #如果题目列表不为空，开始测试。取随机个题目进行测试，需要随机个测试次数的一个可迭代对象
    # 生成可迭代对象，值在题目索引范围内，不允许重复
    indices = random.sample(range(len(questions)), k=test_number)
    print("本次测试题目索引：", indices)
    # 可以用 indices 来遍历题目
    for idx in indices:
        user_one = questions[idx]#用户需要回答的题目之一
        print(f"题目：{user_one.question}")
        for i, opt in enumerate(user_one.options):
            print(f"{i+1}. {opt}")
        #接受用户输入答案
        answer = user_input_answer()
        # 检查答案是否正确，并且更新题目统计信息
        is_correct = (answer == user_one.answer)
        Study_statistics(user_one, is_correct)
        if is_correct:
            print("回答正确！")
        else:
            print(f"回答错误，正确答案是: {user_one.options[user_one.answer]}")



#2. 添加题目    
def add_prombles(questions , new_question=None):
    questions.append(new_question)


# 3. 查看题目列表  
def view():
    print("开始测试功能待实现...")

# 4. 学习统计
def Study_statistics(questions,is_correct):
    # 更新下面三个参数self.review_count self.correct_count self.accuracy_rating
    questions.review_count += 1
    questions.correct_count += 1
    questions.accuracy_rating = questions.correct_count / questions.review_count



# 5. 退出
def project_exit():
    print("退出功能待实现...")
#6 用户输入答案
def user_input_answer():
    answer = input("请输入你的答案(选项编号): ")
    return int(answer) - 1  # 返回用户选择的索引



if __name__ == "__main__":
    # 程序主循环
    while True:
        # 显示菜单并获取选择
        user_choice = main_menu()
        
        # 执行选择的功能
        choice(user_choice)