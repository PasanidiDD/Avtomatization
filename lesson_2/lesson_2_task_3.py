import math
s=float(input("Enter side of square: ")) # Принимаем ввод стороны от пользователя
area=s*s #  Вычислеяем площадь
print("Area of square=",math.ceil(area)) # Выводим область с помощью "%.1f",для получения 1 цифры после запятой, а f указывает значение с плавающей точкой.