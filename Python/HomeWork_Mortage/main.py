print("Задача №1")

regions = [
  "Республика Бурятия",
  "Республика Саха",
  "Забалькайский край",
  "Камчатский край",
  "Приморский край",
  "Хабаровский край",
  "Амурская обрасть",
  "Магаданская область",
  "Сахалинская область",
  "Еврейская автономная область",
  "Чукотский автономный округ"
]

key_rate = 8
far_east_key_rate = 2

print("Добро пожаловать в наш банк! Для расчета Вашей \
ипотечной ставки просим ответить на некоторые наши вопросы.")
print("")

region = input("В каком регионе Вы проживаете: ")
children = int(input("Сколько у Вас детей: "))
salary_project = input("Есть ли у Вас зарплатный проект в \
нашем банке (Да/Нет): ")
insurance = input("Хотели бы Вы оформить Страхование в \
нашем банке (Да/Нет): ")
print("")

discount_children = 1
discount_salary_project = 0.5
discount_insurance = 1.5


if region in regions:
  if insurance == "Да":
    rate = far_east_key_rate - discount_insurance
    print(f"Ваша ипотечная ставка составит {rate}%")
  elif children >= 3:
    if salary_project == "Да":
      rate = far_east_key_rate - discount_children - discount_salary_project
      print(f"Ваша ипотечная ставка составит {rate}%")
    else:
      rate = far_east_key_rate - discount_children
      print(f"Ваша ипотечная ставка составит {rate}%")
  elif children < 3:
    if salary_project == "Да":
      rate = far_east_key_rate - discount_salary_project
      print(f"Ваша ипотечная ставка составит {rate}%")
    else:
      rate = far_east_key_rate
      print(f"Ваша ипотечная ставка составит {rate}%")
else:
  if insurance == "Да":
    if children >= 3:
      if salary_project == "Да":
        rate = key_rate - discount_children - discount_insurance - discount_salary_project
        print(f"Ваша ипотечная ставка составит {rate}%")
      else:
        rate = key_rate - discount_children - discount_insurance
        print(f"Ваша ипотечная ставка составит {rate}%")
    else:
      if salary_project == "Да":
        rate = key_rate - discount_insurance - discount_salary_project
        print(f"Ваша ипотечная ставка составит {rate}%")
      else:
        rate = key_rate - discount_insurance
        print(f"Ваша ипотечная ставка составит {rate}%")
  else:
    if children >= 3:
      if salary_project == "Да":
        rate = key_rate - discount_children - discount_salary_project
        print(f"Ваша ипотечная ставка составит {rate}%")
      else:
        rate = key_rate - discount_children
        print(f"Ваша ипотечная ставка составит {rate}%")
    else:
      if salary_project == "Да":
        rate = key_rate - discount_salary_project
        print(f"Ваша ипотечная ставка составит {rate}%")
      else:
        rate = key_rate
        print(f"Ваша ипотечная ставка составит {rate}%")