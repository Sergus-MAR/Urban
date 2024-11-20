#простой парсер для поиска изображений на веб странице с выводом первого найденного и удовлетворяющего размеру,
#изображения с последующим изменением размера изображения. Сохраняет исходный и измененный файлы.
from urllib.parse import urlparse #Библиотека для получения информации о доменном имени в URL
import requests #Библиотека для работы с HTTP-запросами
import subprocess #Библиотека для запучка внешних процессов из Python
from bs4 import BeautifulSoup #Библиотека для парсинга информации
from PIL import Image #Библиотека для работы с изображениями
from io import BytesIO #Библиотек, которая позволяет работать с двоичными данными в памяти


def site_getting(url):
    getting = requests.get(site_url, timeout=5)
    return getting
def url_answer(site_url:str):
    '''Функция - обработчик ошибок web-страницы'''
    try:
        answer = site_getting(site_url) # отправляем запрос странице и ждем ответа в течении 5 сек
        match answer.status_code:
            case 200:
                print('Сеть присутствует. Начинаем поиск')
                return True
            case 400:
                print('Некорректный запрос (адрес). Невозможно работать с данной ссылкой')
                return False
            case 401:
                print('Unauthorized. Невозможно работать с данной ссылкой')
                return False
            case 403:
                print('Forbidden. Невозможно работать с данной ссылкой')
                return False
            case 404:
                print('Not Found. Невозможно работать с данной ссылкой')
                return False
            case _:
                print('Ошибка открытия страниц. Невозможно работать с данной ссылкой')
                return False
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
        print("Timed out!!! Сайт недоступен!!! Некорректная ссылка!!!")
        return False


def net_test(url:str):
    '''Функция для проверки доступности домена URL. Принимает URL, выделяет доменное имя и возвращает True,
    если доменное имя доступно (проверка производится ICMP (ping)'''
    domain = urlparse(url).netloc #Извлечение доменного имени из URl
    network_is_ok = False #Присваиваем промежуточной переменной временное значение
    while not network_is_ok:
        try:
            subprocess.run(["ping", "-c 1", domain], stdout=subprocess.DEVNULL, encoding='utf-8') #вызов внешнего процесса ping
            #Проверяем доступность домена (применяем экранирование вывода результата ping  - .DEVNULL)
            return True
        except subprocess.CalledProcessError:
            print("Internet is still down, or incorrect URL :(")
            #return False

def find_need_image(width, height, find_list):
    '''Функция поиска изображения'''
    pozition = 0
    for element in find_list:
        response = site_getting(element)  # отправляем get-запрос
        img_data = response.content #получение ответа сервера
        image = Image.open(BytesIO(img_data)) #чтение данных изображения
        x, y = image.size #получение данных о размере изображения
        if x >= width and y >= height:
            return True, pozition
        else:
            pozition += 1
    return False, None

def site_scan_image(web_page, width = 640, height = 480, new_size = 100):
    '''функция парсинга и последующей обработки изображения '''
    if url_answer(web_page) and net_test(web_page):
        web_site = site_getting(web_page) #отправляем get-запрос
        soup = BeautifulSoup(web_site.text, "html.parser") #парсинг страницы
        images = soup.find_all('img') #поиск всех изображений на странице
        all_site_image = []
        for image in images:
            str_image = str(image)
            start = str_image.find('https')
            if str_image.find('.jpeg') >= 0:
                end = str_image.find('.jpeg') + 5
            elif str_image.find('.jpg') >= 0:
                end = str_image.find('.jpg') + 4
            else:
                continue
            image_url = str_image[start:end]
            if image_url:
                all_site_image.append(image_url)
        unique_image_list = list(set(all_site_image))
        logic, find_index = find_need_image(width, height, unique_image_list)
        if logic:
            response = site_getting(unique_image_list[find_index])  #отправляем get-запрос
            with open('original_image.jpeg', 'wb') as file:  #открытие файла
                file.write(response.content) #запись файла
            image_path = './original_image.jpeg'  # указываем путь картинки - текущая директория
            img = Image.open(image_path)
            x = int(img.width * new_size / 100) #создаем переменную с требуемым размером, согласно запроса
            y = int(img.height * new_size / 100) #создаем переменную с требуемым размером, согласно запроса
            new_size = (x, y)
            new_image = img.resize(new_size)  # меняем размер
            new_image.save('new_image.jpeg')
            print('Запрос выполнен')
            print(f'Начальный размер изображения: ({img.width}, {img.height}) - новый размер: {new_image.size}')
        else:
            print('Файл, удовлетворяющий Вашим критериям, не обнаружен')
    else:
        print('Поиск невозможен')
        print('Остановка программы из-за проблем с сетью или недоступностью сайта')

min_width = 50 #минимальный размер изображения для поиска
min_height = 50 #минимальный размер изображения для поиска
new_size_proc = 50 #величина изменения размера изображения от текущего (в процентах)
test_page = ('https://tproger.ru/articles/python-pandas')
#test_page = 'https://ru.wallpaper.mob.org/pc/gallery/tag=oshki_oty_otiki/'
site_scan_image(test_page, min_width, min_height, new_size_proc)