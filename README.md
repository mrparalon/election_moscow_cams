# Запись скриншотов камер наблюдения на московских выборах

## Требования
   - python 3.7 [веб-установщик](https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64-webinstall.exe) При установке надо поставить флажек `Add Phyton 3.7 to PATH`
   - Браузер Google Chrome [установка тут](https://www.google.ru/intl/ru/chrome)
   - Драйвер для браузера[установка тут](https://sites.google.com/a/chromium.org/chromedriver/downloads). 

## Установка драйвера браузера
   1. Скачиваем [тут](https://sites.google.com/a/chromium.org/chromedriver/downloads) Версия должна быть как [тут](chrome://version) с точность до первой точки.
   2. Распаковываем архив в C:\Windows\ (там всего один файл)

## Установка

1. Качаем все файлы из репозитория (зеленая кнопка Clone, надпись Download .zip)
2. Распаковываем архив в том месте на диске, где есть место для скриншотов.
3. Запускаем консоль. В Window это делается так - нажимаем клавиши Win+R, пишем `cmd`, нажимаем Enter.
4. В консоле переходим в папку с распакованными файлами из репозитория (команда в консоле `D:`, где D - буква диска. Далее `cd ПУТЬ_К_ПАПКЕ`, где путь к папке можно скопировать в окне с открытой папкой)
5. Далее в консоле команда:
`pip install -r requirements.txt`
6. Открываем файл stations.txt и записываем туда свой список номеров УИК, каждый номер на новой строке, пустых строк не должно быть. Сохраняем.


## Запуск
В консоль копируем команду:
`python run.py --stream_delay 2 --shots_delay 5`
  - stream_delay - задержка начала сохранения скриншотов после открытия видео в полный экран
  - shots_delay - задержка между кадрами
  - stations - путь к списку уиков. Текстовый файл с номерами уиков. Один номер уика на каждой строчке. Пример stations.txt


## Описание работы

Скрипт создаст нужные папки и откроет браузер. После загрузки страницы откроет видео в полный экран и сделает 3 скриншота с задержкой. Затем закроет видео, откроет новую страницу и дальше по кругу.

