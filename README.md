<img src="[](https://github.com/Just279/AeraOkulo/blob/main/apliko/static/image/logo.png)">
 Веб-сервис для мониторинга воздушного пространства
Создан исключительно для систем под архитектурой linux **(Ubuntu, Kali linux, Debian)**

Воспользоваться этим репозиторием в случае, если у вас возникнут проблемы с Docker образом.

1. Необходимо в командной строке linux установить следующее:

**apt install ffmpeg**

**pip install ultralytics Django Pillow numpy opencv-python**

2. Далее прописать следующие команды в папке с веб-сервисом:

**python manage.py makemigrations** 

**python manage.py migrate** 

**python manage.py runserver 127.0.0.1:80** 



После этого веб-сервис должен запуститься без ошибок. При возникновении ошибок в консоли, доустановить необходимые пакеты в зависимости от того какая библиотека отсутсвует указанная в ошибке. (Хотя этого произойти не должно)
