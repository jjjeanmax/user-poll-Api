# user-poll-Api
API для системы опросов пользователей

>Django 2.2.10, Django REST framework.

##Функционал для администратора системы:

- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

##авторизация в системе (регистрация не нужна)
- Для доступа к методам API требуется Token(Basic)

## Старт

1. Создать и активировать виртуальное окружение:

    `python -m venv venv`

2. Установить пакеты:

    `pip install -r requirements.txt`

3. Выполнить команду для выполнения миграций :

    `python manage.py migrate`

4. Создать статичные файлы: 

    `python manage.py collectstatic`

5. Создать суперпользователя:

    `python manage.py createsuperuser`


7. Запустить сервер:

    `$ python manage.py runserver`

> Документация доступна в
   http://127.0.0.1:8000/redoc/