class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        '''Метод возвращает словарь с указанием имени файла и слов, включенных в него без спец.символов'''
        out_set_symbol = {ord(','): '',
                          ord('.'): '',
                          ord('='): '',
                          ord('!'): '',
                          ord('?'): '',
                          ord(';'): '',
                          ord(':'): '',
                          }
        all_words={}
        for element in self.file_names:
            split = []
            with open(element) as file:
                for line in file:
                    split = split + (((line.lower().translate(out_set_symbol)).replace(' - ',' ')).split())
                    #print(split)
            all_words[element] = split
        return all_words

    def find(self, word):
        word = word.lower()
        resault_find = {}
        for name, words in self.get_all_words().items():
            counter = 1
            for element in words:
                if element == word:
                    resault_find[name] = counter
                    break
                else:
                    resault_find[name] = 'Отсутствует'
                    counter+=1
        return resault_find
        pass

    def count(self, word):
        word = word.lower()
        resault_count = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for element in words:
                if element == word:
                    counter += 1
            resault_count[name] = counter
        return resault_count

finder2 = WordsFinder('test_file.txt')
print(finder2.__dict__)
print(finder2.get_all_words()) #Все слова
print(finder2.find('TEXT')) #3 слово по счету
print(finder2.count('teXT')) #4 слова teXT в тексте всего
