def int_funk(*args):
    #arg - строка из слов через пробел
    for el in args:
        result = el.title()
    return result

print(int_funk("я работаю в питоне"))