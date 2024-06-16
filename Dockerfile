FROM python:latest


RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0

WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80
EXPOSE 8000

RUN echo '#!/bin/bash\n\
python manage.py makemigrations\n\
python manage.py migrate\n\
python manage.py runserver 0.0.0.0:8000' > /start.sh && chmod +x /start.sh


ENTRYPOINT ["/start.sh"]
