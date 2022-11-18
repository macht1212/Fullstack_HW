print("Задача №2\n")

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_arr = []

for i, el in enumerate(list(ids.values())):
    ids_arr += list(ids.values())[i]

ids_arr = list(set(ids_arr))
print(sorted(ids_arr))
