import string


def read(file):
    try:
        with open(file, 'r') as fileR:
            content = fileR.read()
            return content
    except FileNotFoundError:
        print("Файл не найден")
        return ""
    except PermissionError:
        print("Файл не открывается")
        return ""
    except ValueError:
        print("Файл пустой")
        return ""


def task(text):
    words = text.split()
    word_count = len(words)
    symbol_count = len(text)
    word_dict = {}
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        else:
            word_count -= 1
    if word_count > 0:
        frequent_word = max(word_dict, key=word_dict.get)
    else:
        frequent_word = ""
        word_count = 0
    return frequent_word, word_count, symbol_count


file = input("Название файла: ")
if read(file) != "":
    most_frequent_word, word_count, char_count = task(read(file))
    print(f"Самое популярное слово: {most_frequent_word}\nКоличество слов: {word_count}\nКоличество символов: {char_count}")
