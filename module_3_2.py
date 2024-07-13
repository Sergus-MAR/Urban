def send_email(message, recipient, sender="university.help@gmail.com"):
    '''функция отправки сообщения'''
    default_sender = "university.help@gmail.com"
    if (test_mail_address(recipient) and test_mail_address(sender)) == False:
        print('Невозможно отправить посьмо с адреса ',sender, ' на адрес ', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')
    elif default_sender != sender:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ',sender, ' на адрес ', recipient)
    elif recipient != sender and sender == default_sender:
        print('Письмо успешно отправлено с адреса ',sender, ' на адрес ', recipient)
     
def test_mail_address(mail):
    '''проверка корректности адреса электронной почты'''

    resault = False
    mail_server = ('.com', '.ru', '.net')
    if mail.find('@') > 0:
        email_list = [mail[0: mail.index('@')], mail[mail.index('@')], mail[mail.index('@') + 1: len(mail)]]
        for i in range(len(mail_server)):
            if email_list[2].find(mail_server[i]) > 0:
                resault = resault + True
    else:
        resault = False
    return resault


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, тсправьте задание', 'urban.student@mail.ru', sender ='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')




