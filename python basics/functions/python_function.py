def prime_function(fucn_lower, func_upper):
    lower = fucn_lower
    upper = func_upper
    print("Prime numbers between",lower,"and",upper,"are:")
    for num in range(lower,upper + 1):
        if num > 1:
            for i in range(2,num):
            #print(num)
                if (num % i) == 0:
                #print(i)
                    break
                else:
                    print(num)
                    break

            
prime_function(1,10)
prime_function(700,900)
