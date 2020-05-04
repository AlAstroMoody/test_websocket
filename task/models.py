from django.db import models


class TaskModel(models.Model):
    input_url = models.CharField(max_length=50, verbose_name="Введите Url")
    input_minutes = models.IntegerField(default=0, verbose_name="минут")
    input_seconds = models.IntegerField(default=0, verbose_name="секунд")

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
    seconds = models.IntegerField(default=0)
