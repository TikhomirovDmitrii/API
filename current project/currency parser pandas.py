import requests
import xml.etree.ElementTree as ET

# URL для получения курсов валют
url = 'https://www.cbr.ru/scripts/XML_daily.asp'

# Выполняем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Парсим XML-ответ
    root = ET.fromstring(response.content)

    # Итерируемся по элементам Valute
    for valute in root.findall('Valute'):
        # Получаем код валюты
        char_code = valute.find('CharCode').text
        # Получаем значение курса
        value = valute.find('Value').text
        # Получаем номинал
        nominal = valute.find('Nominal').text

        # Выводим информацию о валюте
        print(f'Код валюты: {char_code}, Курс: {value}, Номинал: {nominal}')
else:
    print(f'Ошибка при выполнении запроса: {response.status_code}')
