def month_to_season(month):
    season_ranges = {
    (12, 1, 2): 'Зима', # Создание словаря для хранения информации о сезонах
    (3, 4, 5): 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень'
  }
    season = None # Создание переменной для возвращаемого значения функции
    for key, value in season_ranges.items(): # Цикл, в котором по очереди перебираются пары ключ-значение(номера месяцев - сезон) из словаря
       if month in key: # Если значение входного параметра(номер месяца) входит в состав ключа(пример ключа - (3, 4, 5))
         season = value # То присваиваем возвращаемой переменной season название сезона
         break # Останавливаем цикл
    return season # Возвращаем название сезона
print(month_to_season(1)) # Проверяем работу функции
print(month_to_season(5)) # Проверяем работу функции