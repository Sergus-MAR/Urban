def all_variants(text):
    i = 0
    symbols = len(text) 
    while i != symbols:
        j = 0
        while j != (symbols - i):
            yield text[j:i+j+1]
            j += 1
        i += 1

a = all_variants("abc")
for i in a:
    print(i)