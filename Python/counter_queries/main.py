queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

queries_new = []
queries_count = []

for i, el in enumerate(queries):
    queries[i] = queries[i].split()
    queries_new.append(queries[i])

for i, el in enumerate(queries_new):
    queries_new[i] = len(queries_new[i])
    queries_count.append(queries_new[i])

new_set = list(set(queries_count.copy()))

for i, el in enumerate(new_set):
    count = queries_count.count(new_set[i])
    percent = round(count / len(queries_new) * 100, 2)
    print(f'Поисковых запросов из {new_set[i]} слов составляет {percent}%')