def count_calls(count_or_print=True):
    '''функция подсчета вызовов'''
    global calls
    if count_or_print:
        print(calls)
    else:
        calls += 1

def string_info(string: str):
    '''функция обработки строк'''
    count_calls(False)
    string = (len(string)), string.upper(), string.lower()
    return (string)

def is_contains(string:str, list_to_search:list):
    '''функция поиска искомого в списке'''
    count_calls(False)
    string = string.lower()
    result = False
    for i in range (len(list_to_search)):
        if list_to_search[i].lower() == string:
            result = result or True
    return (result)


calls = 0
print(string_info('Leopard'))
print(string_info('manchester'))
print(is_contains('Town', ['tank', 'teacher', 'toWN'])) # Urban ~ urBAN
print(is_contains('cinema', ['cream', 'cyclic'])) # No matches
print(calls)