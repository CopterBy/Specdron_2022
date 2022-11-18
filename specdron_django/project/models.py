from django.db import models

# Create your models here.


# python manage.py makemigrations project # создание файла БД в папке migrations
# python manage.py migrate project # выполнение миграции данных для приложения project
# python manage.py migrate # выполнение миграции данных для всего проекта


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')