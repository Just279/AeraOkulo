FROM python:latest

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0

WORKDIR /app

# Копирование проекта в контейнер
COPY . /app

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 80
EXPOSE 80

# Скрипт для выполнения команд перед запуском сервера
RUN echo '#!/bin/bash\n\
python manage.py makemigrations\n\
python manage.py migrate\n\
python manage.py runserver 127.0.0.1:80' > /start.sh && chmod +x /start.sh

# Используем ENTRYPOINT для запуска скрипта
ENTRYPOINT ["/start.sh"]
