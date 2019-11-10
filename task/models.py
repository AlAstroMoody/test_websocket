from datetime import timedelta

from django.db import models


# работа со временем DurationField?

class TaskModel(models.Model):
    input_url = models.CharField(max_length=50, verbose_name = "Введите Url")

    objects = models.Manager()

    def __str__(self):
        return self.input_url

    class Meta:
        verbose_name = 'Ввод url-ов'
        verbose_name_plural = 'Ввод url-ов'

class OutputModel(models.Model):
    save_url = models.CharField(max_length=50)
    save_title = models.CharField(max_length=50)
    save_h1 = models.CharField(max_length=50)
    save_encoding = models.CharField(max_length=50)
    objects = models.Manager()
