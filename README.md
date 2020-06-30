# Запись скриншотов камер наблюдения на московских выборах

## Требования
    - python 3.7
    - [chrome web driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## Установка

`pip install -r requirements.txt`

Скачать chrome driver и добавить его в PATH

[Инструкция по установку selenium](https://selenium-python.readthedocs.io/installation.html)


## Запуск

`python run.py --stream_delay 2 --shots_delay 5`
    - stream_delay - задержка начала сохранения скриншотов после открытия видео в полный экран
    - shots_delay - задержка между кадрами
    - stations - путь к списку уиков. Текстовый файл с номерами уиков. Один номер уика на каждой строчке. Пример stations.txt


## Описание работы

Скрипт создаст нужные папки и откроет браузер. После загрузки страницы откроет видео в полный экран и сделает 3 скриншота с задержкой. Затем закроет видео, откроет новую страницу и дальше по кругу.

