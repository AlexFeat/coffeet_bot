FROM python:3.9-buster

# объявляем рабочую директорию
WORKDIR /var/app

# устанавливаем зависимости проекта
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# копирование кода проекта в докер
COPY app .

#регламентируем порт
EXPOSE 8000