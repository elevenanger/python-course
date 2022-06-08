def word_count(file_name):
    try:
        with open(file_name) as file_obj:
            content = file_obj.read();
    except FileNotFoundError:
        # 静默失败 Python 中的 pass 关键字表示什么都不做
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"{file_name} 有 {num_words} 个词")
        return num_words


file = 'word_count.py'
word_count(file)
