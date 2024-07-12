def set_password(password_pair: int):
    '''Подбор кодового слова'''
    
    if password_pair < 3 or password_pair > 20:
        print('Your first pair ', password_pair, ' is not correct')
    else:    
        for i in range(1, password_pair):
            for j in range(1, password_pair):
                if password_pair % (i + j) == 0 and i != j and i < j:
                    print(i, j, sep='', end='')


first_pair = int(input('Input first pair - '))
set_password(first_pair)