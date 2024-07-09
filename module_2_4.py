numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers)):
    if numbers[i] != 1 and numbers[i] != 2:  
        diviser = 2
        is_prime = False
        for j in range (1, numbers[i]):
            if (numbers[i]%diviser == 0) and (diviser != numbers[i]) :
                is_prime = is_prime or True
            else:
                is_prime = is_prime or False
            diviser += 1
        if is_prime == False:
            primes.append(numbers[i])
        elif numbers[i] != 1:
            not_primes.append(numbers[i])    
    elif numbers[i] == 2:
        primes.append(numbers[i])
print('not_primes ', not_primes)
print('primes ', primes)
