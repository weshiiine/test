import re
from difflib import get_close_matches

def read_file(file_path):
    """读取文件内容并返回为字符串。"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def find_word(text, word):
    """在文本中查找单词的所有出现位置并返回其位置列表。"""
    lower_text = text.lower()
    lower_word = word.lower()

    # 使用正则表达式查找完整单词的所有匹配项，并记录每个匹配项的起始位置和匹配的内容
    matches = [(m.start(), m.group()) for m in re.finditer(r'\b' + lower_word + r'\b', lower_text)]
    
    # 计算每个匹配项在文本中的位置，位置是从文本的开始到匹配项的空格数加1
    positions = [lower_text.count(' ', 0, pos) + 1 for pos, _ in matches]
    
    return positions  # 返回所有匹配项的位置列表

def build_dictionary(text):
    """从文本中创建唯一单词的列表。"""
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)  # 使用集合去重，得到唯一的单词
    return list(unique_words)  # 将集合转换为列表并返回

def suggest_similar_word(input_word, dictionary):
    """根据模糊匹配从字典中建议相似的单词。"""
    close_matches = get_close_matches(input_word, dictionary, n=1, cutoff=0.6)  # 获取与输入单词相似的单词，返回最接近的一个
    return close_matches[0] if close_matches else None  # 如果有相似单词，则返回第一个；否则返回None

def main():
    file_path = 'test.txt'
    text = read_file(file_path)
    
    # 从文本中构建唯一单词的字典
    dictionary = build_dictionary(text)

    while True:
        input_word = input("请输入要匹配的单词：").strip()
        if not input_word or not re.match(r'^\w+$', input_word):
            print("无效输入，请输入一个有效的单词。")
            continue
        positions = find_word(text, input_word)
        break
    
    if positions:
        print(f"单词 '{input_word}' 出现了 {len(positions)} 次。位置：")
        for pos in positions:
            print(f"位置: {pos}")
    else:
        print(f"未找到单词 '{input_word}'。")
        suggestion = suggest_similar_word(input_word, dictionary)  # 从字典中建议一个相似的单词
        if suggestion:
            print(f"您是否想要匹配 '{suggestion}'？")
        else:
            print("没有找到相似的单词建议。")

if __name__ == '__main__':
    main()
