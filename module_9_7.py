def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result != 1 and result != 2:
            diviser = 2
            is_prime = False
            for j in range (1, result):
                if (result%diviser == 0) and (diviser != result) :
                    is_prime = is_prime or True
                else:
                    is_prime = is_prime or False
                diviser += 1
            if is_prime == False:
                print('Простое')
            elif result != 1:
                print('Составное')
        elif result == 2:
            print('Простое')
        else:
            print('Ни простое и не сложное - просто 1') 
        return result
    return wrapper
            
@ is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

result = sum_three(0, 0, 1)
print(result)

result = sum_three(2, 2, 6)
print(result)