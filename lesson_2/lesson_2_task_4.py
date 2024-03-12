def fizz_buzz(n): 
	# объявляем список для хранения результатов 
	result = [] 

	# Цикл от 1 до n (включительно) 
	for i in range(1, n + 1): 

		# Проверяем, делится ли i как на 3, так и на 5 
		if i % 3 == 0 and i % 5 == 0: 

			# если да то пишет FizzBuzz
			result.append("FizzBuzz") 

		# Проверяем, делится ли i на 3 
		elif i % 3 == 0: 

			# если да то пишет Fizz
			result.append("Fizz") 

		# Проверяем, делится ли i на 5 
		elif i % 5 == 0: 

			# если да то пишет Buzz 
			result.append("Buzz") 
		else: 

			# Добавляем текущий номер в виде строки в список результатов 
 
			result.append(str(i)) 

	# Возвращаем список результатов 
	return result 


# вводим число 
n = 35

# Вызываем функцию fizz_buzz, чтобы получить результат 
result = fizz_buzz(n) 

# Вывод результат на печать 
print(' '.join(result)) 
