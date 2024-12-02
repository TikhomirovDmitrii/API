import requests
import pandas as pd
from io import StringIO

# URL для получения курсов валют
url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/12/2024'

# Выполняем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Декодируем ответ в кодировке Windows-1251
    content = response.content.decode('windows-1251')

    # Используем StringIO для передачи строки в read_xml
    xml_data = StringIO(content)

    # Парсим XML-ответ
    root = pd.read_xml(xml_data, encoding='windows-1251')

    # Выбираем только нужные столбцы
    df = root[['CharCode', 'Nominal', 'Name', 'Value']]

    # Выводим данные
    print(df)
else:
    print(f'Ошибка при выполнении запроса: {response.status_code}')