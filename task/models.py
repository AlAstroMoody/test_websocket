from django.db import models


# работа со временем DurationField?
# добавить в модель поля под: значения из парсера
class TaskModel(models.Model):
    input_url = models.CharField(max_length=50, verbose_name = "Введите Url")
    objects = models.Manager()

    def __str__(self):
        return self.input_url

    class Meta:
        verbose_name = 'Ввод url-ов'
        verbose_name_plural = 'Ввод url-ов'
