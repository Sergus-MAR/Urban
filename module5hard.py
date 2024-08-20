import time # Импорт библиотеки Time 


class UrTube(): #Базовый класс

    
    def __init__(self):
        self.users = {}      #иннициализация словаря польвателей (dict)
        self.videos = {}     #иннициализация словаря видео (dict)
        self.current_user = None    #иннициализация текущего пользователя (string)  
    
        
    def add(self, *args):   #Добавление видео
        """
        добавление видео в систему видео хостинга
        args: входные данные о видео.
        Последовательность данных:
        1. Заголовок (string)
        2. Продолжительность секунд (int)
        3. Секунда остановки (по умолчанию 0) (int)
        4. Ограничение по возрасту (bool)
        """
            
        for add_video in args:  #распаковка массива полученных данных
            if self.videos.keys().__contains__(add_video.title):   #проверка уникальности ключа
                continue
            else:
                self.videos[add_video.title] = {'duration': add_video.duration,
                                                'time now': add_video.time_now,
                                                'adult mode': add_video.adult_mode}  #создание экземляра
    def get_videos(self, videos_string): #Поиск видео в базе данных
        """
        поиск видео по ключевому слову
        входной параметр - videos_string: клюевое слово
        возвращает список найденных видео
        """
        videos_list= []
        for title in self.videos.keys():
            if title.lower().__contains__(videos_string.lower()):
                videos_list.append(title)
            else:
                continue
        return videos_list

    def watch_video(self, title):
        """"
        просмотр видео
        """
        if self.current_user != None:             #  проверка на вход пользоваетеля
            if self.videos.__contains__(title):     # проверка наличия видео
                if self.videos[title]['adult mode'] == True and self.users[self.current_user]['age'] < 18:  #проверка на возврасное ограничение и возраст пользователя
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for sec in range(self.videos[title]['time now'], self.videos[title]['duration']+1, 1):
                        print (sec, end=" ")
                        time.sleep(1)
                    print ("Конец видео")
            else:
                print('Такого видео нет на UrTube')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


    def register_user(self, nickname, password, age):
        """
        регистрирует пользователя в системе и сохраняет его данные
        :param nickname: имя пользователя
        :param password: пароль пользователя в хешированном виде
        :param age:  возраст пользователя (
        :return:
        """
        if nickname not in self.users.keys():
            user = User(nickname, password, age)
            self.users[user.nickname] = {'password': user.password,
                                         'age': user.age}
            self.current_user = user.nickname
            print(f"Пользователь {nickname} зарегистрирован! \n , {nickname}")
        else:
            return print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        """
        Логин на хостинге
        входные параметры 
        1. nickname имя пользователя (string)
        2. password пароль пользователя (string)
        Возвращает текущего авторизированного пользователя, 
        либо предлагает провести авторизацию/регистрацию
        """
        print()
        if nickname in self.users.keys():   # проверка регистрации  пользователя
            if hash(password) == self.users[nickname]['password']:
                print(f"Приветствую на UrTube, {nickname}")
                self.current_user = nickname
                return self.current_user
            else:
                print("Введен неверный пароль")
        else:
            print("Указанный пользователь не обнаружен - выберите дальнейшие действия")
            choice = int (input("Для регистрации нажмите - 1,\nдля выхода - 2,\nОтвет: "))
            if isinstance(choice, int):
                match choice:
                    case 1:
                        user = User(nickname, password, int(input("Введите ваш возраст: ")))
                        self.register_user(user.nickname, user.password, user.age)
                        self.log_out()
                        self.current_user = user.nickname
                        return self.current_user
                    case 2:
                        self.log_out()
                    case _ :
                        print('Некорректный ввод. Попробуте в следующий раз')

    def log_out(self):
        """
        Выход из системы
        :return:
        """
        self.current_user = None
        return self.current_user


class User():   #Клас для обработки данных по пользователям
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video():  #Класс для работы с видео

     def __init__(self, title, duration, time_now = 0, adult_mode = False):
        if isinstance(title, str):
            self.title = title
        if isinstance(duration, int):
            self.duration = duration
        if isinstance(time_now, int):    
            self.time_now = time_now
        if isinstance(adult_mode, bool):
            self.adult_mode = adult_mode



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Лучший язык программирования 2024 года', 100)

    # Добавление видео
    ur.add(v1, v2, v3)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register_user('vasya_pupkin', 'lolkekcheburek',13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register_user('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')