import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def find_word(text, word):
    lower_text = text.lower()
    lower_word = word.lower()
    
    matches = [(m.start(), m.group()) for m in re.finditer(r'\b' + re.escape(lower_word) + r'\b', lower_text)]
    
    positions = [lower_text.count(' ', 0, pos) + 1 for pos, _ in matches]
    
    return positions

def suggest_similar_word(input_word, dictionary):
    for word in dictionary:
        if input_word.lower() in word.lower():
            return word
    return None

def main():
    file_path = 'test.txt'
    text = read_file(file_path)
    
    input_word = input("请输入要匹配的单词：")
    positions = find_word(text, input_word)
    
    if positions:
        print(f"单词 '{input_word}' 出现了 {len(positions)} 次。位置：")
        for pos in positions:
            print(f"位置: {pos}")
    else:
        print(f"未找到单词 '{input_word}'。")
        dictionary = ['security', 'information', 'computer', 'assurance']
        suggestion = suggest_similar_word(input_word, dictionary)
        if suggestion:
            print(f"您是否想要匹配 '{suggestion}'？")
        else:
            print("没有找到相似的单词建议。")

if __name__ == '__main__':
    main()
