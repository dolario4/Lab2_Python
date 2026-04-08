def filter_text(func, text):
    result = []
    for i in text:
        if func(i):
            result.append(i)
    return func(text)
space = lambda a: [i for i in a if " " not in i]
a_deletion = lambda a: [i for i in a if i[0] != "а" and i[0] != "А"]
length_deletion = lambda a: [i for i in a if len(i) >= 5]
text = ["рвал дед лавр", "Hello_World!", 'Абоба',"Прив"]

print('Исключение строк с пробелами :\n',filter_text(space, text))
print('Исключение строк, начинающихся с "а" или "А" :\n',filter_text(a_deletion, text))
print('Исключение строк, длина которых меньше 5 :\n',filter_text(length_deletion, text))

