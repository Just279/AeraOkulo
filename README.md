

<br/>

![](https://github.com/Just279/AeraOkulo/blob/main/apliko/static/image/name.png)

___

**Веб-сервис для мониторинга воздушного пространства
Создан исключительно для систем под архитектурой linux** ***(Ubuntu, Kali linux, Debian)***
Сам Docker образ лежит на Яндекс диске. Команды по развертыванию образа находятся в этом репозитории в файле с названием Запуск  докера.txt 

**Подключение веб-камеры к сервису возможно только при развертывании веб-сервиса вне контейнера и локально**

*Воспользоваться этим репозиторием в случае, если у вас возникнут проблемы с Docker образом.*

1. Необходимо в командной строке linux установить следующее:
```
apt install ffmpeg
```

```
pip install ultralytics Django Pillow numpy opencv-python
```
<br/>


2.  Далее прописать следующие команды в папке с веб-сервисом:

```
python manage.py makemigrations
``` 

```
python manage.py migrate
```

```
python manage.py runserver 127.0.0.1:80
``` 

<br/>

После этого веб-сервис должен запуститься без ошибок. При возникновении ошибок в консоли, доустановить необходимые пакеты в зависимости от того какая библиотека отсутсвует (указанная в ошибке). (Хотя этого произойти не должно)


## Разворачивание виртуальной среды venv в Python

**1. Установка Python:** <br/>
Убедитесь, что Python установлен на вашем компьютере. Вы можете проверить это, открыв командную строку (или терминал) и набрав команду:

```sh
python3 --version
```

Если Python не установлен, скачайте его с официального сайта [python.org](https://www.python.org) и установите.

**2. Создание виртуальной среды:**<br/>
Выполните следующую команду для создания новой виртуальной среды. Замените myenv на желаемое имя для вашей виртуальной среды:

```sh
python3 -m venv myenv
```

**3. Активация виртуальной среды:**<br/>
После создания виртуальной среды, ее нужно активировать.
<br/>
На Linux:
```sh
source myenv/bin/activate
```
После активации вы должны увидеть (myenv) в начале командной строки, что указывает на активированную виртуальную среду.


**4. Установка пакетов в виртуальной среде:**<br/>
Когда виртуальная среда активирована, вы можете устанавливать пакеты с помощью pip и они будут установлены только в этой среде:
```sh
pip install package_name
```

**5. Деактивация виртуальной среды:**<br/>
Когда вы закончите работать, вы можете деактивировать виртуальную среду с помощью команды:
```
deactivate
```
