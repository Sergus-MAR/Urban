class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self._is_valid_vin(vin):
            self._vin = vin
        if self._is_valid_numbers(numbers):
            self._numbers = numbers

    @staticmethod 
    def _is_valid_vin(vin_number): # Валидация VIN без привязки к объекту (декоратор staticmethod) 
        if isinstance(vin_number, int) and (1000000 <= vin_number <= 9999999):
            return True
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            raise IncorrectVinNumber("Неверный тип vin номер")

    @staticmethod
    def _is_valid_numbers(numbers): #Валидация номера без привязки к объекту (декоратор staticmethod)
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

