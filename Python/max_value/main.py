stats = {
  'facebook': 55, 
  'yandex': 120, 
  'vk': 115, 
  'google': 99, 
  'email': 42, 
  'ok': 98
}


max_value = max(stats.values())
print(list(stats.keys())[list(stats.values()).index(max_value)])