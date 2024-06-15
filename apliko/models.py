
from django.db import models
from django.core.validators import FileExtensionValidator


class Fotilo(models.Model):
    name=models.CharField(max_length=50,verbose_name='Название')
    location=models.CharField(max_length=50,verbose_name='Местоположение')
    def __str__(self):
       return str(self.name)
    class Meta:
        verbose_name_plural='Камеры'
        verbose_name='Камера'
        ordering=['name']

class Mesagoj(models.Model):
    name=models.CharField(max_length=50,verbose_name='Название')
    description=models.TextField(verbose_name='Описание')
    time=models.DateTimeField(verbose_name='Время',auto_now_add=True)
    is_new3=models.TextField(verbose_name='Актуальность',null=True,default='False')
    def __str__(self):
       return str(self.name)
    class Meta:
        verbose_name_plural='События'
        verbose_name='Событие'
        ordering=['-time']

class Vidbendo(models.Model):
    upload = models.FileField(upload_to = 'apliko/static/source_video/', validators =[FileExtensionValidator(allowed_extensions=['mp4'])])
    time=models.DateTimeField(verbose_name='Время',auto_now_add=True, null=True, blank=True)
    name=models.TextField(verbose_name='Путь', null=True, blank=True)
    in_process=models.TextField(verbose_name='В обработке', null=True, blank=True)
    st256=models.TextField(verbose_name='Таймлайн', null=True, blank=True)
    def __str__(self):
       return str('Видео ')
    class Meta:
        verbose_name_plural='Видео'
        verbose_name='Видео'
        ordering=['-time']

class Foto(models.Model):
    upload = models.FileField(upload_to = 'apliko/static/source_foto/', validators =[FileExtensionValidator(allowed_extensions=['jpg','png'])])
    time=models.DateTimeField(verbose_name='Время',auto_now_add=True, null=True, blank=True)
    name=models.TextField(verbose_name='Путь', null=True, blank=True)
    name_txt=models.TextField(verbose_name='Путь txt', null=True, blank=True)
    labels=models.TextField(verbose_name='Метки', null=True, blank=True)
    def __str__(self):
       return str('Фото ')

    class Meta:
        verbose_name_plural='Фото'
        verbose_name='Фото'
        ordering=['-time']

class Arkivo(models.Model):
    upload = models.FileField(upload_to = 'apliko/static/source_arkivo/', validators =[FileExtensionValidator(allowed_extensions=['zip'])])
    time=models.DateTimeField(verbose_name='Время',auto_now_add=True, null=True, blank=True)
    name=models.TextField(verbose_name='Путь', null=True, blank=True)
    name_arch=models.TextField(verbose_name='Путь к архиву', null=True, blank=True)
    name_arch_lbls=models.TextField(verbose_name='Путь к меткам', null=True, blank=True)
    def __str__(self):
       return str('Архив ')

    class Meta:
        verbose_name_plural='Архивы'
        verbose_name='Архив'
        ordering=['-time'] 



