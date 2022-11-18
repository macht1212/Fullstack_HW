print("Задача №1\n")

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

print("Исходный список:\n")
for i, el in enumerate(geo_logs):
    print(geo_logs[i])

new_geo_logs = {}
new_dict_geo_logs = []

for i, el in enumerate(geo_logs):
    geo_logs[0].update(geo_logs[i])

for key in geo_logs[0]:
    var = geo_logs[0][key]
    if var[1] == "Россия":
        new_geo_logs[key] = var

for key, var in new_geo_logs.items():
    new_dict_geo_logs.append({key: var})

print("")
print("Отсортированный по посещениям России:\n")
for i, el in enumerate(new_dict_geo_logs):
    print(new_dict_geo_logs[i])
