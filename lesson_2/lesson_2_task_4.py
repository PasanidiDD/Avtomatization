for num in range(17): 
    # если число делится на 3 и на 5, печатать FizzBuzz
    if num % 15 == 0: 
        print(" FizzBuzz ")                                         
        continue 
    # если число делится на 3, печатать Fizz 
    elif num % 3 == 0:     
        print(" Fizz")                                         
        continue 
    # если число делится на 5, печатать Buzz 
    elif num % 5 == 0:         
        print(" Buzz ")                                     
        continue  
    # в результате он выведет цифры 
    print(num) 