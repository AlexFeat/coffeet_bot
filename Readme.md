# Coffeet Study Project

Time To Coffeet!!

## How to run

Run

````
% docker-compose up -d --build
% docker-compose exec app sh -c 'alembic upgrade head'
````

and go to http://0.0.0.0:8000/

## About

Проект по организации встреч коллег по средствам телеграмм.
Поддерживается ряд команд:
* /help - подсказки по командам
* /me - информация о себе
* /meet_request_add - создать заявку
* /meet_request_list - список активных заявок
* /cancel - отмена заполнения формы

Все данные проходят через бекенда на FastAPI и сохраняюся в БД Postgresql.

## TODO
* Доработать логику создания встреч по указанным заявкам
* Добавить больше данных для пользователя, для повышения качества проводимых встреч
* Добавить админку (возможно https://github.com/fastapi-admin/fastapi-admin)
