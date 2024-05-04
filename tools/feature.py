import re

def read_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "文件未找到"
    except Exception as e:
        return f"读取文件出错: {e}"


def read_rules(rules_file_path):
    """读取规则库文件，每个规则由一行正则表达式和一行对应数据组成"""
    rules = []
    try:
        with open(rules_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i in range(0, len(lines), 2):
            pattern = lines[i].strip()  # 正则表达式
            data = lines[i + 1].strip()  # 对应的数据
            rules.append((pattern, data))

        return rules
    except FileNotFoundError:
        return "规则文件未找到"
    except Exception as e:
        return f"读取规则文件出错: {e}"


def apply_rules_to_file(rules_file_path, target_file_path):
    """将规则应用到指定文件内容上"""
    rules = read_rules(rules_file_path)
    if isinstance(rules, str):  # 如果是错误消息，直接打印
        print(rules)
        return

    file_content = read_file_content(target_file_path)
    if isinstance(file_content, str) and file_content.startswith("错误"):
        print(file_content)
        return

    matched = False  # 是否有匹配的标志
    for pattern, data in rules:
        if re.search(pattern, file_content):
            # 发现匹配的模式时的操作
            print(f"[INFO]{data}")
            matched = True

    if not matched:
        print("未检测到任何匹配的规则，跳过检测。")


def feature():
    """主功能函数，交互式读取用户输入的文件路径"""
    rules_path = 'rule.txt'
    target_file_path = input('输入要扫描的文件路径:-->')
    apply_rules_to_file(rules_path, target_file_path)
