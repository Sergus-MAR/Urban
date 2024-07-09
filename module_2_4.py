numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
for i in range(0, len(numbers)):
    diviser = 2
    is_prime = False
    for j in range (1, numbers[i]):
        if numbers[i] == 2:
            primes.append(numbers[i])
        else:
            test_number_3 = numbers[i]
            if (numbers[i]%diviser == 0) and (diviser != numbers[i]) :
                test_number = numbers[i]
                test_number_2 = numbers[i]%diviser
                is_prime = is_prime or False
            else:
                is_prime = is_prime or True
            diviser += 1
    if is_prime == True:
        primes.append(numbers[i])
    elif numbers[i] != 1:
        not_primes.append(numbers[i])
print('not_primes ', not_primes)
print('primes ', primes)