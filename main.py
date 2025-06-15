# 知识点回顾系统 - 基础框架
# 这是一个简单的命令行程序，我们将逐步完善它

def main_menu():
    """显示主菜单"""
    print("\n===== 知识点回顾系统 =====")
    print("1. 开始测试")
    print("2. 添加题目")
    print("3. 查看题目列表")
    print("4. 学习统计")
    print("5. 退出")
    
    # 获取用户选择
    choice = input("请选择功能(1-5): ")
    return choice

#定义具体功能
#1. 开始测试"
def start_testing():
    print("开始测试功能待实现...")

#2. 添加题目    
def add_prombles():
    print("增加题目功能待实现...")

# 3. 查看题目列表  
def view():
    print("开始测试功能待实现...")

# 4. 学习统计
def Study_statistics():
    print("学习统计功能待实现...")

# 5. 退出
def project_exit():
    print("退出功能待实现...")

#根据用户的选择选择具体功能
def choice(choice):
     actions = {
        1: start_testing,
        2: add_prombles,
        3: view,
        4: Study_statistics,
        5: project_exit
    }
    return actions.get(int(choice) , default_action )
# 根据用户的选择执行具体功能

if __name__ == "__main__":
    # 程序主循环
    while True:
        # 显示菜单并获取选择
        user_choice = main_menu()
        
        # 执行选择的功能
        choice(user_choice)