def brackets_matched(expression):
    stack = []  # 用于存储未匹配的开括号
    i = 0  # 当前字符索引
    length = len(expression)

    while i < length:
        char = expression[i]  # 读取当前字符

        # 处理单行注释 (//)
        if char == '/' and i + 1 < length and expression[i + 1] == '/':
            i += 2  # 跳过'//'
            while i < length and expression[i] != '\n':
                i += 1  # 跳过注释内容
        # 处理多行注释 (/* ... */)
        elif char == '/' and i + 1 < length and expression[i + 1] == '*':
            i += 2  # 跳过'/*'
            while i < length - 1 and not (expression[i] == '*' and expression[i + 1] == '/'):
                i += 1  # 跳过注释内容
            i += 2  # 跳过'*/'
        # 处理开括号
        elif char in '([{':
            stack.append(char)  # 将开括号压入栈
        # 处理闭括号
        elif char in ')]}':
            if not stack:  # 如果栈为空，表示没有匹配的开括号
                return False
            top = stack.pop()  # 弹出栈顶的开括号
            # 检查弹出的开括号是否与当前闭括号匹配
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False 
        i += 1  # 移动到下一个字符
    return len(stack) == 0  # 如果栈为空，所有括号都匹配，返回 True


def find_matching_bracket(expression, position):
    stack = []  # 用于存储未匹配的开括号及其位置
    pairs = {}  # 存储匹配括号的位置对
    i = 0  # 当前字符索引
    length = len(expression)  # 表达式的长度

    while i < length:
        char = expression[i]  # 读取当前字符
        # 处理单行注释
        if char == '/' and i + 1 < length and expression[i + 1] == '/':
            i += 2
            while i < length and expression[i] != '\n':
                i += 1  # 跳过注释内容
        # 处理多行注释
        elif char == '/' and i + 1 < length and expression[i + 1] == '*':
            i += 2
            while i < length - 1 and not (expression[i] == '*' and expression[i + 1] == '/'):
                i += 1  # 跳过注释内容
            i += 2  # 跳过'*/'
        # 处理开括号
        elif char in '([{':
            stack.append((char, i))  # 将开括号及其位置压入栈
        # 处理闭括号
        elif char in ')]}':
            if not stack:  # 如果栈为空，表示没有匹配的开括号
                return None
            top, top_pos = stack.pop()  # 弹出栈顶的开括号及其位置
            # 检查弹出的开括号是否与当前闭括号匹配
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return None  # 如果不匹配，则返回 None
            pairs[top_pos] = i  # 记录开括号和闭括号的匹配位置
            pairs[i] = top_pos
        i += 1  # 移动到下一个字符

    if position in pairs:  # 检查给定位置是否在匹配对中
        return pairs[position]  # 返回匹配的括号位置
    else:
        return None  # 如果没有匹配，返回 None


# 主程序
expression = input("请输入表达式: ")  # 用户输入表达式
is_matched = brackets_matched(expression)  # 检查括号是否匹配
if is_matched:
    print("括号匹配。")
    position = int(input("请输入要查找匹配的括号位置: ")) - 1  # 用户输入要查找的括号位置
    matching_position = find_matching_bracket(expression, position) + 1
    if matching_position is not None:
        print(f"位置 {position + 1} 的括号与位置 {matching_position} 的括号匹配。")
    else:
        print(f"位置 {position + 1} 的括号没有匹配的括号。")
else:
    print("括号不匹配。")



# (a+b)*(c-[d/e])+{f*(g-h)}

# (/* comment */ [a + /* another comment */ {b + c}])

# (a + b * (c - d

# [(a + b) * (c - d})]

